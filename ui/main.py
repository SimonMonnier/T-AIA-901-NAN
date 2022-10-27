import tkinter
from tkinter import ttk
import customtkinter
from Orchestrator import Orchestrator
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    if __name__ == "__main__":
        Or = Orchestrator()
        Or.orchestrator()
