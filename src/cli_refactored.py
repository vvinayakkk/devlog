import sys
import datetime


def log_entry(message, level="INFO"):
    """Log a timestamped entry to stdout."""
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{level}] [{timestamp}] {message}")


def main():
    if len(sys.argv) <= 1:
        script_name = sys.argv[0]
        print(f"Usage: python {script_name} <message>")
        return

    message = " ".join(sys.argv[1:])
    log_entry(message)


if __name__ == "__main__":
    main()
