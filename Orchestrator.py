from tkinter import messagebox
from Reco_vocal import Reco_vocal
from ExtractLocation import ExtractLocation
from Search_path import Search_path
from tabulate import tabulate
from tkinter import * 


class Orchestrator:
    def __init__(self):
        self.rc = Reco_vocal()
        self.el = ExtractLocation()
        self.sp = Search_path()

    def search(self):
        request = self.rc.command()

        if request != None:
            locations = self.el.extract_location(request)

            if locations != None:
                path = self.sp.search_path(locations[0], locations[1])

                if path.empty:
                    self.rc.readText("Aucun trajet n'est disponible, veuillez reformuler votre demande.")
                else:
                    print(tabulate(path, headers = 'keys', tablefmt = 'psql'))
                    
                    messagebox.showinfo("Trajet le plus court",tabulate(path, headers = 'keys', tablefmt = 'psql'))
            else:
                self.rc.readText("Je ne peux pas répondre à votre demande. Je suis un assitant de voyage.")
        else:
            self.rc.readText("Je n'ai pas compris votre demande.")
                

    def orchestrator(self):
        fenetre = Tk()
        photo = PhotoImage(file="image/chargement.png")
        canvas = Canvas(fenetre,width=640, height=380)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack()

        button = Button(fenetre, text ="Search", command = self.search)
        button.pack()
        
        canvas.mainloop()