import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

# a) Load CIFAR-10 dataset and preprocess
(x_train, _), (x_test, _) = cifar10.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Flatten images (32x32x3 = 3072)
x_train = x_train.reshape((len(x_train), 32*32*3))
x_test = x_test.reshape((len(x_test), 32*32*3))

# b) Encoder-Decoder architecture
input_dim = 3072
encoding_dim = 256   # higher than MNIST due to complexity

input_img = Input(shape=(input_dim,))

# Encoder
encoded = Dense(512, activation='relu')(input_img)
encoded = Dense(encoding_dim, activation='relu')(encoded)

# Decoder
decoded = Dense(512, activation='relu')(encoded)
decoded = Dense(input_dim, activation='sigmoid')(decoded)

# Autoencoder model
autoencoder = Model(input_img, decoded)

# c) Compile and train
autoencoder.compile(optimizer=Adam(), loss='binary_crossentropy')

history = autoencoder.fit(
    x_train, x_train,
    epochs=20,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test, x_test)
)

# d) Reconstruct images
decoded_imgs = autoencoder.predict(x_test)

# Reshape back to image format
decoded_imgs = decoded_imgs.reshape((-1, 32, 32, 3))
x_test_images = x_test.reshape((-1, 32, 32, 3))

# Visualize results
n = 10
plt.figure(figsize=(20, 4))

for i in range(n):
    # Original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test_images[i])
    plt.title("Original")
    plt.axis('off')

    # Reconstructed
    ax = plt.subplot(2, n, i + n + 1)
    plt.imshow(decoded_imgs[i])
    plt.title("Reconstructed")
    plt.axis('off')

plt.show()

# e) Plot reconstruction loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Reconstruction Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()