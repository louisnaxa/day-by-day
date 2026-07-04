import urllib.request
import ssl
import certifi
import json
from coach_message import generate_message

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

# Use certifi's certificate bundle — correct fix for macOS Python's missing system certs.
# On Linux (GitHub Actions), ssl.create_default_context() works without this.
ctx = ssl.create_default_context(cafile=certifi.where())

coach = json.load(open("coach.json"))

for person in coach:
    msg = generate_message(person)
    req = urllib.request.Request(
        f"https://ntfy.sh/{TOPIC}",
        data=msg.encode(),
        method="POST",
    )
    urllib.request.urlopen(req, context=ctx)
    print(f"{person['name']}: {msg}")
