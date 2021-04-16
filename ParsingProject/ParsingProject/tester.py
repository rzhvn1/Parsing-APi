import re

from bs4 import BeautifulSoup
import requests as req

with open('index.html', 'r') as f:

    contents =  f.read()

    soap = BeautifulSoup(contents, 'lxml')

    strings =  soap.find_all(string=re.compile('BSD'))

    for txt in strings:

        print(" ".join(txt.split()))




