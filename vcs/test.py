import hashlib
import datetime 

message = "Fixed a bug!"
timestamp = datetime.datetime.now().isoformat()
content = b"Hello world!"

h = hashlib.sha256()
h.update(content)
h.update(message.encode())
h.update(timestamp.encode())
print("Hash 1 is ", h.hexdigest())



