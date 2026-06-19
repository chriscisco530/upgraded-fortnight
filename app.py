from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id TEXT,
        name TEXT,
        email TEXT,
        course TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/students', methods=['POST'])
def add_student():
    student_id = request.form['studentId']
    full_name = request.form['fullName']
    email = request.form['email']
    course = request.form['course']
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('INSERT INTO students VALUES (?,?,?,?)',
              (student_id, full_name, email, course))
    conn.commit()
    conn.close()
    return render_template('students.html', students=get_students())

@app.route('/delete/<student_id>',methods=['POST'])
def delete_student(student_id):
    conn=sqlite3.connect('students.db')
    c=conn.cursor()
    c.execute('DELETE FROM students WHERE id=?',(student_id,))
    conn.commit()
    conn.close()
    return render_template('students.html',students=get_students())

def get_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return students

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
