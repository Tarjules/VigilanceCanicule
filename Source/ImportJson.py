import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Source.Date import Date

BASE = "https://files.data.gouv.fr/"


class ImportJsonTexteVigilanceMeteoFrance:
    @staticmethod
    def construct_url(year: int, month: int, day: int):
        """ Permet de construire l'URL poitant vers le fichier json contenant
        les textes de vigilances à 6h à la date fournie. Ce code dépend de
        la structure de la base de données proposée par Météo France.

        Args:
            year(int): année
            month(int): mois
            day(int): jour
        Returns:
            link(str) : lien vers le json contenant les informations
            recherchées
                """

        # A partir des entiers fournis, il faut reconstituer une date
        date = Date.from_int_to_string_slash(year, month, day)
        url_page_html = BASE + "meteofrance/data/vigilance/metropole/"
        url_page_html += date + "/"

        # Au vue de la structure des archives de Météo France (1er numéro
        # de dossier variant pour chaque date),
        # Il faut passer par la structure HTML de deux pages pour obtenir
        # le lien vers le json intéréssant

        html_content = requests.get(url_page_html).text
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find("title")
        if "No Files Available for Listing" == title.text:
            raise FileExistsError
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')
        link = urljoin(BASE, links[1].get('href'))

        html_content = requests.get(link).text
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')
        try:
            i = 0
            presence_cdp_texte_vigilance = False
            while i < len(links):
                href = links[i].get('href')
                if "CDP_TEXTES_VIGILANCE" in href:
                    link_json = href
                    i = len(links)
                    presence_cdp_texte_vigilance = True
                i = i+1
            if not presence_cdp_texte_vigilance:
                raise FileNotFoundError
        except FileNotFoundError:
            print("Il n'y a pas de fichier CDP_TEXTE_Vigilance.json" +
                  "pour la date du " + date)
            return None
        else:
            link = urljoin(BASE, link_json)
            return link

    @staticmethod
    def download_day(url, path: str):
        """Sauvegarde le fichier json pointé par l'URL dans le
        dossier 'loc' sous le nom 'name'

        Args:
            URL(str): URL poitant vers le json
            path(str): chemin relatif où enregistrer le json
            """
        try:
            if url is None:
                raise FileNotFoundError
        except FileNotFoundError:
            print("URL vide")
            pass
        else:
            response = requests.get(url)
            response_json = response.json()
            with open(path, 'w', encoding='utf-8') as fichier:
                json.dump(response_json, fichier, indent=4, ensure_ascii=False)

    @staticmethod
    def construct_path_json(loc: str, name: str):
        '''
        Args:
            loc(str): Dossier
            name(str): Nom du fichier

        Returns:
            "loc/name.json"'''
        return loc + "/" + name + ".json"

    @staticmethod
    def download_month(year: int, month: int):
        '''Permet de télécharger tout un mois de donnée de
        vigilance jour par jour si elles existent. Les fichiers sont
        enregistrés dans un dossier "year" sous le format Année_mois_jour.json
        Attention :  programme lent

        Args:
            year(int): Année concernée
            month(int): mois concerné
        '''
        i = 1
        while i <= 31:
            name = Date.from_int_to_string_underscore(year, month, i)
            path = ImportJsonTexteVigilanceMeteoFrance.construct_path_json(
                "data/" + str(year), name)
            try:
                url = ImportJsonTexteVigilanceMeteoFrance.construct_url(year,
                                                                        month,
                                                                        i)
                ImportJsonTexteVigilanceMeteoFrance.download_day(url, path)
            except FileExistsError:
                i = 32
                print("il n'y a plus de données pour ce mois")
            i += 1

    @staticmethod
    def download_year(year: int):
        '''Permet de télécharger toute une année de donnée de vigilance jour
        par jour si elles existent. Les fichiers sont enregistrés dans un
        dossier "year" sous le format Année_mois_jour.json
        Peut-être utilisé même si l'année est incomplète.
        Attention :  programme lent

        Args:
            year(int): Année concernée
        '''
        try:
            if year < 2022 or year > 2026:
                raise IndexError
        except IndexError:
            print(f"l'année {year} est indisponible")
            pass
        else:
            m = 1
            while m <= 12:
                ImportJsonTexteVigilanceMeteoFrance.download_month(year, m)
                m += 1
