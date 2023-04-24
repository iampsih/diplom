from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/courses/')
def get_all_courses():
    resp = [
        {
            'title': 'Python course',
            'image': '/assets/images/courses-01.jpg',
            'mini_desc': 'asdadsasdasdada',
            'url': '/courses/1'
        },
        {
            'title': 'Java course',
            'image': '/assets/images/courses-02.jpg',
            'mini_desc': 'asdadsasdasdada',
            'url': '/courses/2'
        },
        {
            'title': 'Golang course',
            'image': '/assets/images/courses-03.jpg',
            'mini_desc': 'asdadsasdasdada',
            'url': '/courses/3'
        }
    ]
    return return_json_response(resp)

@app.route('/courses/<int:course_id>')
def get_course(course_id):
    resp = [
        {
            'title': 'Python course',
            'image': '/assets/images/courses-01.jpg',
            'full_desc': 'asdadsasdasdadaasdadsasdasdadaasdadsasdasd<br>adaasdadsasdasdadaasdadsasdasdadaasdadsasdasdadaasdadsasdasdada',
            'lessons': [
                {
                    'title': 'Lesson 1',
                    'image': '/assets/images/courses-01.jpg',
                    'url': '/courses/{course_id}/lessons/1',
                    'youtube': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                },
                {
                    'title': 'Lesson 2',
                    'image': '/assets/images/courses-02.jpg',
                    'url': '/courses/{course_id}/lessons/2',
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
