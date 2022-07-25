import csv
import pandas as pd

def main():
    with open ("D:\Intern\project\data_scraping\demo_files\appstore_demo.csv", 'r', encoding = 'utf-8') as file:
        data  = list(csv.reader(file))
        for d in data:
            CC = d.find('Creative Cast') 
            CV = d.find('Collavision')
            one = d.find('OneLink')
            
            

