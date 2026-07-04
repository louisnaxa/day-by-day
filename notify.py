import urllib.request
import ssl

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

req = urllib.request.Request(
    f"https://ntfy.sh/{TOPIC}",
    data=b"Day 3. Ship something small.",
    method="POST",
)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
urllib.request.urlopen(req, context=ctx)
print("Notification sent.")
