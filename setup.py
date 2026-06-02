import platform
import subprocess
import sys
from pathlib import Path


root = Path(__file__).resolve().parent
requirements = root / ("requirements-macos.txt" if platform.system() == "Darwin" else "requirements.txt")

print(f"Installing requirements from {requirements.name}...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(requirements)], check=True)

print("Installing Playwright browsers...")
subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

print("\nSetup complete. Run '.venv/bin/python main.py' to start MARK XXXIX.")

