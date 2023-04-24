from flask import Flask, Response
import json

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_courses/')
def get_all_courses():
    resp = [
        {
            'id': 1,
            'title': 'Python course',
            'image': '/assets/images/courses-01.jpg',
            'mini_desc': 'asdadsasdasdada',
            'url': '/courses/1'
        },
        {
            'id': 2,
            'title': 'Java course',
            'image': '/assets/images/courses-02.jpg',
            'mini_desc': 'asdadsasdasdada',
            'url': '/courses/2'
        },
        {
            'id': 3,
            'title': 'Golang course',
            'image': '/assets/images/courses-03.jpg',
            'mini_desc': 'asdadsasdasdada',
            'url': '/courses/3'
        }
    ]
    return return_json_response(resp)

@app.route('/get_course/<int:course_id>')
def get_course(course_id):
    resp = [
        {
            'title': 'Python course',
            'image': '/assets/images/courses-01.jpg',
            'full_desc': 'asdadsasdasdadaasdadsasdasdadaasdadsasdasd<br>adaasdadsasdasdadaasdadsasdasdadaasdadsasdasdadaasdadsasdasdada',
            'lessons': [
                {
                    'id': 1,
                    'title': 'Lesson 1',
                    'image': '/assets/images/courses-01.jpg',
                },
                {
                    'id': 2,
                    'title': 'Lesson 2',
                    'image': '/assets/images/courses-02.jpg',
                    'url': '/courses/{course_id}/lessons/2',
                    'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                }
            ]
        }
    ]
    return return_json_response(resp)

@app.route('/get_lessons/<int:course_id>')
def get_lessons(course_id):
    resp = [
        {
            'title': 'Python course',
            'image': '/assets/images/courses-01.jpg',
            'full_desc': 'asdadsasdasdadaasdadsasdasdadaasdadsasdasd<br>adaasdadsasdasdadaasdadsasdasdadaasdadsasdasdadaasdadsasdasdada',
            'lessons': [
                {
                    'id': 1,
                    'title': 'Lesson 1',
                    'image': '/assets/images/courses-01.jpg',
                    'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                },
                {
                    'id': 2,
                    'title': 'Lesson 2',
                    'image': '/assets/images/courses-02.jpg',
                    'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                }
            ]
        }
    ]
    return return_json_response(resp)

def dump_json(passed_json):
    return json.dumps(passed_json, indent=4, sort_keys=True, default=str)

def return_json_response(json):
    return Response(dump_json(json),
        status=200, mimetype='application/json')

def return_failed_response(ex):
    return Response(dump_json({"error": ex}),
        status=500, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
