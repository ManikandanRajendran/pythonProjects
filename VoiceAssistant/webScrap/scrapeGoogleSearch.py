import random
import requests
import pprint
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q={}&hl=en'

A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 "
     "Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
     )
Agent = A[random.randrange(len(A))]
headers = {'user-agent': Agent}


def scrape_google_result(query):
    try:
        response = requests.get(url.format(query.replace(" ", "+")), headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.select('div.BNeawe')
        for i in range(len(divs)):
            if divs[i].span:
                divs[i].span.decompose()
                result = divs[i].getText()
                if len(result) > 20:
                    result = result.rsplit('.', 1)[0]
                    return result
    except Exception as ex:
        return "sorry no details available"


def scrape_google_links(query):
    try:
        response = requests.get(url.format(query.replace(" ", "+")), headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.select('a')
        myList = ['w3schools.com', 'programiz.com', 'tutorialspoint.com', 'geeksforgeeks.org']
        newList = []
        for i in range(len(divs)):
            link = divs[i].get('href')
            if any(x in link for x in myList):
                link = (link.split("=")[1])
                remove = link.split('/')[2]
                if not any(remove in x for x in newList):
                    newList.append(link)
            elif len(newList) < 5 and not 'maps' in link and ('wikipedia' in link or 'quora' in link or 'https://' in link):
                link = (link.split("=")[1]).split('&')[0]
                newList.append(link)

        return newList
    except Exception as ex:
        return "sorry no links available"
    # result = divs[0].getText()


if __name__ == "__main__":
    qstn = 'how to gain wait?'
    pprint.pprint(scrape_google_result(qstn))
    scrape_google_links(qstn)
