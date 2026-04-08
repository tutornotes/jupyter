import numpy as np
import pandas as pd
import os
import kagglehub
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

# a) Load dataset
path = kagglehub.dataset_download("seesea0203/umich-si650-nlp")
print("Dataset path:", path)

train_data = pd.read_csv(os.path.join(path, "train.csv"))
test_data = pd.read_csv(os.path.join(path, "test.csv"))

X_train = train_data['sentence'].values
y_train = train_data['label'].values
X_test = test_data['sentence'].values

# Preprocess text
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

max_len = 50
X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

# b) Build LSTM model
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=64, input_length=max_len))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

# c) Compile & train
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train_pad,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.2
)

# d) Predict on unseen data
predictions = model.predict(X_test_pad)
predicted_labels = (predictions > 0.5).astype(int)

for i in range(5):
    print(
        X_test[i],
        "→",
        "Positive" if predicted_labels[i] == 1 else "Negative"
    )

# e) Evaluate performance (graphs)
plt.figure(figsize=(12,5))

# Accuracy
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy Curve')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Loss
plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss Curve')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()