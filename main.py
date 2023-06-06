import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import mainthread
import speech_recognition as sr
import threading
from kivy.utils import get_color_from_hex

class SpeechRecognitionApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Start speaking...", font_size=30, color=get_color_from_hex("#00FFFF"))
        layout.add_widget(self.label)
        return layout
    def recognize_speech(self):
        recognizer = sr.Recognizer()

        while True:
            try:
                with sr.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    text = recognizer.recognize_google(audio)
                    text = text.lower()
                    self.update_label(text)
            except sr.UnknownValueError:
                pass  # Ignore unknown speech
            except Exception as e:
                print(f"Error: {e}")

    @mainthread
    def update_label(self, text):
        self.label.text = f"Recognized: {text}"

    def on_start(self):
        threading.Thread(target=self.recognize_speech).start()

if __name__ == '__main__':
    SpeechRecognitionApp().run()
