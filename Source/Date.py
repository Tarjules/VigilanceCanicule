class Date:
    @staticmethod
    def valid(year: int, month: int, day: int):
        """Vérifie que la date saisie existe.

        Args:
            year(int): Année
            mont(int): Mois
            day(int): Jour
        Returns:
            bool: True si la date existe, false sinon
        """
        if day <= 0:
            return False
        if month <= 12 and month >= 1:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day <= 31:
                    return True
                else:
                    return False
            if month in [4, 6, 9, 11]:
                if day <= 30:
                    return True
                else:
                    return False
            else:
                if year % 4 == 0 or year % 400 == 0:
                    if day <= 29:
                        return True
                    else:
                        return False
                else:
                    if day <= 28:
                        return True
                    else:
                        return False
        else:
            return False

    @staticmethod
    def from_int_to_string_slash(year: int, month: int, day: int):
        """Permet de convertir une date faite d'entier en une chaine de
        caractère sous le format year/month/day

        Args:
            year(int): Année
            mont(int): Mois
            day(int): Jour
        Returns:
            date(str): "year/month/day"
        """
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)
        date = str(year) + "/" + month + "/" + day
        return date

    @staticmethod
    def from_int_to_string_underscore(year: int, month: int, day: int):
        """Permet de convertir une date faite d'entier en une chaine de
        caractère sous le format year_month_day

        Args:
            year(int): Année
            mont(int): Mois
            day(int): Jour
        Returns:
            date(str): "year_month_day"
        """
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)
        date = str(year) + "_" + month + "_" + day
        return date
