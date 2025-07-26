# 🧪 Testing Guide: CNN Digit Recognition App

## 🎯 Quick Test Steps

### 1. **Find Your App URL**
- Go to your Render dashboard
- Click on your web service
- Copy the URL (e.g., `https://your-app-name.onrender.com`)

### 2. **Basic Manual Testing**
1. **Visit your app URL**
2. **Upload a test image** (use one of your existing images: 3.png, 5.png, 51.png, 52.png)
3. **Click "Predict Digit"**
4. **Verify the prediction** and confidence score

### 3. **Test with Different Images**
- Try uploading different digit images
- Test with various image formats (PNG, JPG)
- Try uploading non-digit images (should show error)

## 🚀 Automated Testing

### **Option 1: Use the Test Script**
```bash
# Test your deployed app
python test_app.py --deployed https://your-app-name.onrender.com
```

### **Option 2: Test Health Endpoint**
Visit: `https://your-app-name.onrender.com/health`
Should return: `{"status": "healthy", "model_loaded": true}`

## 📊 What to Look For

### ✅ **Success Indicators:**
- ✅ App loads without errors
- ✅ File upload works
- ✅ Prediction returns a digit (0-9)
- ✅ Confidence score is shown (0-100%)
- ✅ Image preview displays correctly
- ✅ Loading spinner appears during processing

### ❌ **Error Indicators:**
- ❌ App doesn't load (check Render logs)
- ❌ Upload fails (check file size/format)
- ❌ Prediction fails (check model loading)
- ❌ No confidence score (check backend)

## 🔧 Troubleshooting

### **App Won't Load:**
1. Check Render dashboard for build status
2. Look at deployment logs
3. Verify all files are committed to GitHub

### **Upload Fails:**
1. Check file format (PNG, JPG, JPEG, GIF, BMP)
2. Check file size (should be under 10MB)
3. Try a different image

### **Prediction Fails:**
1. Check if model loaded correctly
2. Verify image is a clear digit
3. Check Render logs for errors

## 📱 Test Cases

### **Test Case 1: Valid Digit Image**
- **Input**: Clear handwritten digit (0-9)
- **Expected**: Correct prediction with confidence > 70%

### **Test Case 2: Invalid File**
- **Input**: Text file or non-image
- **Expected**: Error message about invalid file type

### **Test Case 3: No File**
- **Input**: Submit without selecting file
- **Expected**: Error message about no file selected

### **Test Case 4: Multiple Digits**
- **Input**: Image with multiple digits
- **Expected**: Prediction of the most prominent digit

## 🎯 Performance Testing

### **Response Time:**
- First prediction: 5-10 seconds (model loading)
- Subsequent predictions: 1-3 seconds

### **Memory Usage:**
- Should stay under 512MB (Render free tier limit)
- Model size: ~1.4MB

## 📈 Monitoring

### **Health Check:**
```bash
curl https://your-app-name.onrender.com/health
```

### **Render Dashboard:**
- Monitor CPU usage
- Check memory consumption
- View request logs

## 🚨 Common Issues & Solutions

### **Issue: App sleeps after 15 minutes**
- **Solution**: Normal for free tier, first request will be slow

### **Issue: Model loading errors**
- **Solution**: Check if `cnn_model.h5` is in repository

### **Issue: Upload folder permissions**
- **Solution**: App creates folder automatically

### **Issue: TensorFlow warnings**
- **Solution**: Normal, just informational messages

## 🎉 Success Checklist

- [ ] App loads successfully
- [ ] File upload works
- [ ] Predictions are accurate
- [ ] Confidence scores display
- [ ] Error handling works
- [ ] Health endpoint responds
- [ ] App handles different image formats
- [ ] Loading states work correctly

## 📞 Need Help?

If testing reveals issues:
1. Check Render deployment logs
2. Verify all files are committed
3. Test locally first: `python app.py`
4. Use the test script for automated testing

---
**🎯 Your app is ready for the world!** 🌍 