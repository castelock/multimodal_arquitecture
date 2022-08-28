from Gesture_Recognition import GestureRecognition
from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor

import sys
import mediapipe as mp
import tensorflow as tf
# from Speech_Recognition import SpeechRecognition
from tensorflow.keras.models import load_model

class InteractionManager:
    

    """def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def activateUI(self):                

        self.window.show()

        self.app.exec()

    def activateGestureInteraction(self):
        
        gr = GestureRecognition()
        
        className = gr.recognize_handGestures()

        print("The prediction is", className)

        self.window.activateFocus("textboxaAge")

        # sr = SpeechRecognition()
        # sr.list_mics()
        # sr.speechRecognition()"""

    def __init__(self) -> None:
        pass

             

        

    def activateGestureInteraction(self):
        
        app = QApplication(sys.argv)
        window = MainWindow()

        window.show()

        app.exec()

        gr = GestureRecognition()
        
        className = gr.recognize_handGestures()

        print("The prediction is", className)

        window.activateFocus("textboxAge")

        # sr = SpeechRecognition()
        # sr.list_mics()
        # sr.speechRecognition()
    
    



