# SportPulse - Sports Popularity Prediction

A Flask web application that uses ARIMA and SARIMA models to predict sports popularity trends.

## 🚀 Quick Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/new?template=https://github.com/yourusername/sportpulse)

## 📋 Manual Deployment Steps

### 1. Prepare Your Repository
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Push to GitHub
git remote add origin https://github.com/yourusername/sportpulse.git
git push -u origin main
```

### 2. Deploy on Railway
1. Go to [railway.app](https://railway.app)
2. Sign up/Login with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will automatically detect Python and deploy

### 3. Configure Environment Variables (Optional)
- `FLASK_ENV=production`
- `PORT=5000` (Railway sets this automatically)

## 🏗️ Project Structure
```
sports_popularity_prediction/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── railway.json          # Railway deployment config
├── runtime.txt           # Python version
├── multiTimeline.csv     # Dataset
├── models/               # ML model modules
├── static/               # CSS, JS files
└── templates/            # HTML templates
```

## 🛠️ Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Access at http://localhost:5000
```

## 📊 Features
- **Multi-Sport Support**: NBA, Premier League, LaLiga, NFL
- **Dual Models**: ARIMA and SARIMA
- **Interactive Visualizations**: Plotly charts
- **Accuracy Analysis**: Model performance metrics
- **Responsive Design**: Mobile-friendly interface

## 🔧 Technologies Used
- **Backend**: Flask, Python
- **ML Models**: Statsmodels (ARIMA/SARIMA)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualization**: Plotly.js
- **Deployment**: Railway, Gunicorn

## 📝 License
MIT License 