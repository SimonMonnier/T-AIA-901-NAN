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
        src_tab = []
        dest_tab = []

        while i < len(self.dfTimeTables):
            nodes = self.dfTimeTables["trajet"][i].split(" - ")
            if src.lower() in nodes[0].lower():
                src_tab.append(nodes[0])
            if src.lower() in nodes[1].lower():
                src_tab.append(nodes[1])
            if dest.lower() in nodes[0].lower():
                dest_tab.append(nodes[0])
            if dest.lower() in nodes[1].lower():
                dest_tab.append(nodes[1])
            i += 1
            
        src_tab = list(set(src_tab))
        dest_tab = list(set(dest_tab))
        if src_tab != [] and dest_tab != []:
            k = 0
            l = 0
            m = 1
            df = pd.DataFrame(columns=['id','Trajet'])

            while k < len(src_tab):
                while l < len(dest_tab):
                    trajet = nx.dijkstra_path(self.Graphe, source=src_tab[k], target=dest_tab[l], weight='weight')
                    new_row = {'id': f"{m}",'Trajet': f"{trajet}" }
                    df_tmp = pd.DataFrame(new_row, index=[0])
                    df = pd.concat([df, df_tmp])
                    l += 1
                    m += 1
                k += 1
                m += 1
            k = 0
            l = 0
            while k < len(dest_tab):
                while l < len(src_tab):
                    trajet = nx.dijkstra_path(self.Graphe, source=src_tab[l], target=dest_tab[k], weight='weight')
                    new_row = {'id': f"{m}",'Trajet': f"{trajet}" }
                    df_tmp = pd.DataFrame(new_row, index=[0])
                    df = pd.concat([df, df_tmp])
                    l += 1
                    m += 1
                k += 1
                m += 1
            df = df.drop_duplicates(subset ="Trajet", keep = 'first')
            return df
        else:
            
            return pd.DataFrame(columns=['id','Trajet'])