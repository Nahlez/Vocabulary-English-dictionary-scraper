from selenium import webdriver
import csv, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# IDEA OF THE PROGRAM
# From my personal csv list of english word that i want to remember
# Search that in Cambridge and get the title, spanish translation, meaning and example. 
# Put that in differents csv fields


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=opts)

# URL BASE : https://dictionary.cambridge.org/dictionary/english-spanish/'Strings'

vocabulary_list = open('vocab.csv','r')

for word in vocabulary_list:
    try:
        driver.get('https://dictionary.cambridge.org/dictionary/english-spanish/'+word)
        time.sleep(1)
        spanish_word = driver.find_element_by_xpath("(//span[@class='trans dtrans dtrans-se '])[1]").text
        example_word = driver.find_element_by_xpath('(//span[@class="eg deg"])[1]').text
        meaning_word = driver.find_element_by_xpath('(//div[@class="def ddef_d db"])[1]').text
        word = word.replace('\n','')
        csv_anki = open('csv-vocab-anki.csv','a+')
        csv_anki.write(word+'('+spanish_word+')'+';'+word+';'+meaning_word+';'+ example_word+'\n')
        csv_anki.close()
        print(word+'('+spanish_word+')'+';'+word+';'+meaning_word+';'+ example_word+'\n')


    except Exception as e:
            print(e)
driver.quit()