import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained CNN model
model = tf.keras.models.load_model('cnn_model.h5')

def process_image(filepath):
    image = Image.open(filepath).convert('L')  # grayscale
    image = ImageOps.invert(image)             # invert to match MNIST
    image = image.resize((28, 28))             # resize to 28x28 for MNIST
    image = np.array(image)
    image = image / 255.0                      # scale to 0-1 for MNIST
    image = image.reshape(1, 28, 28, 1)        # shape for CNN
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction_text='No file uploaded.')

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction_text='No selected file.')

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(filepath)

    try:
        image_data = process_image(filepath)
        prediction = np.argmax(model.predict(image_data), axis=1)[0]
        return render_template('index.html', prediction_text=f'Digit: {prediction}', image_path=filepath)
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error processing image: {e}')

if __name__ == '__main__':
    app.run(debug=True)
