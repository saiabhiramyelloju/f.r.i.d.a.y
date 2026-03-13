import random
import memory

def detect_intent(message):
    remember_keyWords = [
        "remember",
        "note this",
        "take this",
        "store this"
    ]

    for word in remember_keyWords:
        if word in message.lower():
            return memory
    return "normal"

def process_message(message):
    print("Processing: ",message)

    greetings = ["hello","hi"]
    wishes = [
        "good morning",
        "good afternoon",
        "good evening",
        "good night"
    ]
    for word in greetings:
        if word == message.lower():
            return random.choice(greetings) + ", I am F.R.I.D.A.Y"    
    return "i dont understand"