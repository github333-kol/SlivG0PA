from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        "title": "Главная страница",
        "name": "коля",
        "weather": "cloudy",
        "fruits":  ["Мандарин", "Киви", "Яблоко"],
        "poems": [
            {
                "head": "Стихотворение ноемр один",
                "text": "Однажды в студёную зимнюю пору",
                "author": "Некрасов"
            },
            {
                "head": "Стихотворение ноемр два",
                "text": "У лукоморья дуб зеленый",
                "author": "Пушкин"
            },
        ]
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)