# 🚀 Deployment Guide: CNN Image Recognition App

## 📋 Prerequisites
- GitHub account
- Render account (free tier available)

## 🎯 Step-by-Step Deployment to Render

### Step 1: Prepare Your Repository
1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Fix deployment dependencies"
   git push origin main
   ```

### Step 2: Deploy to Render
1. **Go to [Render.com](https://render.com)** and sign up/login
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name**: `cnn-digit-recognition`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or paid for better performance)

### Step 3: Environment Variables (Optional)
Add these in Render dashboard if needed:
- `FLASK_ENV=production`
- `FLASK_DEBUG=0`

### Step 4: Deploy
1. **Click "Create Web Service"**
2. **Wait for build** (5-10 minutes for first deployment)
3. **Your app will be live at**: `https://your-app-name.onrender.com`

## 🔧 Files Added for Deployment
- ✅ `requirements.txt` - Updated with stable versions (no scikit-learn)
- ✅ `Procfile` - Tells Render how to run the app
- ✅ `runtime.txt` - Specifies Python 3.10.12 (stable version)

## 🎉 What You Get
- **Free hosting** with Render
- **Automatic HTTPS**
- **Custom domain** (optional)
- **Auto-deploy** on git push
- **Logs and monitoring**

## 🚨 Important Notes
- **Free tier limitations**: 
  - 15 minutes of inactivity = sleep
  - 750 hours/month free
  - Slower cold starts
- **Model size**: Your 1.4MB model is fine for Render
- **Memory**: Free tier has 512MB RAM (sufficient for your app)

## 🔄 Alternative: Railway
If Render doesn't work, try [Railway.app](https://railway.app):
1. Similar setup process
2. Better free tier limits
3. Faster deployments

## 🆘 Troubleshooting

### ❌ Build Fails with scikit-learn Error
**Problem**: `Cython.Compiler.Errors.CompileError: sklearn/linear_model/_cd_fast.pyx`

**Solution**: ✅ **FIXED** - Removed scikit-learn from requirements.txt (not used in your app)

### ❌ Other Common Issues:
- **Build fails**: Check requirements.txt versions
- **App crashes**: Check logs in Render dashboard
- **Model not found**: Ensure `cnn_model.h5` is in repository
- **Memory issues**: Consider paid plan for more RAM
- **Python version issues**: Using Python 3.10.12 (very stable)

### 🔧 Manual Fix Steps:
1. **If build still fails**, try these versions:
   ```
   flask==2.0.3
   pillow==9.0.1
   numpy==1.21.6
   tensorflow==2.8.0
   gunicorn==20.1.0
   werkzeug==2.0.3
   ```

2. **Check Render logs** for specific error messages
3. **Ensure all files are committed** to GitHub

## 📱 Testing Your Deployed App
1. Upload an image of a handwritten digit
2. Click "Predict Digit"
3. Verify the prediction works correctly

---
**🎯 Your app will be live and accessible worldwide!**

## ✅ What Was Fixed
- **Removed scikit-learn** (not used in your app)
- **Updated to Python 3.10.12** (more stable)
- **Used conservative package versions** (better compatibility)
- **Added troubleshooting section** for common issues 