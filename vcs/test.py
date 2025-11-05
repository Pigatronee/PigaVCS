import os
from datetime import datetime

directory = "your_directory_path"

directory = ".vcs_storage/"

# Walk through the directory
snapshots = os.walk(directory)

for root, dirs, files in snapshots:
    # Full paths to files
    full_paths = [os.path.join(root, file) for file in files]
    
    # Sort files by modification time (most recent first)
    full_paths.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    # Alternatively, for creation time (on Windows)
    # full_paths.sort(key=lambda x: os.path.getctime(x), reverse=True)
    
    # Display file info
    for file_path in full_paths:
        mod_time = os.path.getmtime(file_path)
        print(f"{file_path} - Last modified: {datetime.fromtimestamp(mod_time)}")

