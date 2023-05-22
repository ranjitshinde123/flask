import os
from datetime import datetime

import pandas as pd
import xml.etree.ElementTree as ET

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pandas as pd
import mysql.connector

app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# mysql = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydb"
# )
# mysql = mysql.connector.connect(
#   host="containers-us-west-207.railway.app",
#   user="root",
#   password="BjHMCyg2DVsWsCUwiKh2",
#   database="railway",
#   port="7285"
# )

# Route for uploading Excel file
@app.route('/')
def upload():
    folder = r'/templates/uploads/'
#     files = os.listdir(folder)
    return render_template('templates/upload.html',files=folder)

# # @app.route('/all')
# # def index():
# #     # Get the list of files in the folder
# #     folder = r'/templates/uploads/'
# #     files = os.listdir(folder)
# #     # Render the template with the list of files
# #     return render_template('home.html', files=files)

# def getusers(search):
#   # conn = sqlite3.connect(DBFILE)
#   cursor = mysql.cursor()
#   print("hello")
#   # cursor.execute(
#   #   "SELECT * FROM table_name WHERE 'Production_Month'",
#   #   ("%"+search+"%", "%"+search+"%",)
#   # )

#   cursor.execute(f"select * from table_name where Production_Month={search}")
#   results = cursor.fetchall()
#   print(results)
#   cursor.close()
#   return results


# @app.route("/all", methods=["GET", "POST"])
# def index():
#     # (C1) SEARCH FOR USERS
#     if request.method == "POST":
#         data = dict(request.form)
#         print(data)
#         users = getusers(data["search"])
#         print(users)
#     else:
#         users = []
#     # (C2) RENDER HTML PAGE
#     return render_template("s3_users.html", usr=users)


# # @app.route('/', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         # Check if the username and password are correct
# #         username = request.form['username']
# #         password = request.form['password']
# #         if username == 'admin' and password == 'password':
# #             return redirect(url_for('upload'))
# #         else:
# #             error = 'Invalid Credentials. Please try again.'
# #             return render_template('login.html', error=error)
# #     return render_template('login.html')

# @app.route('/file/<path:filename>')
# def download_file(filename):
#     # Serve the file to the user
#     folder = r'C:\Users\DELL\PycharmProjects\chatGpt\chat\uploads'
#     return send_from_directory(folder, filename)

# # Route for processing the uploaded file
# @app.route('/process', methods=['POST'])
# def process():
#     file = request.files['file']
#     now = datetime.now()
#     timestamp = now.strftime('%Y_%m_%d__%H_%M')
#     filename = f"{timestamp}_{file.filename}"
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#     print(file)
#     df = pd.read_excel(file)
#     cursor = mysql.cursor()
#     for i, row in df.iterrows():
#         Production_Month = row['Production Month']
#         PPM_1MIS = row['PPM 1MIS']
#         Failures_1_MIS = row['Failures 1 MIS']
#         Fleet_1_MIS = row['Fleet 1 MIS']
#         Maturity_1_MIS = row['Maturity 1 MIS']
#         PPM_3MIS = row['PPM 3MIS']
#         Failures_3MIS = row['Failures 3MIS']
#         Fleet_3_MIS = row['Fleet 3 MIS']
#         Maturity_3_MIS = row['Maturity 3 MIS']
#         PPM_12_MIS = row['PPM 12 MIS']
#         Failures_12_MIS = row['Failures 12 MIS']
#         Fleet_12_MIS = row['Fleet 12 MIS']
#         Maturity_12_MIS = row['Maturity 12 MIS']
#         Prod_Volume = row['Prod Volume']
#         Sold_Volume = row['Sold Volume']

#         cursor.execute("INSERT INTO table_name (Production_Month, PPM_1MIS, Failures_1_MIS, Fleet_1_MIS, Maturity_1_MIS, PPM_3MIS, Failures_3MIS, Fleet_3_MIS, Maturity_3_MIS, PPM_12_MIS, Failures_12_MIS, Fleet_12_MIS, Maturity_12_MIS, Prod_Volume, Sold_Volume) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Production_Month, PPM_1MIS, Failures_1_MIS, Fleet_1_MIS, Maturity_1_MIS, PPM_3MIS, Failures_3MIS, Fleet_3_MIS, Maturity_3_MIS, PPM_12_MIS, Failures_12_MIS, Fleet_12_MIS, Maturity_12_MIS, Prod_Volume, Sold_Volume))
#         mysql.commit()
#     cursor.close()

#     df = pd.read_excel(file)

#     root = ET.Element("data")

#     for index, row in df.iterrows():
#         # Create an element for each row
#         row_element = ET.SubElement(root, "row")

#         for column_name, value in row.items():

#             column_element = ET.SubElement(row_element, column_name)
#             column_element.text = str(value)

#     tree = ET.ElementTree(root)
#     a=filename.replace('.xlsx','')
#     output_filename = a+'.xml'
#     tree.write(output_filename, encoding="UTF-8", xml_declaration=True)
#     cur = mysql.cursor()
#     query="select * from table_name"
#     cur.execute(query)
#     data = cur.fetchall()

#     return render_template('xml_file.html', filename=output_filename,a=data)


# @app.route('/download/<filename>', methods=['GET'])
# def download(filename):
#     directory = os.getcwd()
#     return send_from_directory(directory, filename, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
