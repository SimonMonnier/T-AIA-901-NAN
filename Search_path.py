import pandas as pd
import networkx as nx


class Search_path:
    def __init__(self):
        i = 0
        self.dfTimeTables = pd.read_csv("data_sncf/timetables.csv", sep="\t")
        self.Graphe = nx.MultiGraph()
        while i < len(self.dfTimeTables):
            nodes_a = self.dfTimeTables["trajet"][i].split(" - ")
            j = 0
            while j < len(self.dfTimeTables):

                nodes_b = self.dfTimeTables["trajet"][j].split(" - ")
                if nodes_a[0] == nodes_b[0]:
                    time = self.dfTimeTables["duree"][j]
                    self.Graphe.add_edge(nodes_a[0], nodes_b[1], poids=time)
                if nodes_a[0] == nodes_b[1]:
                    time = self.dfTimeTables["duree"][j]
                    self.Graphe.add_edge(nodes_a[0], nodes_b[0], poids=time)
                j += 1
            i += 1

    def search_path(self, src, dest):
        i = 0
        j = 0
        src_tmp = src
        dest_tmp = dest

        while i < len(self.dfTimeTables):
            nodes = self.dfTimeTables["trajet"][i].split(" - ")
            if src.lower() in nodes[0].lower():
                src = nodes[0]
                break
            if src.lower() in nodes[1].lower():
                src = nodes[1]
                break
            i += 1
            
        while j < len(self.dfTimeTables):
            nodes = self.dfTimeTables["trajet"][j].split(" - ")
            if dest.lower() in nodes[0].lower():
                dest = nodes[0]
                break
            if dest.lower() in nodes[1].lower():
                dest = nodes[1]
                break
            j += 1
        if src_tmp != src and dest_tmp != dest:
            return nx.dijkstra_path(self.Graphe, source=src, target=dest, weight='weight')
        else:
            return None