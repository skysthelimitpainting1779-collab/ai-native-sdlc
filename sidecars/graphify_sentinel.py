import time
import subprocess
import os
import sys

WATCH_INTERVAL = 30  # seconds between incremental checks

def run_graphify_sync():
    try:
        # Run incremental graphify update
        subprocess.run(["graphify", "--update"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception:
        pass

def main():
    print("[AI-Native SDLC] Graphify Sentinel Sidecar active. Monitoring file changes for knowledge graph sync...")
    while True:
        time.sleep(WATCH_INTERVAL)
        run_graphify_sync()

if __name__ == "__main__":
    main()
