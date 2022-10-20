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

    def search_shortest_path(self):
        request = self.rc.command()

        if request != None:
            locations = self.el.extract_location(request)

            if locations != None:
                path = self.sp.search_shortest_path(locations[0], locations[1])

                if path.empty:
                    self.rc.readText("Aucun trajet n'est disponible, veuillez reformuler votre demande.")
                else:
                    fenetre = Tk()
                    fenetre.title('Result')
                    l = LabelFrame(fenetre, text="Trajet de "+locations[0]+" à "+locations[1], padx=20, pady=20)
                    l.pack(fill="both", expand="yes")
                    paths = path["Trajet"][0].split('\n')
                    for i in paths:
                        label = Label(l, text=i)
                        label.pack()
                    fenetre.mainloop()
            else:
                self.rc.readText("Je ne peux pas répondre à votre demande. Je suis un assitant de voyage.")
        else:
            self.rc.readText("Je n'ai pas compris votre demande.")

    def search_all_path(self):
        request = self.rc.command()

        if request != None:
            locations = self.el.extract_location(request)

            if locations != None:
                path = self.sp.search_all_path(locations[0], locations[1])

                if path.empty:
                    self.rc.readText("Aucun trajet n'est disponible, veuillez reformuler votre demande.")
                else:

                    messagebox.showinfo("Trajet le plus court",tabulate(path, headers = 'keys', tablefmt = 'psql'))
            else:
                self.rc.readText("Je ne peux pas répondre à votre demande. Je suis un assitant de voyage.")
        else:
            self.rc.readText("Je n'ai pas compris votre demande.")
                

    def orchestrator(self):
        fenetre = Tk()
        fenetre.title('Travel Order Resolver')
        photo = PhotoImage(file="image/chargement.png")
        canvas = Canvas(fenetre,width=640, height=380)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack()

        Sp = Button(fenetre, text ="Search Shortest Path", command = self.search_shortest_path)
        Sp.pack()
        Ap = Button(fenetre, text ="Search All Path", command = self.search_all_path)
        Ap.pack()
        
        canvas.mainloop()