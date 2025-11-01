# main.py
# Core logic for Echo Bot

import json

def echo_bot(request):
    """
    Returns a response based on input text:
    - If text is 'gm', reply 'gm'
    - Else, reply "You said: 'text'"
    """
    request_json = request.get_json(silent=True)
    text = request_json.get("text", "").strip() if request_json else ""

    if text.lower() == "gm":
        reply = "gm"
    else:
        reply = f"You said: '{text}'"

    response = [{
        "text": reply,
        "action": "CHAT",
        "actionContext": None
    }]

    return (json.dumps(response), 200, {"Content-Type": "application/json"})