#!/usr/bin/env python3
"""
Test script for the CNN Digit Recognition App
"""

import requests
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_test_digit(digit, filename="test_digit.png"):
    """Create a test image with a handwritten digit"""
    # Create a 200x200 white image
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fallback to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        font = ImageFont.load_default()
    
    # Draw the digit in black
    text = str(digit)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (200 - text_width) // 2
    y = (200 - text_height) // 2
    draw.text((x, y), text, fill='black', font=font)
    
    # Save the image
    img.save(filename)
    print(f"Created test image: {filename}")
    return filename

def test_local_app():
    """Test the app locally"""
    print("🧪 Testing Local App...")
    
    # Create test images
    test_files = []
    for digit in [3, 5, 7, 9]:
        filename = create_test_digit(digit, f"test_{digit}.png")
        test_files.append(filename)
    
    # Test each image
    for filename in test_files:
        print(f"\n📸 Testing with {filename}...")
        
        with open(filename, 'rb') as f:
            files = {'file': f}
            try:
                response = requests.post('http://localhost:5000/predict', files=files)
                if response.status_code == 200:
                    print(f"✅ Success! Response: {response.text[:100]}...")
                else:
                    print(f"❌ Error: Status {response.status_code}")
            except requests.exceptions.ConnectionError:
                print("❌ Could not connect to local app. Make sure it's running on localhost:5000")
                break
    
    # Clean up test files
    for filename in test_files:
        if os.path.exists(filename):
            os.remove(filename)

def test_deployed_app(app_url):
    """Test the deployed app"""
    print(f"🌐 Testing Deployed App at: {app_url}")
    
    # Create a test image
    test_file = create_test_digit(5, "test_deployed.png")
    
    try:
        with open(test_file, 'rb') as f:
            files = {'file': f}
            response = requests.post(f'{app_url}/predict', files=files)
            
            if response.status_code == 200:
                print("✅ Deployed app is working!")
                print(f"Response: {response.text[:200]}...")
            else:
                print(f"❌ Error: Status {response.status_code}")
                print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Error testing deployed app: {e}")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)

def test_health_endpoint(app_url):
    """Test the health endpoint"""
    try:
        response = requests.get(f'{app_url}/health')
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data}")
        else:
            print(f"❌ Health check failed: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")

if __name__ == "__main__":
    print("🚀 CNN Digit Recognition App Tester")
    print("=" * 40)
    
    # Test local app if running
    test_local_app()
    
    print("\n" + "=" * 40)
    print("🌐 To test deployed app, run:")
    print("python test_app.py --deployed YOUR_APP_URL")
    
    # Check if deployed URL is provided
    import sys
    if len(sys.argv) > 2 and sys.argv[1] == '--deployed':
        app_url = sys.argv[2]
        test_health_endpoint(app_url)
        test_deployed_app(app_url) 