import json
import random
import requests
import pyttsx3


# jokeUrl = 'https://icanhazdadjoke.com/', https://official-joke-api.appspot.com/jokes/programming/random https://sv443.net/jokeapi/v2/joke/Programming?type=twopart
# quote apis - https://api.quotable.io/random


def quote_url1():
    url = "https://api.quotable.io/random"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    quote = response['content'] + " - " + response["author"]
    return quote


def local_quote():
    print("from local")
    with open('database/my_quotes.json') as fp:
        data = json.load(fp)
        random_index = random.randint(0, len(data) - 1)
        value1 = data[random_index]['text']
        value2 = data[random_index]['author']
        return f'{value1} - {value2}'


def joke_url1():
    url = "https://icanhazdadjoke.com/"
    headers = {'Accept': 'application/json'}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    return response['joke']


def joke_url2():
    url = "https://sv443.net/jokeapi/v2/joke/Programming"
    headers = {'Accept': 'application/json'}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    if response['type'] == "twopart":
        value1 = response['setup']
        value2 = response['delivery']
        return f'{value1}, \n {value2}'
    else:
        return response['joke']


def joke_url3():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    headers = {'Accept': 'application/json'}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    value1 = response[0]['setup']
    value2 = response[0]['punchline']
    return f'{value1}, \n {value2}'


def synonyms(value):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{value}"
    headers = {'Accept': 'application/json'}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)
    value = {}
    definition, example, synonyms = '', '', ''
    try:
        definition = response[0]['meanings'][0]['definitions'][0]['definition']
        try:
            example = response[0]['meanings'][0]['definitions'][0]['example']
        except:
            example = "No Example available"
        try:
            synonyms = response[0]['meanings'][0]['definitions'][0]['synonyms']
            if len(synonyms) > 5:
                synonyms = synonyms[:6]
            elif len(synonyms) == 0:
                synonyms = "no synonym found"
        except:
            try:
                synonyms = response[0]['meanings'][1]['definitions'][0]['synonyms']
                if len(synonyms) > 5:
                    synonyms = synonyms[:6]
                elif len(synonyms) == 0:
                    synonyms = "no synonym found"
            except:
                synonyms = "no synonym found"
    except:
        definition = response['title']
        example = response['message']
        synonyms = response['resolution']
    value.update({"definition": definition, "example": example, "synonyms": synonyms})
    # return f'{value1}, \n {value2}'
    return value


def getJoke():
    my_list = [joke_url1, joke_url2, joke_url3]
    return random.choice(my_list)()


def getQuote():
    my_list = [quote_url1, local_quote]
    return random.choice(my_list)()
