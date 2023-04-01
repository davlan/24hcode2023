import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Définir les paramètres de notre modèle
batch_size = 32
img_height = 224
img_width = 224
num_epochs = 10

# Charger les images depuis les répertoires et prétraiter
train_data_gen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)

# Créer les générateurs d'images pour l'entraînement et la validation
train_generator = train_data_gen.flow_from_directory(
    './train/',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

val_data_gen = ImageDataGenerator(rescale=1./255)

val_generator = val_data_gen.flow_from_directory(
    './val/',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

# Créer notre modèle CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compiler notre modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraîner notre modèle
history = model.fit(
    train_generator,
    epochs=num_epochs,
    validation_data=val_generator
)

# Évaluer notre modèle sur le jeu de données d'évaluation
test_data_gen = ImageDataGenerator(rescale=1./255)

test_generator = test_data_gen.flow_from_directory(
    './test/',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

test_loss, test_acc = model.evaluate(test_generator)
