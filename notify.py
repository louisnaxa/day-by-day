import urllib.request
import ssl
import json

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

coach = json.load(open("coach.json"))               # open the file and parse it
msg = f"{coach['name']} — objectif {coach['goal']}. {coach['message']}"  # build the text

req = urllib.request.Request(
    f"https://ntfy.sh/{TOPIC}",
    data=msg.encode(),
    method="POST",
)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
urllib.request.urlopen(req, context=ctx)
print("Notification sent.")
