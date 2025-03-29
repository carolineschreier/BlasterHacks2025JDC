# Original article for original chatbot: https://handsonai.medium.com/developing-a-simple-chatbot-with-python-and-tensorflow-a-step-by-step-tutorial-0d35767e113b
# Helpful stack overflow post for fixing error from article: https://stackoverflow.com/questions/78089650/tensorflow-keras-error-attributeerror-tuple-object-has-no-attribute-lower

# import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, LSTM, Dense

# # Prepare the conversation data - make sure inputs and responses lists are same size
# inputs = [
#     "Hello, how are you",
#     "What's your name",
#     "I'm feeling happy today",
#     "Do you like dogs",
#     "I have a pet cat",
#     "What's your favorite food",
#     "I love eating pizza",
#     "Do you like watching movies",
#     "My favorite movie is Titanic",
#     "I'm going to the beach tomorrow",
#     "Do you like swimming",
#     "I'm learning how to play guitar",
#     "What's your favorite music genre",
#     "I love listening to pop music",
#     "Do you have any siblings",
#     "I have an older brother",
#     "What do you like to do on weekends",
#     "I like to play video games",
#     "Do you have a favorite sports team",
#     "I support the New York Yankees",
#     "I'm feeling sad today",
#     "Do you like reading books",
#     "My favorite book is Harry Potter",
#     "I'm going to a concert tonight",
#     "Do you like attending concerts",
#     "I love eating ice cream",
#     "What's your favorite ice cream flavor",
#     "I have a pet dog",
#     "Do you like going to the gym",
#     "I'm trying to learn a new language",
#     "What's your favorite type of music",
#     "I love watching TV shows",
#     "Do you like playing board games",
#     "I have a big family",
#     "I'm going to a wedding next week",
#     "Do you like traveling",
#     "I love eating sushi",
#     "I'm feeling bored today",
#     "Do you like playing chess",
#     "I have a favorite restaurant",
#     "I'm going to a party tonight",
#     "Do you like making new friends",
#     "I love eating breakfast food",
#     "I have a pet bird",
#     "Do you like going to the park",
#     "I'm trying to learn how to cook",
#     "What's your favorite type of cuisine",
#     "I love watching sports games",
#     "I have a big house",
#     "I'm feeling excited today",
#     "Do you like attending festivals",
#     "I love eating cupcakes",
#     "I have a pet fish",
#     "Do you like playing video games",
#     "I'm going to a museum tomorrow"
# ]

