import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
# Load the trained model
tf.config.set_visible_devices([], 'GPU')
IMG_SIZE = (224, 224)

model = load_model('cat_dog_mobilenetv2.h5')
def predict_image(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        return "Dog"
    else:
        return "Cat"

img_path = 'husky-3380548_1280.jpg'  
print(predict_image(img_path))