import subprocess
from datetime import datetime
import os


def capture_robot_logs():
    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Generate timestamp for log filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/robot_log_{timestamp}.txt"

    print("=" * 50)
    print("🎯 Listening to logs...")
    print(f"📁 Logging to: {log_filename}")
    print("🤖 Starting robot connection...")
    print("=" * 50)

    try:
        # Use the Python executable from your virtual environment
        python_exe = r".venv\Scripts\python.exe"

        # Start the robot program
        process = subprocess.Popen(
            [
                python_exe,
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
        )

        with open(log_filename, "w", encoding="utf-8") as log_file:
            # Write header to log file
            log_file.write(f"Robot Log Session Started: {datetime.now()}\n")
            log_file.write("=" * 50 + "\n")
            log_file.flush()

            # Capture both stdout and stderr in real-time
            while True:
                output = process.stdout.readline()  # type: ignore
                if output == "" and process.poll() is not None:
                    break
                if output:
                    timestamp_str = datetime.now().strftime("%H:%M:%S.%f")[
                        :-3
                    ]  # Include milliseconds
                    log_entry = f"[{timestamp_str}] {output.rstrip()}\n"

                    # Write to file
                    log_file.write(log_entry)
                    log_file.flush()

                    # Print to console (with color for timestamp) - ensure flushed
                    print(
                        f"\033[36m[{timestamp_str}]\033[0m {output.rstrip()}",
                        flush=True,
                    )

        # Wait for process to complete
        process.wait()

    except KeyboardInterrupt:
        print("\n🛑 Logging stopped by user")
        if "process" in locals():
            process.terminate()  # type: ignore
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
    finally:
        print(f"📝 Log saved to: {log_filename}")


if __name__ == "__main__":
    capture_robot_logs()
