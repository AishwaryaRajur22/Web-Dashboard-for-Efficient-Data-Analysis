import matplotlib.dates as mdates
import os
import psycopg2
import time
from flask import Flask, render_template, request, send_from_directory, jsonify
from matplotlib.figure import Figure

DB_NAME = os.environ['POSTGRES_DB']
DB_USER = os.environ['POSTGRES_USER']
DB_PASS = os.environ['POSTGRES_PASSWORD']
DB_HOST = os.environ['POSTGRES_HOST']
DB_PORT = os.environ['POSTGRES_PORT']

while True:
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
        break
    except Exception as e:
        print("Database not connected successfully\n", e)
        time.sleep(2)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/visualize')
def visualize():
    data_type = request.args.get('dataType')
    table_name = None
    y_axis_name = None
    if data_type == "temperature":
        table_name = "CM_HAM_DO_AI1/Temp_value"
        y_axis_name = "Temperature"
    elif data_type == "ph":
        table_name = "CM_HAM_PH_AI1/pH_value"
        y_axis_name = "pH"
    elif data_type == "oxygen":
        table_name = "CM_PID_DO/Process_DO"
        y_axis_name = "Distilled Oxygen"
    elif data_type == "pressure":
        table_name = "CM_PRESSURE/Output"
        y_axis_name = "Pressure"
    
    cur = conn.cursor()
    cur.execute('SELECT * FROM "{}"'.format(table_name))
    results = cur.fetchall()
    date, value = list(zip(*results))

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    fig.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y , %H:%M:%S'))
    axis.set_xticks([date[0], date[-1]])
    axis.set_xlabel("Time")
    axis.set_ylabel(y_axis_name)
    axis.plot(date, value)

    folder = "images/"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        os.unlink(file_path)
    filename = folder + str(time.time()) + ".png"
    fig.savefig(filename)
    message = "/files/"+filename
    return jsonify(message=message)

@app.route('/files/<path:path>',methods = ['GET'])
def get_files(path):
    return send_from_directory(".", path, as_attachment=True)

app.run(host="0.0.0.0", port=8888)