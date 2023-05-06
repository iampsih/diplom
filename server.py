from flask import Flask, Response, render_template
import json
from models import DB

app = Flask(__name__, static_url_path='', template_folder='static')

db = DB()

@app.route('/')
def index():
    c_list = db.get_courses_list()
    print(c_list)
    return render_template('index.html', courses=c_list)

@app.route('/course/<int:course_id>')
def get_course(course_id):
    c_data = db.get_course_data(course_id)
    l_list = db.get_lessons_list(course_id)
    return render_template('courses.html', data=c_data, lessons=l_list)

@app.route('/course/<int:course_id>/lesson/<int:lesson_id>')
def get_lesson(course_id, lesson_id):
    l_list = db.get_lessons_list(course_id)
    l_data = db.get_lesson_data(course_id, lesson_id)
    if lesson_id >= len(l_list):
        l_data['id'] = 0
    return render_template('lesson.html', course_id=course_id, data=l_data, lessons=l_list)

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
