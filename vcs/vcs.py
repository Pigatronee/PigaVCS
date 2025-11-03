import os
import hashlib
import pickle
import datetime

# Make init 
def init_vcs():
    os.makedirs(".vcs_storage", exist_ok=True)
    print("VCS started")

# List snapshots
# TODO: make this list timestamp and commit message
# ---------
def list_snapshots(directory, number_of_snapshots):
    if not os.path.exists(directory):
        print(f"Can't find directory {directory}")
        return

    snapshots = os.walk(directory)
    count = 0

    for root, dirs, files in snapshots:
        for file in files:
            print(file)
            count += 1 

            if count >= number_of_snapshots or file == "":
                return 

# Make a snapshot with Snapshot data (crazy shit)
def snapshot(directory, message="Empty Message"):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {
        "files": {},
        "message": message,
        "timestamp": datetime.datetime.now().isoformat() 
    }

    timestamp = datetime.datetime.now().isoformat()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ".vcs_storage" in os.path.join(root, file):
                continue

            file_path = os.path.join(root, file)

            with open(file_path, "rb") as f:
                content = f.read()
                snapshot_hash.update(content)
                snapshot_data["files"][file_path] = content


    hash_digest = snapshot_hash.hexdigest()
    snapshot_data["file_list"] = list(snapshot_data["files"].keys())

    with open(f".vcs_storage/{hash_digest}", "wb") as f:
        pickle.dump(snapshot_data, f)

    print(f"Snapshot created with hash {hash_digest}")

# Revert back to old snapshots 
# TODO: Add functionality to revert back to commit message
# ----------
def revert_to_snapshot(hash_digest):
    snapshot_path = f".vcs_storage/{hash_digest}"
    if not os.path.exists(snapshot_path):
        print("Snapshot probably doesn't exist")
        return
    with open (snapshot_path, "rb") as f:
        snapshot_data = pickle.load(f)

    for file_path, content in snapshot_data["files"].items():
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(content)

    current_files = set()
    for root, dirs, files in os.walk(".", topdown=True):
        if ".vcs_storage" in root:
            continue
        for file in files:
            current_files.add(os.path.join(root, file))

    snapshot_files = set(snapshot_data["file_list"])
    files_to_delete = current_files - snapshot_files

    for file_path in files_to_delete:
        os.remove(file_path)
        print(f"Removed {file_path}")
    print(f"Reverted to snapshot {hash_digest}")

# TODO: Clean this up
# -----------
if __name__ == "__main__":
    import sys 
    command = sys.argv[1]

    if command == "init":
        init_vcs()
    elif command in ("help", "--help"):
        print("commands:\n init \n snapshot \n revert (HashCode) \n List (number of hashes to list )")
    elif command == "snapshot":
        snapshot(".")
    elif command == "revert":
        revert_to_snapshot(sys.argv[2])
    elif command == "list":
        list_snapshots(".vcs_storage", int (sys.argv[2]))
    else:
        print("Unknown Command :( ")

