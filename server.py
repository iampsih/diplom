from flask import Flask, Response, render_template
import json
from models import courses

app = Flask(__name__, static_url_path='', template_folder='static')

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def get_course(course_id):
    resp = courses[course_id - 1]
    return render_template('courses.html', data=resp, lessons=resp['lessons'])

@app.route('/course/<int:course_id>/lesson/<int:lesson_id>')
def get_lessons(course_id, lesson_id):
    resp = {
        'title': 'Python тiлiнде <em> бағдарламалау негiздерi</em>',
        'image': '/assets/images/courses-01.jpg',
        'image_alt': 'ПИТОН ТІЛІ',
        'full_desc': '''<p>
                Бұл бағдарламалауға кiрiспе курсы ешбiр алғашқы бiлiм мен
                тəжiрибесi жоқ барлық үйренемiн деушiлерге ашық, соның ішінде
                әсіресе жоғарғы сынып оқушылары мен студенттерге арналған.
                Курстың мақсаты тереңдетiлген бiлiмнен гөрi бағдарламалаудың
                негiзгi ұғымдарын үйрену. Практикалық шолу жасау болғандықтан,
                бағдарламалау тiлi ретiнде Python (Питон) таңдалды.
              </p>
              <h5>Бұл курста не үйренесіз?</h5>
              <ul class="lesson-ul">
                <li>
                  * Python бағдарламалау тілі туралы іргелі түсінікке ие
                  болыңыз.
                </li>
                <li>* Функцияларды программалауды үйрену.</li>
                <li>* Объектіге бағытталған программалау</li>
                <li>
                  * Таза, өнімді және қатесіз код жазудың ең жақсы тәжірибелерін
                  үйреніңіз.
                </li>
              </ul>''',
    }
    lessons = [
        {
            'id': 1,
            'title': 'Lesson 1',
            'desc': 'Бұл бағдарламалауға кiрiспе курсы ешбiр алғашқы бiлiм мен тəжiрибесi жоқ барлық үйренемiн деушiлерге ашық, соның ішінде әсіресе жоғарғы сынып оқушылары мен студенттерге арналған.',
            'image': '/assets/images/courses-01.jpg',
            'url': f'/course/{course_id}/lesson/1',
            'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        },
        {
            'id': 2,
            'title': 'Lesson 2',
            'desc': 'Бұл бағдарламалауға кiрiспе курсы ешбiр алғашқы бiлiм мен тəжiрибесi жоқ барлық үйренемiн деушiлерге ашық, соның ішінде әсіресе жоғарғы сынып оқушылары мен студенттерге арналған.',
            'image': '/assets/images/courses-02.jpg',
            'url': f'/course/{course_id}/lesson/2',
            'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        },
        {
            'id': 3,
            'title': 'Lesson 3',
            'desc': 'Бұл бағдарламалауға кiрiспе курсы ешбiр алғашқы бiлiм мен тəжiрибесi жоқ барлық үйренемiн деушiлерге ашық, соның ішінде әсіресе жоғарғы сынып оқушылары мен студенттерге арналған.',
            'image': '/assets/images/courses-03.jpg',
            'url': f'/course/{course_id}/lesson/3',
            'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        },
        {
            'id': 4,
            'title': 'Lesson 4',
            'desc': 'Бұл бағдарламалауға кiрiспе курсы ешбiр алғашқы бiлiм мен тəжiрибесi жоқ барлық үйренемiн деушiлерге ашық, соның ішінде әсіресе жоғарғы сынып оқушылары мен студенттерге арналған.',
            'image': '/assets/images/courses-04.jpg',
            'url': f'/course/{course_id}/lesson/4',
            'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        }
    ]
    return render_template('courses.html', data=resp, lessons=lessons)

def dump_json(passed_json):
    return json.dumps(passed_json, indent=4, sort_keys=True, default=str)

def return_json_response(json):
    return Response(dump_json(json),
        status=200, mimetype='application/json')

def return_failed_response(ex):
    return Response(dump_json({"error": ex}),
        status=500, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
