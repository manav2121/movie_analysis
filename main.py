import os

print("Running data cleaning script...")
os.system("python scripts/data_cleaning.py")

print("Running analysis script...")
os.system("python scripts/analysis.py")

print("Running visualization script...")
os.system("python scripts/visualization.py")

print("Project completed successfully!")
