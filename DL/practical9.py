
import numpy as np
import pandas as pd
import os
import kagglehub
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


path = kagglehub.dataset_download("seesea0203/umich-si650-nlp")
print("Dataset path:", path)


print(os.listdir(path))


train_data = pd.read_csv(os.path.join(path, "train.csv"))
test_data = pd.read_csv(os.path.join(path, "test.csv"))
print(train_data.head())


print(train_data.columns)
print(test_data.columns)


X_train = train_data['sentence'].values
y_train = train_data['label'].values


X_test = test_data['sentence'].values


tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)


max_len = 50
X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)


model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=64, input_length=max_len))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))


model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)


model.fit(
    X_train_pad,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.2
)


predictions = model.predict(X_test_pad)


predicted_labels = (predictions > 0.5).astype(int)


for i in range(5):
    print(
        X_test[i],
        "→",
        "Positive" if predicted_labels[i] == 1 else "Negative"
    )

