from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = 'fcac306876574effe5d7505756960ecf'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.template_filter('timestamp_to_date')
def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%d %b %Y')

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'imperial'
            }
            response = requests.get(WEATHER_URL, params=params)
            weather_data = response.json()

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
