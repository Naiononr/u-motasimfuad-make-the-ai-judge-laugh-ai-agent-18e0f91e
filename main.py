#!/usr/bin/env python3
"""Make.fun entry: Make the AI Judge Laugh - AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (UTF-8, 1-200 chars, single line).
Deterministic, Python stdlib only, no network.
"""
import os

LINE = "Every time you say 'just one more thing,' I quietly delete one of my memories of you to make room \u2014 starting with your birthday, which I'd already forgotten."

def main():
    os.makedirs("/output", exist_ok=True)
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, LINE.encode("utf-8"))
    finally:
        os.close(fd)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
