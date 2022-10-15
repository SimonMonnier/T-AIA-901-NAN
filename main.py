from Reco_vocal import Reco_vocal
from ExtractLocation import ExtractLocation
from Search_path import Search_path
from tabulate import tabulate


if __name__ == "__main__":
    rc = Reco_vocal()
    el = ExtractLocation()
    sp = Search_path()

    while True:
        request = rc.command()

        if request != None:
            locations = el.extract_location(request)
            print(locations)
            if locations != None:
                path = sp.search_path(locations[0], locations[1])

                if path.empty:
                    rc.readText("Aucun trajet n'est disponible, veuillez reformuler votre demande.")
                else:
                    print(tabulate(path, headers = 'keys', tablefmt = 'psql'))
                    # break
            else:
                rc.readText("Je ne peux pas répondre à votre demande. Je suis un assitant de voyage.")
            