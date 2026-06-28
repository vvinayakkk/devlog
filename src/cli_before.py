import sys
import datetime

def f(m, l="INFO"):
    t = datetime.datetime.now().isoformat()
    print("["+l+"] ["+t+"] "+m)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f(" ".join(sys.argv[1:]))
    else:
        print("Usage: python cli.py <message>")