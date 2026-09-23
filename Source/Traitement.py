# Pour l'instant, on va travailler uniquement avec Carte 
# dans la mesure où c'est dans ce registre que les 
# informations sont les plus complètes.

from Source.ExtractDataCarte import ExtractDataCarte as Extract


class Traitement:
    def __init__(self):
        pass
    
    def nb_day_heatwave(self, year: list):
        """Compte le nombre de jour en vigilance canicule jaune, 
        orange et rouge.
        
        Args: 
            year(list) : la liste des jour avec une vigilance canicule
            au format [[date, vigilance, niveau], ...]]
        Returns:
            (list) :  [[jaune, X], [orange, Y], [rouge, Z]]"""
        x = 0
        y = 0
        z = 0
        for day in year:
            if day[2] == 2:
                x += 1
            if day[2] == 3:
                y += 1
            if day[2] == 4:
                z += 1
        return [["jaune", x], ["orange", y], ["rouge", z]]

    def dept_heatwaves_per_year(self, dept):
        """Fournit dans une liste, le nombre de jours de vigilance canicule 
        (selon le niveau d'alerte) pour un département et chaque année de
        2023 à 2026

        Args:
            dept(str or int) : département d'intéret
        Returns:
            (list) : [[2023, nb_day_heatwave(2023)] ...]"""
        dept_heatwaves = []
        extracter = Extract()
        for y in range(2023, 2027):
            year = extracter.data_year_and_departement(y, dept)
            dept_heatwaves.append([y, self.nb_day_heatwave(year)])
        return dept_heatwaves
