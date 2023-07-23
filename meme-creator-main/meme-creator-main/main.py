#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        selected_image = request.form.get('image-selector')
        selected_text = request.form.get('text-selector')
        selected_color = request.form.get('color-selector')
        text_bottom = request.form.get('textBottom')
        text_top = request.form.get('textTop')
        text_top_y = request.form.get('textTop_y')
        text_bottom_y =request.form.get('textBottom_y')
        color_selector = request.form.get('color-selector')
        # Задание №3. Получаем цвет текста
        

        return render_template('index.html', 
                               selected_image=selected_image, 
                               selected_text=selected_text,
                               text_top = text_top,
                               text_bottom = text_bottom,
                               text_bottom_y = text_bottom_y,
                               text_top_y = text_top_y,
                               selected_color = selected_color,
                               color_selector = color_selector
                               #Задание №3. Отоброжаем расположение текста

                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
