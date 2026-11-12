import random
import webbrowser
print("Welcome to My Chatbot!")
print("What is your Name?")
name=input("Enter your name \n")
print(f"Hii {name}!")
sent=["How are you?","What is going on today","What do you want to learn today","How can I help you?"]
print(random.choice(sent))
while True:
    query=input("Ask Anything (exit to quit)\n").lower()
    if query=="exit":
        print("Goodbye!")
        break
    elif "news" in query or "headline" in query:
        webbrowser.open("https://news.google.com/")
    elif "sports" in query or "cricket" in query:
        webbrowser.open("https://www.espn.com/")
    elif "weather" in query or "mausam" in query:
        city=input("Name of the city")
        print("Checking the weather in", city + "...")
        webbrowser.open("https://www.google.com/search?q=" + city + "+weather")
    elif "disaster" in query or "earthquake" in query:
        webbrowser.open("https://sachet.ndma.gov.in/")
    elif "trading" in query or "stock" in query or "market" in query:
        webbrowser.open("https://www.nseindia.com/")
    elif "fashion" in query or "outfit" in query:
        webbrowser.open("https://www.vogue.com/")
    elif "what is your name" in query or "what's your name" in query:
        print("My name is Chatboat")
        print("\n")
        print("Do you want to give me new name?")
        ans=input("yes or no").lower()
        if ans=="yes":
           Name=input("My new name")
           print(f"{Name}, it is nice name!")
           print("I like it")
           print(f"Now ,My name is {Name}")
        else:
           print("Okay!,You can call me Chatboat")
    elif "can you give me some motivation" in query or "motivation" in query:
        print("Don't worry about how slowly you move. What matters is that you never stop learning, growing, and believing in yourself. Every small step takes you closer to your dreams.")
        print("\n")
        print("if you want some more motivational line ,I can give you")
        anss=input("yes" or "no").lower()
        if anss=="yes":
            print("Believe in yourself \n","Never give up \n","Stay strong, stay focused \n",
               "Your time will come \n","Learn, grow, repeat \n")
        elif anss=="no":
            print("okay!")
            print("Be motivated")
        else:
            print("Are you feeling demotivated,today?")
            print("You can tell me")
            print("I am here to listen ")
            reply=input().lower()
            if "i am fine" in reply or "i,m fine" in reply:
                print("Then,Okay")
                print("Remember, I am always here")
            else:
                print("What happend?")
                print("How can I help you")
    elif "Tell me a joke" in query or "joke" in query or "jokes" in query:
        print("Here are some short, funny jokes")
        print("Why did the computer go to the doctor? Because it had a virus!")
        print("Why was the math book sad? It had too many problems.")
        print("Why don't eggs tell jokes? They might crack up!")
        print("Teacher: Why are you late? Student: Because the sign said, “School Ahead, Go Slow!")
        print("Why was the calendar so popular? It had lots of dates!")
    else:
        print("Sorry!")
        print("I have no access of this")







