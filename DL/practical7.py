
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU, Reshape, Flatten
from tensorflow.keras.optimizers import Adam


(x_train, _), (_, _) = mnist.load_data()


x_train = (x_train.astype(np.float32) - 127.5) / 127.5


x_train = x_train.reshape(x_train.shape[0], 784)


def build_generator():
    model = Sequential()
    model.add(Dense(256, input_dim=100))
    model.add(LeakyReLU(0.2))

    model.add(Dense(512))
    model.add(LeakyReLU(0.2))

    model.add(Dense(1024))
    model.add(LeakyReLU(0.2))

    model.add(Dense(784, activation='tanh'))
    return model


def build_discriminator():
    model = Sequential()
    model.add(Dense(1024, input_dim=784))
    model.add(LeakyReLU(0.2))

    model.add(Dense(512))
    model.add(LeakyReLU(0.2))

    model.add(Dense(256))
    model.add(LeakyReLU(0.2))

    model.add(Dense(1, activation='sigmoid'))
    return model


discriminator = build_discriminator()
discriminator.compile(
    loss='binary_crossentropy',
    optimizer=Adam(0.0002, 0.5),
    metrics=['accuracy']
)


generator = build_generator()


discriminator.trainable = False

gan = Sequential()
gan.add(generator)
gan.add(discriminator)

gan.compile(
    loss='binary_crossentropy',
    optimizer=Adam(0.0002, 0.5)
)


epochs = 5000
batch_size = 64

for epoch in range(epochs):
   
    idx = np.random.randint(0, x_train.shape[0], batch_size)
    real_images = x_train[idx]

   
    noise = np.random.normal(0, 1, (batch_size, 100))
    fake_images = generator.predict(noise)

   
    real_labels = np.ones((batch_size, 1))
    fake_labels = np.zeros((batch_size, 1))

    
    d_loss_real = discriminator.train_on_batch(real_images, real_labels)
    d_loss_fake = discriminator.train_on_batch(fake_images, fake_labels)

 
    noise = np.random.normal(0, 1, (batch_size, 100))
    g_loss = gan.train_on_batch(noise, real_labels)

    if epoch % 500 == 0:
        print(f"Epoch {epoch} | D Loss: {d_loss_real[0]} | G Loss: {g_loss}")


def generate_images():
    noise = np.random.normal(0, 1, (10, 100))
    generated_images = generator.predict(noise)
    generated_images = generated_images.reshape(10, 28, 28)

    plt.figure(figsize=(10, 2))
    for i in range(10):
        plt.subplot(1, 10, i+1)
        plt.imshow(generated_images[i], cmap='gray')
        plt.axis('off')

    plt.show()

generate_images()