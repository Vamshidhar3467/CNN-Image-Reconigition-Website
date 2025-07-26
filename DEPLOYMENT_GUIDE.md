# 🚀 Deployment Guide: CNN Image Recognition App

## 📋 Prerequisites
- GitHub account
- Render account (free tier available)

## 🎯 Step-by-Step Deployment to Render

### Step 1: Prepare Your Repository
1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Prepare for deployment"
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
- ✅ `requirements.txt` - Updated with specific versions
- ✅ `Procfile` - Tells Render how to run the app
- ✅ `runtime.txt` - Specifies Python version

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
- **Build fails**: Check requirements.txt versions
- **App crashes**: Check logs in Render dashboard
- **Model not found**: Ensure `cnn_model.h5` is in repository
- **Memory issues**: Consider paid plan for more RAM

## 📱 Testing Your Deployed App
1. Upload an image of a handwritten digit
2. Click "Predict Digit"
3. Verify the prediction works correctly

---
**🎯 Your app will be live and accessible worldwide!** 