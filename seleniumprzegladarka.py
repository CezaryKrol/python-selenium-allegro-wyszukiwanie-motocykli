from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class Wyszukiwanie(object):
    def __init__(self, lokalizacja, max_cena):
        self.lokalizacja = lokalizacja
        self.max_cena = max_cena

        self.url=f"https://allegro.pl/kategoria/motocykle-i-quady-300685?price_to={max_cena}&bmatch=baseline-al-product-cl-eyesa2-engag-dict43-aut-1-3-0318&state={lokalizacja}"

        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
        self.delay = 5

    def allegro_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "main-wrapper"))) 
            print("Strona zaladowana")
        except TimeoutException:
            print("Przekroczono czas oczekiwania na zaladowanie strony")

    def tytuly_aukcji(self):
        self.driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div[2]/div/div[2]/button[2]').click()
        aukcje = self.driver.find_elements_by_class_name("_9c44d_3TzmE")
        lista_aukcji = []
        for lista in aukcje:
            print(lista.text)
            lista_aukcji.append(lista.text)
        return lista_aukcji

    def url_aukcji(self):
        lista_url = []
        html = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html, "lxml")
        for link in soup.findAll("a", {"class": "_9c44d_1MOYf"}):
            print(link["href"])
            lista_url.append(link["href"])
        return lista_url

    def zamknij(self):
        self.driver.close()

lokalizacja ="3" #3="z lubelskiego"
max_cena = "10000"

scraper = Wyszukiwanie(lokalizacja,max_cena)
scraper.allegro_url()
scraper.tytuly_aukcji()
scraper.url_aukcji()
scraper.zamknij()