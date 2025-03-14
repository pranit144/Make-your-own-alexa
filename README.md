# Voice Assistant

A Python-based voice assistant that can execute various tasks such as playing music, checking the weather, sending emails, fetching Wikipedia summaries, and more. It integrates speech recognition, text-to-speech, and AI-driven responses using Google's Gemini AI.

## Features
- **Speech Recognition:** Understands and processes voice commands.
- **Text-to-Speech:** Responds verbally using pyttsx3.
- **YouTube Control:** Plays songs on YouTube using PyWhatKit.
- **Time & Date Queries:** Tells the current time and date.
- **Application Control:** Opens Notepad, Chrome, and VS Code.
- **Wikipedia Search:** Fetches brief summaries from Wikipedia.
- **Weather Updates:** Provides weather details for any city.
- **Email Sending:** Sends emails using SMTP.
- **WhatsApp Messaging:** Sends instant WhatsApp messages.
- **Notes Management:** Takes and saves voice notes.
- **Mathematical Calculations:** Evaluates expressions.
- **System Commands:** Shutdown, restart, sleep mode.
- **Web Browsing:** Opens websites on command.
- **AI Chat Integration:** Uses Gemini AI for general queries.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API Keys:
   - **Google Gemini AI**: Set up your API key in the script.
   - **OpenWeather API**: Replace `YOUR_OPENWEATHER_API_KEY` with a valid API key.

4. Run the assistant:
   ```bash
   python main.py
   ```

## Usage
- Run the script and speak commands like:
  - "Play Shape of You"
  - "What is the weather in New York?"
  - "Open Notepad"
  - "Send email"
  - "Search Wikipedia for Python programming"
  - "Calculate 5 + 3"
  - "Shutdown the system"
  - "Tell me a joke"

## Dependencies
- `speechrecognition`
- `pyttsx3`
- `pywhatkit`
- `datetime`
- `os`
- `google-generativeai`
- `wikipedia`
- `smtplib`
- `requests`
- `webbrowser`

## Future Enhancements
- Add voice authentication.
- Expand AI chatbot capabilities.
- Integrate smart home controls.
- Improve error handling.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

