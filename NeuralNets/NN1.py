import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# import matplotlib.pyplot as plt

# # ----------------------------
# # 1️⃣ Load dataset from directory
# # ----------------------------
# # Folder structure should look like this:
# # dataset/
# # ├── train/
# # │   ├── cats/
# # │   └── dogs/
# # └── validation/
# #     ├── cats/
# #     └── dogs/

# train_ds = tf.keras.utils.image_dataset_from_directory(
#     "dataset/train",
#     image_size=(128, 128),
#     batch_size=32
# )

# val_ds = tf.keras.utils.image_dataset_from_directory(
#     "dataset/validation",
#     image_size=(128, 128),
#     batch_size=32
# )

# # ----------------------------
# # 2️⃣ Normalize pixel values (0–1)
# # ----------------------------
# normalization_layer = layers.Rescaling(1./255)
# train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
# val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

# # ----------------------------
# # 3️⃣ Build a CNN model
# # ----------------------------
# model = keras.Sequential([
#     layers.Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
#     layers.MaxPooling2D(2, 2),

#     layers.Conv2D(64, (3,3), activation='relu'),
#     layers.MaxPooling2D(2, 2),

#     layers.Conv2D(128, (3,3), activation='relu'),
#     layers.MaxPooling2D(2, 2),

#     layers.Flatten(),
#     layers.Dense(128, activation='relu'),
#     layers.Dense(1, activation='sigmoid')  # Binary output
# ])

# # ----------------------------
# # 4️⃣ Compile model
# # ----------------------------
# model.compile(
#     optimizer='adam',
#     loss='binary_crossentropy',
#     metrics=['accuracy']
# )

# # ----------------------------
# # 5️⃣ Train model
# # ----------------------------
# history = model.fit(
#     train_ds,
#     validation_data=val_ds,
#     epochs=10
# )

# # ----------------------------
# # 6️⃣ Evaluate performance
# # ----------------------------
# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1)
# plt.plot(acc, label='Training Accuracy')
# plt.plot(val_acc, label='Validation Accuracy')
# plt.legend()
# plt.title('Accuracy')

# plt.subplot(1, 2, 2)
# plt.plot(loss, label='Training Loss')
# plt.plot(val_loss, label='Validation Loss')
# plt.legend()
# plt.title('Loss')
# plt.show()

# # ----------------------------
# # 7️⃣ Test with a custom image
# # ----------------------------
# import numpy as np
# from PIL import Image

# img = Image.open("my_test_image.jpg").resize((128, 128))
# img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

# prediction = model.predict(img_array)[0][0]
# if prediction > 0.5:
#     print(f"Prediction: 🐶 Dog ({prediction:.2f})")
# else:
#     print(f"Prediction: 🐱 Cat ({1 - prediction:.2f})")



