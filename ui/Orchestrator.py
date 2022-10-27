from tkinter import messagebox
from reco_vocal import Reco_vocal
from ExtractLocation import ExtractLocation
from Search_path import Search_path
from tabulate import tabulate
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter
import customtkinter
import pandas as pd
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class Orchestrator(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.rc = Reco_vocal()
        self.el = ExtractLocation()
        self.sp = Search_path()

    def on_closing(self, event=0):
        self.destroy()

    def load_image(self, path, image_size):
        """ Load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def show_error(self):
        self.circleDeparture.after(0, self.circleDeparture.grid_forget)
        self.circleDestination.after(0, self.circleDestination.grid_forget)
        self.labelDuration.after(0, self.labelDuration.grid_forget)
        self.labelNumberStations.after(0, self.labelNumberStations.grid_forget)
        self.line.after(0, self.line.grid_forget)
        self.labelWaiting.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="ew")
        self.labelWaiting.configure(text="Aucun trajet n'est disponible, veuillez reformuler votre demande.")

    def search_shortest_path_by_vocal(self):
        request = self.rc.command()

        if request != None:
            locations = self.el.extract_location(request)

            if locations != None:
                path = self.sp.search_shortest_path(locations[0], locations[1])

                if path.empty:
                    self.rc.readText("Aucun trajet n'est disponible, veuillez reformuler votre demande.")
                else:
                    print(tabulate(path, headers = 'keys', tablefmt = 'psql'))
                    
                    messagebox.showinfo("Trajet le plus court",tabulate(path, headers = 'keys', tablefmt = 'psql'))
            else:
                self.rc.readText("Je ne peux pas répondre à votre demande. Je suis un assitant de voyage.")
        else:
            self.rc.readText("Je n'ai pas compris votre demande.")

    def search_shortest_path_by_text(self):
        departure = self.entryDeparture.get()
        destination = self.entryDestination.get()

        if not departure.strip() or not destination.strip():
            self.show_error()
        else:
            path = self.sp.search_shortest_path(departure, destination)

            if path.empty:
                self.show_error()
            else:
                self.labelWaiting.after(0, self.labelWaiting.grid_forget)

                print(path["Trajet"][0])
                stations = path["Trajet"][0]
                array_stations = stations.split(", ")
                print(array_stations)

                self.circleDeparture.configure(text=departure)
                self.circleDestination.configure(text=destination)
                self.labelDuration.configure(text="Duration: 150min")
                self.labelNumberStations.configure(text="Number of stations: 4")

                self.circleDeparture.grid(row=0, column=1, pady=(20, 0), padx=(0, 0), sticky="nw")
                self.circleDestination.grid(row=3, column=1, pady=(0, 20), padx=(0, 10), sticky="sw")
                self.line.grid(row=0, column=1, rowspan=4, padx=(8, 0), pady=(28, 28), ipadx=2, sticky="nsw")
                self.labelDuration.grid(row=1, column=2, pady=20, padx=20, sticky="ns")
                self.labelNumberStations.grid(row=2, column=2, pady=20, padx=20, sticky="ns")

    # def search_all_path(self):
    #     request = self.rc.command()
    #
    #     if request != None:
    #         locations = self.el.extract_location(request)
    #
    #         if locations != None:
    #             path = self.sp.search_all_path(locations[0], locations[1])
    #
    #             if path.empty:
    #                 self.rc.readText("Aucun trajet n'est disponible, veuillez reformuler votre demande.")
    #             else:
    #                 print(tabulate(path, headers = 'keys', tablefmt = 'psql'))
    #
    #                 messagebox.showinfo("Trajet le plus court",tabulate(path, headers = 'keys', tablefmt = 'psql'))
    #         else:
    #             self.rc.readText("Je ne peux pas répondre à votre demande. Je suis un assitant de voyage.")
    #     else:
    #         self.rc.readText("Je n'ai pas compris votre demande.")
                

    def orchestrator(self):

        self.title("Travel Order Resolved")
        self.geometry(f"{Orchestrator.WIDTH}x{Orchestrator.HEIGHT}")
        self.minsize(Orchestrator.WIDTH, Orchestrator.HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.styl = ttk.Style()
        self.styl.configure('TSeparator', background='purple')

        # ========== Create Frame Layout ==========
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_rowconfigure(2, weight=1)

        # Create frame Search
        self.frameSearch = customtkinter.CTkFrame(master=self)
        self.frameSearch.grid(row=1, column=0, sticky="nswe", padx=20, pady=(20, 10))

        self.frameSearch.rowconfigure(1, weight=0)
        self.frameSearch.columnconfigure((0, 1), weight=1)
        self.frameSearch.columnconfigure((2, 3), weight=0)

        # Create frame result
        self.frameResult = customtkinter.CTkFrame(master=self)
        self.frameResult.grid(row=2, column=0, sticky="nswe", padx=20, pady=(10, 20))

        self.frameResult.rowconfigure((0, 3), weight=2)
        self.frameResult.rowconfigure((1, 2), weight=1)
        self.frameResult.columnconfigure(0, weight=1)
        self.frameResult.columnconfigure(1, weight=1)
        self.frameResult.columnconfigure(2, weight=2)

        # ========== Load images and icons ==========

        self.vocal_image = self.load_image("/icons/mic_icon_48x48.png", 20)
        self.search_image = self.load_image("/icons/icon_search_48x48.png", 20)

        # ========== Create Title of Application ==========

        title = tkinter.StringVar(value="Travel Order Resolved")

        self.labelTitle = customtkinter.CTkLabel(master=self,
                                                 textvariable=title,
                                                 text_font=("Roboto Medium", -16),
                                                 text_color="white")
        self.labelTitle.grid(row=0, column=0, sticky="we", pady=(20, 0))

        # ========== Create Departure and Destination ==========

        self.labelDeparture = customtkinter.CTkLabel(master=self.frameSearch,
                                                     text="Departure")
        self.labelDeparture.grid(row=0, column=0, sticky="we", pady=(10, 10), padx=0)

        self.labelDestination = customtkinter.CTkLabel(master=self.frameSearch,
                                                       text="Destination")
        self.labelDestination.grid(row=0, column=1, sticky="we", pady=(10, 10), padx=0)

        self.entryDeparture = customtkinter.CTkEntry(master=self.frameSearch,
                                                     placeholder_text="Nantes")
        self.entryDeparture.grid(row=1, column=0, columnspan=1, pady=(0, 20), padx=20, sticky="ew")

        self.entryDestination = customtkinter.CTkEntry(master=self.frameSearch,
                                                       placeholder_text="Paris")
        self.entryDestination.grid(row=1, column=1, columnspan=1, pady=(0, 20), padx=20, sticky="ew")

        self.buttonVocal = customtkinter.CTkButton(master=self.frameSearch,
                                                   image=self.vocal_image,
                                                   text="",
                                                   width=100,
                                                   fg_color="green")
        self.buttonVocal.grid(row=1, column=2, columnspan=1, pady=(0, 20), padx=10, sticky="ew")

        self.buttonSearch = customtkinter.CTkButton(master=self.frameSearch,
                                                    image=self.search_image,
                                                    text="",
                                                    width=100,
                                                    fg_color="green",
                                                    command=self.search_shortest_path_by_text)
        self.buttonSearch.grid(row=1, column=3, columnspan=1, pady=(0, 20), padx=(10, 20), sticky="ew")

        # ========== Error and Waiting modules ==========
        self.labelWaiting = customtkinter.CTkLabel(master=self.frameResult,
                                                    text="Search departure and destination to see the shortest path!",
                                                   text_font=("Roboto Medium", -20),
                                                   text_color="white")
        self.labelWaiting.grid(row=0, column=0, rowspan=4, columnspan=3, sticky="ew")

        # ========== Create visualization route  ==========

        # Create line separator for visualization
        self.line = ttk.Separator(master=self.frameResult,
                                  orient=tkinter.VERTICAL,
                                  style="TSeparator",
                                  class_=ttk.Separator
                                  )

        # Create the circle of departure with name of station
        self.circleDeparture = customtkinter.CTkRadioButton(master=self.frameResult,
                                                            text="",
                                                            border_color="purple",
                                                            text_color_disabled="white",
                                                            state=tkinter.DISABLED)

        # Create the circle of destination with name of station
        self.circleDestination = customtkinter.CTkRadioButton(master=self.frameResult,
                                                              text="",
                                                              border_color="purple",
                                                              text_color_disabled="white",
                                                              state=tkinter.DISABLED)

        # ========== Create informations route  ==========

        self.labelDuration = customtkinter.CTkLabel(master=self.frameResult,
                                                    text="Duration: ",
                                                    text_font=("Roboto Medium", -16))

        self.labelNumberStations = customtkinter.CTkLabel(master=self.frameResult,
                                                          text="Number of stations: ",
                                                          text_font=("Roboto Medium", -16))

        self.mainloop()
