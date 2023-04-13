simport docx2txt

# Load the Word file
text = docx2txt.process("my_word_file.docx")

# Clean and preprocess the text data
text = text.lower()  # convert all letters to lowercase
text = ''.join(c for c in text if c.isalpha() or c.isspace())  # remove non-alphabetic characters


# Tokenize the text into words
words = text.split()


import random

# Build a Markov chain
chain = {}
for i in range(len(words)-1):
    if words[i] not in chain:
        chain[words[i]] = []
    chain[words[i]].append(words[i+1])

# Use the Markov chain to generate new text
generated_text = ""
current_word = random.choice(words)
while len(generated_text) < 1000:
    generated_text += current_word + " "
    if current_word not in chain:
        current_word = random.choice(words)
    else:
        current_word = random.choice(chain[current_word])


import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
sequences = tokenizer.texts_to_sequences([text])
max_sequence_length = max([len(x) for x in sequences])
vocab_size = len(tokenizer.word_index) + 1

# Pad the sequences to a fixed length
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='pre')

# Split the sequences into input/output pairs
X = padded_sequences[:,:-1]
y = padded_sequences[:,-1]

# Define the RNN model
model = Sequential([
    Embedding(vocab_size, 50, input_length=max_sequence_length-1),
    LSTM(100),
    Dense(vocab_size, activation='softmax')
])

# Train the RNN model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=100, verbose=1)

# Use the RNN model to generate new text
generated_text = ""
current_sequence = sequences[0]
for i in range(1000):
    padded_sequence = pad_sequences([current_sequence], maxlen=max_sequence_length-1, padding='pre')
    prediction = model.predict(padded_sequence)
    predicted_index = tf.random.categorical(prediction, num_samples=1)[-1,0].numpy()
    predicted_word = list(tokenizer.word_index.keys())[list(tokenizer.word_index.values()).index(predicted_index)]
    generated_text += predicted_word + " "
    current_sequence = current_sequence[1:] + [predicted_index]

import openai
import os

# Set up the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Generate text with GPT-3
prompt = "Once upon a time"
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  temperature=0.7,
  max_tokens=1000,
  n=1,
  stop=None,
  timeout=20,
)

# Print the generated text
generated_text = response.choices[0].text.strip()
print(generated_text)
