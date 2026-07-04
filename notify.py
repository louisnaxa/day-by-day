import urllib.request
import ssl
import json

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

coach = json.load(open("coach.json"))               # open the file and parse it as a list

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for person in coach:                               # repeat once per person in the list
    msg = f"{person['name']} — objectif {person['goal']}. {person['message']}"
    req = urllib.request.Request(
        f"https://ntfy.sh/{TOPIC}",
        data=msg.encode(),
        method="POST",
    )
    urllib.request.urlopen(req, context=ctx)
    print(f"Notification sent to {person['name']}.")
