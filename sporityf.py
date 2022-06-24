from attr import s
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome_options = webdriver.ChromeOptions()                        #Driver ayarları
chrome_options.add_argument("--incognito")
s = Service("chromedriver.exe")

""""
input = open("Dinleyiciler.txt","r")           # Kişileri kaydettik
girisbilgileri=[]                              # eğer birden fazla hesap ile yapılacak ise
for x in input:                                # for döngüsü kullanılarak bu bilgiler alınır.
    girisbilgileri.append(x)
"""

a = "birisi@outlook.com"
b = "birisi123"

def Giris(eposta,password):
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)                             #Driver kurduk
    driver.get("https://accounts.spotify.com/tr/login?continue=https%3A%2F%2Fopen.spotify.com%2F")  #Login sayfasını açtık  
     
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/input").send_keys(eposta)  #Eposta girildi
    time.sleep(1)
    
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/input").send_keys(password) #Password girildi
    time.sleep(1)
    
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/button").click()  #Login butonu
    time.sleep(1)
    
    driver.get("https://open.spotify.com/artist/3P25KHpw54IBgPlI7JQC5L")   #Açılacak şarkı linki
    time.sleep(1)
    
    #Şarkı başlatıldı
    for i in range(2):
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[3]/div[1]/div/div[1]/div/div/div[2]/div[1]").click()
    time.sleep(1)
    
    #Şarkı döngüye alındı
    for i in range(2):
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]").click()
    time.sleep(1)
    
    
c = Giris(a,b)
    


