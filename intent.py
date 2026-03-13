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

    #keywords that messages have
    greetings = ["/start","hello","hi"]
    wishes = [
        "good morning",
        "good afternoon",
        "good evening",
        "good night"
    ]
    calculations = [
        "add",
        "subtract",
        "multiply",
        "divide",
        "to the power"
    ]
    #greetings
    for word in greetings:
        if word == message.lower():
            return "Hello, I am F.R.I.D.A.Y\nHow can i help you today?"
    #wishes
    for word in wishes:
        if word == message.lower():
            return message+" ,sir"
    #creater of friday response
    if message.lower() == ("who created you" or "founder of friday" or "creater of you"):
        return "AbhiRam"
    #addition
    if message.lower() == "/add":
        return "give me two numbers to for addition with spaces between\nExample: 2 3"
    numbers = message.split()
    if len(numbers) == 2:
        numbers[0].isdigit()
        numbers[1].isdigit()        
        a = int(numbers[0])
        b = int(numbers[1])
        result = a + b
    #subtraction
    if message.lower() == "/subtract":
        return "give me two numbers to for subtraction with spaces between\nExample: 2 3"
    numbers = message.split()
    if len(numbers) == 2:
        numbers[0].isdigit()
        numbers[1].isdigit()        
        a = int(numbers[0])
        b = int(numbers[1])
        result = a - b
    #multiplication
    if message.lower() == "/muliply":
        return "give me two numbers to for multiplication with spaces between\nExample: 2 3"
    numbers = message.split()
    if len(numbers) == 2:
        numbers[0].isdigit()
        numbers[1].isdigit()        
        a = int(numbers[0])
        b = int(numbers[1])
        result = a * b
    #division
    if message.lower() == "/divide":
        return "give me two numbers to for division with spaces between\nExample: 2 3"
    numbers = message.split()
    if len(numbers) == 2:
        numbers[0].isdigit()
        numbers[1].isdigit()        
        a = int(numbers[0])
        b = int(numbers[1])
        result = a / b
    return "I coudn't process your request as am under development\nPlease try again later"
