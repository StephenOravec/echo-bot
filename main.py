# main.py
# Core logic for Echo Bot

def echo_bot_logic(text):
    """
    Returns a response based on input text:
    - If text is 'gm', reply 'gm'
    - Else, reply "You said: 'text'"
    """
    if text.lower() == "gm":
        return "gm"
    else:
        return f"You said: '{text}'"