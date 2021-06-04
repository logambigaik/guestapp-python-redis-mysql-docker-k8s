import os
from flask import Flask, render_template, request
from redis import Redis
import mysql.connector
app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

app = Flask(__name__)

#mysql = MySQL()

# MySQL configurations
#app.config["MYSQL_DATABASE_USER"] = "root"
#app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("MYSQL_ROOT_PASSWORD")
#app.config["MYSQL_DATABASE_DB"] = os.getenv("MYSQL_DATABASE")
#app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
#app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
#mysql.init_app(app)

config = {
    'user': 'root',
    'password': 'admin123',
    'host':  'mysqldb',
    'database':  'guestapp'

}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thanks', methods=['GET','POST'])
def thanks():

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS guestbook(visitor_name VARCHAR(20),visitor_count integer)")
    conn.commit()

    if request.method == "POST":
        details = request.form
        visitor_name = details['visitor']
        visitor_count = redis.incr('hits')
        #sql1 = "SELECT * FROM guestbook where visitor_name = %s "
        cursor.execute("SELECT * FROM guestbook where visitor_name = %s ", (visitor_name,))
        row_count = cursor.fetchone()
        if row_count == None:
            cursor.execute("INSERT INTO guestbook(visitor_name,visitor_count) VALUES (%s, %s)",
                           (visitor_name, visitor_count))

        else:
            cursor.execute("UPDATE guestbook set visitor_count = %s where visitor_name= %s ",
                           (visitor_count, visitor_name))

        conn.commit()
        cursor.close()
        return render_template("thanks.html", visitor_name=visitor_name, visitor_count=visitor_count)


@app.route('/listofvisitor', methods=['GET'])
def listofvisitor():
    if request.method == "GET":
        conn = mysql.connector.connect(**config)
        cursor=conn.cursor()
        cursor.execute("select * from guestbook")
        result = cursor.fetchall()
        return render_template('listofvisitor.html', result=result)
        cursor.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
