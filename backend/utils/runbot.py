import random 
import json 
import pickle 
import numpy as np 
import nltk 
from keras.models import load_model 
from nltk.stem import WordNetLemmatizer 
from codecarbon import EmissionsTracker


lemmatizer = WordNetLemmatizer()

tracker = EmissionsTracker()

intents = json.loads(open('utils/intense.json').read())
words = pickle.load(open('utils/words.pkl', 'rb'))
classes = pickle.load(open('utils/classes.pkl', 'rb'))
model = load_model('utils/blasterbot.h5')

def clean_up_sentences(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bagw(sentence):
    sentence_words = clean_up_sentences(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow = bagw(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]],
                            'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def frontend_chat(message):
    tracker = EmissionsTracker(allow_multiple_runs = True)
    tracker.start()
    ints = predict_class(message)
    res = get_response(ints, intents)
    tracker.stop()
    emissions: float = tracker.stop()
    print(emissions)
    return res, emissions