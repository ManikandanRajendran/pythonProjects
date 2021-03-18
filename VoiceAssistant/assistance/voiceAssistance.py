import pprint
import speech_recognition as sr
import wikipedia
import pyttsx3
import sys
sys.path.insert(1, 'webScrap')
import scrapeGoogleSearch

engine = pyttsx3.init()
engine.setProperty('voice', 'english+f4') #_rp
engine.setProperty('rate', 107)  # Speed percent (can go over 100)
# engine.setProperty('volume', 0.5)  # Volume 0-1
query = 'nothing'
recognizer = sr.Recognizer()


def saySomething(text):
    engine.say(text)


def recordQuery():
    with sr.Microphone() as source:
        print('\n \n clearing background noise.. please wait! \n')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Shoot your question now! \n')
        record_audio = recognizer.listen(source)
        print("Done recording \n")
    try:
        text = recognizer.recognize_google(record_audio, language='en-US')
        print(f'Searching with your query : {text} \n')
        return text
    except Exception as ex:
        print(ex)
        return ""


def search_in_wiki(query):
    try:
        wiki_search = wikipedia.summary(query)
        return wiki_search
    except Exception as ex:
        print(ex)


def read_result(result):
    pprint.pprint(result)
    print('\n \n')
    saySomething(result)


def initiateProgram():
    try:
        query = recordQuery()
        if not query == "":
            result = scrapeGoogleSearch.scrape_google_result(query)
            read_result(result)
            links = scrapeGoogleSearch.scrape_google_links(query)
            if len(links) > 0:
                saySomething("please refer below links for more info \n")
                print('\n Below links will be helpful \n') 
                pprint.pprint(links)
        else:
            saySomething('Sorry, facing issue with listening you')        
        engine.runAndWait()
    except Exception as ex:
        print(ex)



if __name__ == '__main__':
    initiateProgram()

