#!/usr/bin/env python3
"""
moa_advisor_drain.py - nightly queue drainer for the free-tier skills.

Run by the Hermes cron after the OpenRouter daily free cap resets. Attempts
--run-queue for both moa-free and model-advisor. If still capped, each script
re-queues and reports the next reset. Results are appended to a log file.

Usage (from cron):
  python moa_advisor_drain.py
"""
import os, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
LIB  = r"C:/Users/nator/hermes-skills-lib"
MOA  = os.path.join(LIB, "skills", "moa-free", "moa_all.py")
ADV  = os.path.join(LIB, "skills", "model-advisor", "model_advisor.py")
LOG  = os.path.join(LIB, "drain.log")

def run(label, script):
    if not os.path.exists(script):
        return f"[{label}] MISSING: {script}"
    try:
        out = subprocess.run(["python", script, "--run-queue"],
                             capture_output=True, text=True, timeout=300)
        return f"[{label}]\n{out.stdout.strip()}\n{out.stderr.strip()}"
    except Exception as e:
        return f"[{label}] ERROR: {e}"

def main():
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [f"===== DRAIN {ts} ====="]
    lines.append(run("MOA", MOA))
    lines.append(run("ADVISOR", ADV))
    lines.append("")
    with open(LOG, "a") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))

if __name__ == "__main__":
    main()
