import subprocess
from datetime import datetime
import os
import time
import signal
import atexit
import sys
from types import FrameType
from typing import TextIO, Optional, NoReturn


# Global variables
csv_file_handle: Optional[TextIO] = None
csv_filename: Optional[str] = None


def cleanup_handler() -> None:
    """Write END status and close file when program exits"""
    if csv_file_handle and not csv_file_handle.closed:
        csv_file_handle.write("END,END,END,END,END\n")
        csv_file_handle.flush()
        csv_file_handle.close()


def signal_handler(signum: int, frame: Optional[FrameType]) -> NoReturn:
    """Handle signals by calling cleanup and then exiting"""
    cleanup_handler()
    sys.exit(0)


def capture_robot_logs():
    global csv_file_handle, csv_filename

    # Create ui/stream directory if it doesn't exist
    stream_dir = "ui/stream"
    if not os.path.exists(stream_dir):
        os.makedirs(stream_dir)

    # CSV file for real-time data streaming
    csv_filename = "ui/stream/info.csv"

    # Register cleanup handlers
    atexit.register(cleanup_handler)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print("=" * 50)
    print("🎯 Listening to robot logs...")
    print(f"📁 Streaming CSV to: {csv_filename}")
    print("🤖 Starting robot connection...")
    print("=" * 50)

    # Initialize CSV file with header and INIT row
    global csv_file_handle
    csv_file_handle = open(csv_filename, "w", encoding="utf-8")
    csv_file_handle.write(
        "HEALTH,LIGHT, PRESSURE_LEFT, PRESSURE_RIGHT, PRESSURE_BACK\n"
    )
    csv_file_handle.write("INIT, INIT, INIT, INIT, INIT\n")
    csv_file_handle.flush()

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

        csv_file_handle.seek(0, 2)  # Seek to end of file for appending
        # Real-time monitoring using character-by-character reading
        output_buffer = ""

        while True:
            # Check if process is still running
            if process.poll() is not None:
                # Process has ended, no need to process remaining output
                # since we've been processing line by line in real-time
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
                            if line.strip():  # Skip empty lines
                                _write_csv_entry(line.strip())

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
        cleanup_handler()
        print(f"📝 CSV data saved to: {csv_filename}")


def _write_csv_entry(line: str) -> None:
    """Write pure CSV data to file and display to console"""
    # Filter out non-CSV lines (connection progress, search messages, etc.)
    if _is_valid_csv_line(line) and csv_file_handle:
        # Write pure CSV line to file (no timestamp, no formatting)
        csv_file_handle.write(f"{line}\n")
        csv_file_handle.flush()

    # Display to console with timestamp for monitoring (all lines)
    timestamp_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"\033[36m[{timestamp_str}]\033[0m {line}", flush=True)


def _is_valid_csv_line(line: str) -> bool:
    """Check if a line is valid CSV data that should be written to file"""
    line = line.strip()

    # Skip empty lines
    if not line:
        return False

    # Skip connection/search messages
    if "Searching for" in line:
        return False

    # Skip progress bars (contain % and | characters)
    if "%" in line and "|" in line:
        return False

    # Skip other pybricksdev messages
    if "The program was stopped" in line:
        return False

    # Skip lines that don't contain expected sensor indicators or CSV format
    # Allow lines with sensor indicators like "HEALTH_INDICATOR: 100"
    # or proper CSV format with commas
    if (
        "HEALTH" in line
        or "LIGHT" in line
        or "PRESSURE" in line
        or "," in line
        or "NONE" in line
        or "RED" in line
        or "GREEN" in line
    ):
        return True

    # Skip everything else
    return False


if __name__ == "__main__":
    capture_robot_logs()
