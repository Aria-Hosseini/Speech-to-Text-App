import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

engine = pyttsx3.init()
r = sr.Recognizer()
stop_listening = False  

def SpeakText(command):
    """ تابع تبدیل متن به گفتار """
    engine.say(command)
    engine.runAndWait()

def recognize_speech():
    """ تابع ضبط صدا به‌صورت مداوم تا زمانی که متوقف شود """
    global stop_listening
    stop_listening = False  

    def listen_continuously():
        """ حلقه ضبط صدا به‌صورت مداوم """
        global stop_listening
        while not stop_listening:
            try:
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.5)
                    
                    status_label.config(text="🎤 گوش می‌دهم، لطفاً صحبت کنید...")
                    window.update()

                    audio2 = r.listen(source2)

                    MyText = r.recognize_google(audio2, language="fa-IR")

                    status_label.config(text="✅ متن دریافت شد!")
                    text_box.insert(tk.END, MyText + "\n")  
                    text_box.see(tk.END)  

                    SpeakText(MyText)  

            except sr.UnknownValueError:
                status_label.config(text="⚠️ متوجه نشدم، لطفاً دوباره امتحان کنید.")
            except sr.RequestError as e:
                status_label.config(text=f"❌ خطا در ارتباط با گوگل: {e}")
                break

    thread = threading.Thread(target=listen_continuously)
    thread.daemon = True  
    thread.start()

def stop_recognition():
    """ تابع متوقف کردن ضبط صدا """
    global stop_listening
    stop_listening = True
    status_label.config(text="⏹️ ضبط متوقف شد.")

def copy_text():
    """ تابع کپی متن در کلیپ‌بورد """
    text = text_box.get("1.0", tk.END)  
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()
    messagebox.showinfo("کپی شد!", "متن در کلیپ‌بورد کپی شد. 📋")

window = tk.Tk()
window.title("🎤 تبدیل گفتار به متن (فارسی)")
window.geometry("500x450")
window.resizable(False, False)

status_label = tk.Label(window, text="روی دکمه 'شروع ضبط' کلیک کنید و صحبت کنید.", fg="blue", font=("Arial", 12))
status_label.pack(pady=10)

text_box = scrolledtext.ScrolledText(window, width=60, height=10, font=("Arial", 12))
text_box.pack(pady=10)

start_button = tk.Button(window, text="🎤 شروع ضبط", font=("Arial", 12), command=recognize_speech, bg="green", fg="white")
start_button.pack(pady=5)

stop_button = tk.Button(window, text="⏹️ توقف ضبط", font=("Arial", 12), command=stop_recognition, bg="red", fg="white")
stop_button.pack(pady=5)

copy_button = tk.Button(window, text="📋 کپی متن", font=("Arial", 12), command=copy_text, bg="blue", fg="white")
copy_button.pack(pady=5)

window.mainloop()
