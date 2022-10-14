from Reco_vocal import Reco_vocal
from ExtractLocation import ExtractLocation
from Search_path import Search_path


if __name__ == "__main__":
    rc = Reco_vocal()
    el = ExtractLocation()
    sp = Search_path()

    while True:
        request = rc.command()

        if request != None:
            locations = el.extract_location(request)

            if locations != None:
                path = sp.search_path(locations[0], locations[1])

                if path != None:
                    print(path)
                    break
            