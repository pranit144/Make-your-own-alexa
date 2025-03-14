import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import google.generativeai as genai
import wikipedia
import smtplib
import requests
import webbrowser

# Configure Gemini AI
genai.configure(api_key="AIzaSyClLXoS5I0GGZQENj3JTuiUJztB1KqWocI")

model = genai.GenerativeModel("gemini-1.5-flash")
chat_session = model.start_chat(history=[])

# Initialize Speech Engine
engine = pyttsx3.init()
engine.setProperty("voice", engine.getProperty("voices")[1].id)  # Female voice


def talk(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def listen_command():
    """Listen for user command"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            return "I didn't understand. Can you repeat?"
        except sr.RequestError:
            return "Please check your internet connection."


def send_email(to, subject, message):
    """Send an email"""
    EMAIL = "your_email@gmail.com"
    PASSWORD = "your_password"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL, to, email_message)
        server.close()
        talk("Email sent successfully!")
    except Exception as e:
        talk("I was unable to send the email.")
        print(e)


def get_weather(city):
    """Get weather updates"""
    API_KEY = "YOUR_OPENWEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        weather_desc = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {weather_desc}."
    else:
        return "Sorry, I couldn't fetch the weather data."


def take_notes():
    """Take voice notes and save them"""
    talk("What should I write?")
    note = listen_command()
    with open("notes.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {note}\n")
    talk("Note saved successfully!")


def process_command(command):
    """Process and execute user commands"""

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {now}")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        talk(f"Today's date is {today}")

    elif "open notepad" in command:
        talk("Opening Notepad")
        os.system("notepad.exe")

    elif "open chrome" in command:
        talk("Opening Google Chrome")
        os.system("start chrome")

    elif "open vs code" in command:
        talk("Opening VS Code")
        os.system("code")

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        talk(f"Searching Wikipedia for {query}")
        result = wikipedia.summary(query, sentences=2)
        talk(result)

    elif "weather" in command:
        talk("Which city's weather do you want?")
        city = listen_command()
        weather = get_weather(city)
        talk(weather)

    elif "send email" in command:
        talk("To whom should I send the email?")
        recipient = listen_command()
        talk("What is the subject?")
        subject = listen_command()
        talk("What is the message?")
        message = listen_command()
        send_email(recipient, subject, message)

    elif "send message" in command:
        talk("Who should I send the message to?")
        contact = listen_command()  # Get recipient name/number
        talk("What should I say?")
        message = listen_command()
        pywhatkit.sendwhatmsg_instantly(f"+91{contact}", message)
        talk("Message sent successfully!")

    elif "note" in command:
        take_notes()

    elif "calculate" in command:
        talk("What calculation should I perform?")
        expression = listen_command()
        try:
            result = eval(expression)
            talk(f"The result is {result}")
        except:
            talk("Sorry, I couldn't calculate that.")

    elif "shutdown" in command:
        talk("Shutting down your computer")
        os.system("shutdown /s /t 1")

    elif "restart" in command:
        talk("Restarting your computer")
        os.system("shutdown /r /t 1")

    elif "sleep" in command:
        talk("Putting the system to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "open website" in command:
        talk("Which website should I open?")
        site = listen_command()
        webbrowser.open(f"https://{site}.com")

    else:
        # If not a predefined command, ask Gemini AI
        response = chat_session.send_message(command)
        talk(response.text)


# Run Alexa continuously
def run_alexa():
    while True:
        command = listen_command()
        process_command(command)


# Start the assistant
talk("Hello! How can I assist you?")
run_alexa()
