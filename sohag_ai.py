
import datetime

print("AI Assistant: Hello! Ami tomar personal AI.")
print("Type 'exit' to close the AI.")

while True:
    user = input("\nYou: ").lower()

    if user == "exit":


        print("AI: Goodbye!")
        break

    elif "hello" in user or "hi" in user:
        print("AI: Hello! How are you?")

    elif "your name" in user:
        print("AI: My name is Personal AI.")

    elif "time" in user:
        now = datetime.datetime.now()
        print("AI: Current time is", now.strftime("%I:%M %p"))

    elif "date" in user:
        today = datetime.date.today()
        print("AI: Today's date is", today)

    elif "how are you" in user:
        print("AI: I am fine! How can I help you?")

    elif "who created you" in user:
        print("AI: I was created by my developer.")

    else:
        print("AI: Sorry, I don't understand that yet.")
