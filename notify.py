import urllib.request
import ssl
import json
from coach_message import generate_message

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

coach = json.load(open("coach.json"))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for person in coach:
    msg = generate_message(person)
    req = urllib.request.Request(
        f"https://ntfy.sh/{TOPIC}",
        data=msg.encode(),
        method="POST",
    )
    urllib.request.urlopen(req, context=ctx)
    print(f"{person['name']}: {msg}")
