import urllib.request
import ssl
import json

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

def build_message(person):
    name, goal, day = person['name'], person['goal'], person['days_in']
    if person['goal_type'] == "perte":
        return f"{name} — Jour {day}. Objectif: {goal}. Bois de l'eau et bouge 20 min."
    elif person['goal_type'] == "muscle":
        return f"{name} — Jour {day}. Objectif: {goal}. Mange assez de proteines et dors bien."
    else:
        return f"{name} — Jour {day}. Objectif: {goal}. Continue comme ca."

coach = json.load(open("coach.json"))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for person in coach:
    msg = build_message(person)
    req = urllib.request.Request(
        f"https://ntfy.sh/{TOPIC}",
        data=msg.encode(),
        method="POST",
    )
    urllib.request.urlopen(req, context=ctx)
    print(f"{person['name']}: {msg}")
