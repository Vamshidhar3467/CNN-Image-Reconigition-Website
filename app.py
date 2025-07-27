import os
import logging
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your-secret-key-here'  # For flash messages

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the trained CNN model
try:
    model = tf.keras.models.load_model('cnn_model.h5')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(filepath):
    try:
        image = Image.open(filepath).convert('L')  # grayscale
        image = ImageOps.invert(image)             # invert to match MNIST
        image = image.resize((28, 28))             # resize to 28x28 for MNIST
        image = np.array(image)
        image = image / 255.0                      # scale to 0-1 for MNIST
        image = image.reshape(1, 28, 28, 1)        # shape for CNN
        return image
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', 
                             prediction_text='Error: Model not loaded. Please try again later.',
                             error=True)
    
    if 'file' not in request.files:
        return render_template('index.html', 
                             prediction_text='No file uploaded. Please select an image.',
                             error=True)

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', 
                             prediction_text='No file selected. Please choose an image.',
                             error=True)

    if not allowed_file(file.filename):
        return render_template('index.html', 
                             prediction_text='Invalid file type. Please upload an image (PNG, JPG, JPEG, GIF, BMP).',
                             error=True)

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        logger.info(f"Processing image: {filename}")
        image_data = process_image(filepath)
        prediction = np.argmax(model.predict(image_data), axis=1)[0]
        confidence = float(np.max(model.predict(image_data), axis=1)[0])
        
        result_text = f'Predicted Digit: {prediction} (Confidence: {confidence:.2%})'
        logger.info(f"Prediction: {result_text}")
        
        return render_template('index.html', 
                             prediction_text=result_text, 
                             image_path=filepath,
                             confidence=confidence)
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return render_template('index.html', 
                             prediction_text=f'Error processing image: {str(e)}. Please try a different image.',
                             error=True)

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return {'status': 'healthy', 'model_loaded': model is not None}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
