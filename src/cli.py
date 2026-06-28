import sys
import datetime

def log_entry(message, level="INFO"):
    """Log a timestamped entry to stdout."""
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{level}] [{timestamp}] {message}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        log_entry(" ".join(sys.argv[1:]))
    else:
        print("Usage: python cli.py <message>")