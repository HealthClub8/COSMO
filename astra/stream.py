import os
import random
import subprocess

# Specify the directory where the files are stored
directory = 'db'
# Define the IP address of Chromecast 
ip_address = '192.168.1.141'

# Get all files from the directory
files = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

# Read all lines from all files
all_lines = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            all_lines.append((file, line.strip()))  # Store tuple of filename and line

# Pick a random line and its corresponding file
random_file, random_line = random.choice(all_lines)

# Print the result
print(f"File: {random_file}\nLine: {random_line}")


# Run chromecast.py and pass the random line as a parameter
subprocess.run(['python', 'chromecast.py', ip_address, random_line])