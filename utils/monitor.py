import subprocess
from datetime import datetime
import os
import time
from typing import TextIO


def capture_robot_logs():
    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Generate timestamp for log filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"ui/logs/robot_log_{timestamp}.txt"

    print("=" * 50)
    print("🎯 Listening to logs...")
    print(f"📁 Logging to: {log_filename}")
    print("🤖 Starting robot connection...")
    print("=" * 50)

    process = None
    try:
        # Use the Python executable from your virtual environment
        python_exe = r".venv\Scripts\python.exe"

        # Start the robot program with additional buffering control
        process = subprocess.Popen(
            [
                python_exe,
                "-u",  # Force unbuffered output
                "-m",
                "pybricksdev",
                "run",
                "ble",
                "-n",
                "bubulux",
                "build/main.py",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Redirect stderr to stdout
            text=True,
            bufsize=0,  # Unbuffered
            universal_newlines=True,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        )

        with open(log_filename, "w", encoding="utf-8") as log_file:
            # Write header to log file
            log_file.write(f"Robot Log Session Started: {datetime.now()}\n")
            log_file.write("=" * 50 + "\n")
            log_file.flush()

            # Real-time monitoring using character-by-character reading
            output_buffer = ""

            while True:
                # Check if process is still running
                if process.poll() is not None:
                    # Process has ended, read any remaining output
                    remaining = process.stdout.read()  # type: ignore
                    if remaining:
                        output_buffer += remaining
                        _process_buffer_lines(output_buffer, log_file)
                    break

                # Read one character at a time for immediate processing
                try:
                    char = process.stdout.read(1)  # type: ignore
                    if char:
                        output_buffer += char

                        # Process complete lines immediately
                        if char == "\n":
                            lines = output_buffer.split("\n")
                            # Process all complete lines
                            # (all but the last, which might be incomplete)
                            for line in lines[:-1]:
                                if line:  # Skip empty lines
                                    _write_log_entry(line, log_file)

                            # Keep the last (potentially incomplete) line in buffer
                            output_buffer = lines[-1]
                    else:
                        # No more data available right now,
                        # small sleep to prevent busy waiting
                        time.sleep(0.001)

                except Exception as e:
                    print(f"Error reading from process: {e}")
                    break

        # Wait for process to complete
        if process:
            process.wait()

    except KeyboardInterrupt:
        print("\n🛑 Logging stopped by user")
        if process:
            process.terminate()
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
    finally:
        print(f"📝 Log saved to: {log_filename}")


def _process_buffer_lines(buffer: str, log_file: TextIO) -> None:
    """Process any remaining lines in the buffer"""
    lines = buffer.split("\n")
    for line in lines:
        if line.strip():  # Skip empty lines
            _write_log_entry(line, log_file)


def _write_log_entry(line: str, log_file: TextIO) -> None:
    """Write a log entry with timestamp to both file and console"""
    timestamp_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    log_entry = f"[{timestamp_str}] {line.rstrip()}\n"

    # Write to file immediately
    log_file.write(log_entry)
    log_file.flush()

    # Print to console (with color for timestamp) - ensure flushed
    print(f"\033[36m[{timestamp_str}]\033[0m {line.rstrip()}", flush=True)


if __name__ == "__main__":
    capture_robot_logs()
