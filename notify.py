import urllib.request
import ssl
import json
import os
import anthropic

TOPIC = "louis-buzz-2026"  # change this to match what you typed in the app

def build_message(person):
    name, goal, day = person['name'], person['goal'], person['days_in']
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=60,
            messages=[{
                "role": "user",
                "content": (
                    f"Tu es un coach diet concis. Ecris UNE phrase de motivation en francais pour "
                    f"{name}, jour {day}, objectif: {goal}. Une phrase courte, directe, pas de guillemets."
                )
            }]
        )
        return response.content[0].text.strip()
    except Exception:
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
