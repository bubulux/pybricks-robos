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
                "src/main.py",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )

        with open(log_filename, "w", encoding="utf-8") as log_file:
            # Write header to log file
            log_file.write(f"Robot Log Session Started: {datetime.now()}\n")
            log_file.write("=" * 50 + "\n")
            log_file.flush()

            # Capture stdout in real-time
            for line in iter(process.stdout.readline, ""):  # type: ignore
                if line:
                    timestamp_str = datetime.now().strftime("%H:%M:%S.%f")[
                        :-3
                    ]  # Include milliseconds
                    log_entry = f"[{timestamp_str}] {line.rstrip()}\n"

                    # Write to file
                    log_file.write(log_entry)
                    log_file.flush()

                    # Print to console (with color for timestamp)
                    print(f"\033[36m[{timestamp_str}]\033[0m {line.rstrip()}")

            # Capture any remaining stderr
            stderr_output = process.stderr.read()  # type: ignore
            if stderr_output:
                error_entry = f"[ERROR] {stderr_output}\n"
                log_file.write(error_entry)
                print(f"\033[31m[ERROR]\033[0m {stderr_output}")

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
