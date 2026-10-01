import matplotlib.pyplot as plt
import numpy as np
from Source.ExtractData import ExtractData as loadjson


class Graphique:
    def __init__(self):
        """Crée une instance de classe Graphique"""
        pass

    def from_number_to_name(self, dept):
        if type(dept) is int:
            if dept < 10:
                dept = "0" + str(dept)
            else:
                dept = str(dept)
        dict = loadjson.load_json("data/departements-region.json")
        for D in dict:
            if D["num_dep"] == dept:
                return D["dep_name"]

    def histogramme_dept_years(self, L_heatwaves: list):
        """Permet de générer un histogramme des jours
        en vigilance canicule jaune, orange et rouge, à partir de la liste fournie.

        Args:
            L_heatwaves(list) : [dept, [2023, [[level alerte, x], ...]], ...]"""
        dept = L_heatwaves[0]
        h2023 = L_heatwaves[1]
        h2024 = L_heatwaves[2]
        h2025 = L_heatwaves[3]
        h2026 = L_heatwaves[4]
        labels = [h2023[0], h2024[0], h2025[0], h2026[0]]
        jaune = [h2023[1][0][1], h2024[1][0][1], h2025[1][0][1], h2026[1][0][1]]
        orange = [h2023[1][1][1], h2024[1][1][1], h2025[1][1][1], h2026[1][1][1]]
        rouge = [h2023[1][2][1], h2024[1][2][1], h2025[1][2][1], h2026[1][2][1]]
        x = np.arange(len(labels))
        width = 0.25
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, jaune, width, label='Vigilance Jaune',
                        color="yellow")
        rects2 = ax.bar(x, orange, width, label='Vigilance Orange',
                        color="orange")
        rects3 = ax.bar(x + width, rouge, width, label="Vigilance Rouge",
                        color="red")
        ax.set_ylabel('nombre de jours', fontsize=17)
        ax.set_title("Evolution du nombre de jours en vigilance canicule " +
                     "dans le département '" + self.from_number_to_name(dept)+"'", fontsize=26)
        ax.set_xticks(x, labels, fontsize=17)
        ax.legend(fontsize=17, loc="upper left")

        ax.bar_label(rects1, padding=3, fontsize=15)
        ax.bar_label(rects2, padding=3, fontsize=15)
        ax.bar_label(rects3, padding=3, fontsize=15)

        fig.tight_layout()

        plt.show()
