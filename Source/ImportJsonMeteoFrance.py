import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Source.Date import Date
from abc import ABC

BASE = "https://files.data.gouv.fr/"


class ImportJsonMeteoFrance(ABC):

    def construct_url(self, filename: str, year: int, month: int, day: int):
        # A partir des entiers fournis, il faut reconstituer une date
        date = Date.from_int_to_string_slash(year, month, day)
        url_page_html = (BASE + "meteofrance/data/vigilance/metropole/" +
                         date + "/")

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
        j = 1
        presence_fichier = False
        while j < len(links):
            link = urljoin(BASE, links[j].get('href'))
            html_content = requests.get(link).text
            soup = BeautifulSoup(html_content, 'html.parser')
            linksjson = soup.find_all('a')
            i = 0
            while i < len(linksjson):
                href = linksjson[i].get('href')
                if filename in href:
                    link_json = href
                    i = len(linksjson)
                    j = len(links)
                    presence_fichier = True
                i = i+1
            j = j+1
        if not presence_fichier:
            print("Il n'y a pas de fichier " +
                  filename+".json pour la date du " + date)
            return None
        else:
            link = urljoin(BASE, link_json)
            return link

    def test_file_ever_exist(self, path: str):
        try:
            with open(path, "r"):
                return True
        except FileNotFoundError:
            return False
        except IOError:
            return False

    def download_day(self, url, path: str):
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
            pass
        else:
            e = self.test_file_ever_exist(path)
            if not e:
                response = requests.get(url)
                response_json = response.json()
                with open(path, 'w', encoding='utf-8') as fichier:
                    json.dump(response_json, fichier,
                              indent=4, ensure_ascii=False)
            else:
                pass

    def download_year(self, year: int):
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
                self.download_month(year, m)
                m += 1

    def download_month(self, year, month):
        '''Permet de télécharger tout un mois de donnée de
            vigilance jour par jour si elles existent. Les fichiers sont
            enregistrés dans un dossier "year" sous le
            format Année_mois_jour.json
            Attention :  programme lent

            Args:
                year(int): Année concernée
                month(int): mois concerné
            '''
        i = 1
        while i <= 31:
            name = Date.from_int_to_string_underscore(year, month, i)
            path = self.construct_path_json(year, name)
            try:
                url = self.construct_url(year, month, i)
                self.download_day(url, path)
            except FileExistsError:
                i = 32
                print("il n'y a plus de données pour ce mois")
            i += 1

    @staticmethod
    def construct_path_json(self, year: int, name: str):
        pass
