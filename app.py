from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Cho phép tất cả các nguồn truy cập

# Load the trained model
model = load_model('cat_dog_mobilenetv2.h5')

# Define image size expected by the model (e.g., 224x224 for MobileNetV2)
IMG_SIZE = (224, 224)

# Function to predict the image label
def predict_image(img):
    img = img.resize(IMG_SIZE)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize image
    prediction = model.predict(img_array)
    return "dog" if prediction[0][0] > 0.5 else "cat"

# API endpoint to handle image classification
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    img_file = request.files['image']
    img = Image.open(io.BytesIO(img_file.read()))
    
    # Get prediction
    label = predict_image(img)
    
    return jsonify({'label': label})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
