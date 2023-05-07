import mysql.connector as mysql

class DB:
    def __init__(self):
        self.db = mysql.connect(
            host='db4free.net',
            user='diplom_cavechart',
            password='f4ef91557b471aa8dd4eb32e772a9873b49be455',
            database='diplom_cavechart',
            port='3306',
            # connect_timeout=180,
        )
        self.cursor = self.db.cursor()

    def get_courses_list(self):
        result = []
        if self.cursor:
            self.cursor.execute("SELECT id, title_short, image, desc_mini FROM courses")
            data = self.cursor.fetchall()
            for item in data:
                item_data = {
                    'id': item[0],
                    'title_short': item[1],
                    'image': item[2],
                    'mini_desc': item[3].decode('utf-8'),
                }
                result.append(item_data)
        return result

    def get_course_data(self, course_id):
        result = None
        if self.cursor:
            self.cursor.execute("SELECT id, title_long, image, image_alt, desc_full FROM courses where id = " +str(course_id))
            data = self.cursor.fetchall()
            for item in data:
                result = {
                    'id': item[0],
                    'title_long': item[1],
                    'image': item[2],
                    'image_alt': item[3],
                    'full_desc': item[4].decode('utf-8'),
                }
                break
        return result

    def get_lessons_list(self, course_id):
        result = []
        if self.cursor:
            self.cursor.execute("SELECT id, title, image, desc_long FROM lessons where course_id = " + str(course_id))
            data = self.cursor.fetchall()
            for item in data:
                item_data = {
                    'id': item[0],
                    'title': item[1],
                    'image': item[2],
                    'desc_long': item[3],
                }
                result.append(item_data)
        return result

    def get_lesson_data(self, course_id, lesson_id):
        result = None
        if self.cursor:
            self.cursor.execute("SELECT id, title, image, desc_long, url FROM lessons where id = " + str(lesson_id))
            data = self.cursor.fetchall()
            for item in data:
                result = {
                    'id': item[0],
                    'title': item[1],
                    'image': item[2],
                    'desc_long': item[3],
                    'url': item[4],
                }
                break
        return result

if __name__ == "__main__":
    db = DB()
    print(db.get_courses_list())