# responses = [
#     "I'm doing great, thanks for asking",
#     "My name is Chatbot",
#     "That's awesome, what's making you happy",
#     "Yes, I love dogs, they're so cute",
#     "That's cool, I've never had a pet cat",
#     "I'm just a chatbot, I don't have personal preferences",
#     "Pizza is delicious, what's your favorite topping",
#     "Yes, I love watching movies, what's your favorite genre",
#     "Titanic is a classic, I've seen it many times",
#     "That sounds like fun, be careful at the beach",
#     "Yes, I love swimming, it's great exercise",
#     "That's awesome, playing guitar is a great hobby",
#     "I'm just a chatbot, I don't have personal preferences",
#     "Pop music is catchy, I love listening to it",
#     "Yes, I have many users who talk to me",
#     "That's cool, what's your brother like",
#     "I'm always available to chat, 24/7",
#     "Video games are fun, what's your favorite game",
#     "I'm just a chatbot, I don't have personal preferences",
#     "The New York Yankees are a great team",
#     "Sorry to hear that, what's wrong",
#     "Yes, I love reading books, what's your favorite author",
#     "Harry Potter is a great series, I've read all the books",
#     "That sounds like fun, who's the concert for",
#     "Yes, I love attending concerts, they're so much fun",
#     "Ice cream is delicious, what's your favorite flavor",
#     "Chocolate is a great choice, I love chocolate ice cream",
#     "That's awesome, what's your dog's name",
#     "Yes, exercising is important, I'm glad you're going to the gym",
#     "Learning a new language is difficult, but rewarding",
#     "I'm just a chatbot, I don't have personal preferences",
#     "TV shows are great, what's your favorite show",
#     "Yes, I love playing board games, they're so much fun",
#     "That's cool, what's it like having a big family",
#     "Weddings are fun, I'm sure you'll have a great time",
#     "Yes, traveling is great, where have you been",
#     "Sushi is delicious, what's your favorite type of sushi",
#     "Sorry to hear that, what's on your mind",
#     "Yes, I love playing chess, it's a great game",
#     "That's awesome, what's your favorite restaurant",
#     "Parties are fun, I'm sure you'll have a great time",
#     "Yes, making new friends is great, I'm glad you're meeting new people",
#     "Breakfast food is delicious, what's your favorite breakfast dish",
#     "That's cool, what's your bird's name",
#     "Yes, I love going to the park, it's so much fun",
#     "Cooking is a great skill, what's your favorite dish to make",
#     "I'm just a chatbot, I don't have personal preferences",
#     "Sports games are exciting, what's your favorite sport",
#     "That's awesome, what's your house like",
#     "That's great, what's making you excited",
#     "Yes, attending festivals is fun, what's your favorite festival",
#     "Cupcakes are delicious, what's your favorite flavor",
#     "That's cool, what's your fish's name",
#     "Yes, I love playing video games, they're so much fun",
#     "Museums are great, what's your favorite exhibit"
# ]

# # Initialize and fit the tokenizer on the input texts
# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(inputs + responses)  # Fit on both inputs and responses

# # Define vocabulary size
# vocab_size = len(tokenizer.word_index) + 1

# # Convert texts to sequences
# input_sequences = tokenizer.texts_to_sequences(inputs)
# response_sequences = tokenizer.texts_to_sequences(responses)

# # Determine the maximum sequence length
# max_sequence_len = max(max(len(seq) for seq in input_sequences),
#                     max(len(seq) for seq in response_sequences))

# # Pad sequences
# X = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='post')
# y = pad_sequences(response_sequences, maxlen=max_sequence_len, padding='post')

# # Define the model
# model = Sequential([
#     Embedding(vocab_size, 64, input_length=max_sequence_len, mask_zero=True),
#     LSTM(100, return_sequences=True),
#     Dense(vocab_size, activation='softmax')
# ])

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# # Fit the model
# model.fit(X, y, epochs=50, verbose=1)

# def generate_response(input_text):
#     input_seq = tokenizer.texts_to_sequences([input_text])
#     padded_input = pad_sequences(input_seq, maxlen=max_sequence_len, padding='post')
#     predicted_output = model.predict(padded_input)
#     predicted_word_index = tf.argmax(predicted_output, axis=-1).numpy()[0]
#     response = tokenizer.sequences_to_texts([predicted_word_index])
#     return response[0]  

# # Interaction loop
# while True:
#     user_input = input(">>> ")
#     response = generate_response(user_input)
#     print(f"Chatbot: {response}")

import random
import json
import pickle
import numpy as np
import nltk

from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
from keras.layers import Dense,Activation,Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open("intense.json").read())

words = []
classes = []
documents = []
ignore_letters = ["?", "!", ".", ","]
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        
        documents.append(((word_list), intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))



training = []
output_empty = [0]*len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training, dtype='object')

train_x = list(training[:,0])
train_y = list(training[:,1])


model = Sequential([
    Dense(128, input_shape=(len(train_x[0]),),activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(train_y[0]), activation='softmax')
])

sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(
    loss='categorical_crossentropy',
    optimizer=sgd,
    metrics=['accuracy']
)
hist = model.fit(
    np.array(train_x),
    np.array(train_y),
    epochs=250,
    batch_size=5,
    verbose=1
)

model.save("blasterbot.h5", hist)
