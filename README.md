# AI Voice Assistant

A Python-based AI Voice Assistant that listens to voice commands and performs tasks like opening websites and responding using text-to-speech.

---

FEATURES:

-  Voice command recognition
-  Text-to-speech response
-  Opens websites (YouTube, Google, Facebook, etc.)
-  Continuous listening mode
-  Lightweight and fast execution

---

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- Webbrowser module
- PyAudio

---

## Project Structure

AI-Voice-Assistant/
│── index.py  
│── requirements.txt  
│── README.md  
│── .gitignore  

---

##  Installation & Setup

###  Clone the Repository

```bash
git clone https://github.com/sujitpatil2223/ai-voice-assistant.git
cd ai-voice-assistant

### Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python index.py
```

---

## How It Works

1. The microphone captures user voice input.
2. SpeechRecognition converts speech to text.
3. The assistant processes the command.
4. pyttsx3 converts the response back to speech.
5. The requested website is opened using the webbrowser module.

---

## Future Improvements

- Add GUI interface (Tkinter / PyQt)
- Add AI chatbot integration
- Add weather & news APIs
- Add task automation features
- Store command history using MySQL
