# Speech to Text (Persian) with GUI

This is a Python-based speech-to-text application that converts spoken Persian (Farsi) language into text using Google Speech Recognition. It also features text-to-speech (TTS) functionality and a GUI built with Tkinter.

## Features
- 🎤 **Continuous Speech Recognition** (Persian/Farsi)
- 🔊 **Text-to-Speech (TTS)** using `pyttsx3`
- 📝 **Text Display** in a scrollable text box
- 📋 **Copy Text** to clipboard
- ⏹️ **Start/Stop Recording** for better control
- 🎨 **User-Friendly GUI** with Tkinter

## Requirements
Make sure you have Python installed. Then install the required dependencies:
```sh
pip install speechrecognition pyttsx3 tkinter
```

## How to Run
Run the following command in your terminal or command prompt:
```sh
python script.py
```

## Usage
1. Click on the **"Start Recording"** button.
2. Speak in Persian, and the text will appear in the text box.
3. The application will also read the recognized text aloud.
4. Click **"Stop Recording"** to stop speech recognition.
5. Click **"Copy Text"** to copy the transcribed text to the clipboard.

## Troubleshooting
- Ensure your microphone is properly connected and working.
- If the app doesn't recognize your speech, check your internet connection (Google Speech Recognition requires internet access).
- If you get a `RequestError`, Google's API might be temporarily unavailable.

## License
This project is open-source and available under the MIT License.

