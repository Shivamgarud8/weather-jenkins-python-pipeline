from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = "2c400b4eb0d3d8789bc77c4c9ca18d4f"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    try:
        res = requests.get(url)
        data = res.json()
        
        if data.get("cod") != 200:
            return render_template('result.html', error="City not found!", weather=None)

        weather_data = {
            'city': city.title(),
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed']
        }

        return render_template('result.html', weather=weather_data, error=None)

    except Exception as e:
        return render_template('result.html', error=f"Error: {str(e)}", weather=None)

# Bind Flask to all interfaces (EC2-friendly)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
