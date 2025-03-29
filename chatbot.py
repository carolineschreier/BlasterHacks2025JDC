# Original article for original chatbot: https://handsonai.medium.com/developing-a-simple-chatbot-with-python-and-tensorflow-a-step-by-step-tutorial-0d35767e113b
# Helpful stack overflow post for fixing error from article: https://stackoverflow.com/questions/78089650/tensorflow-keras-error-attributeerror-tuple-object-has-no-attribute-lower

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Prepare the conversation data - make sure inputs and responses lists are same size
inputs = ["Hello", "How are you?", "What's your name?"]
responses = ["Hi there!", "I'm doing well, thanks.", "I'm a chatbot."]

# Initialize and fit the tokenizer on the input texts
tokenizer = Tokenizer()
tokenizer.fit_on_texts(inputs + responses)  # Fit on both inputs and responses

# Define vocabulary size
vocab_size = len(tokenizer.word_index) + 1

# Convert texts to sequences
input_sequences = tokenizer.texts_to_sequences(inputs)
response_sequences = tokenizer.texts_to_sequences(responses)

# Determine the maximum sequence length
max_sequence_len = max(max(len(seq) for seq in input_sequences),
                    max(len(seq) for seq in response_sequences))

# Pad sequences
X = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='post')
y = pad_sequences(response_sequences, maxlen=max_sequence_len, padding='post')

# Define the model
model = Sequential([
    Embedding(vocab_size, 64, input_length=max_sequence_len, mask_zero=True),
    LSTM(100, return_sequences=True),
    Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=50, verbose=1)

def generate_response(input_text):
    input_seq = tokenizer.texts_to_sequences([input_text])
    padded_input = pad_sequences(input_seq, maxlen=max_sequence_len, padding='post')
    predicted_output = model.predict(padded_input)
    predicted_word_index = tf.argmax(predicted_output, axis=-1).numpy()[0]
    response = tokenizer.sequences_to_texts([predicted_word_index])
    return response[0]

# Interaction loop
while True:
    user_input = input(">>> ")
    response = generate_response(user_input)
    print(f"Chatbot: {response}")