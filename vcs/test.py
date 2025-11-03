import hashlib
import datetime 
import pickle


hash_digest = "5a54b9e2e245528a53fad52e3c8498750fae28b9c461356c086b45112b6d616b"
snapshot_path = f".vcs_storage/{hash_digest}"

with open(snapshot_path, "rb") as f:
    snapshot_data = pickle.load(f)
    message = snapshot_data.get("message", "no message")
    timestamp = snapshot_data.get("timestamp", "no timestamp")

    print("commit: ", hash_digest)
    print("message: ", message)
    print("timestamp: ", timestamp)

