import os
from datetime import datetime

import xml.etree.ElementTree as ET
import  pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file

# import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'templates'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def upload():
    folder = r'/templates'
    # files = os.listdir(folder)
    return render_template(r'upload.html',files=folder)


@app.route('/show')
def show():
    # Serve the file to the user
    # folder = r'templates\uploads'
    pass
    return render_template('test.html')

# Route for processing the uploaded file
@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    now = datetime.now()
    timestamp = now.strftime('%Y_%m_%d__%H_%M')
    filename = f"{timestamp}_{file.filename}"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    print(file)
    # df = pd.read_excel(file)
    d = pd.read_excel(file, sheet_name="RoW")
    f = d['Production Month']
    a = list(f)  # total production Month
    r = []  # all Month
    for i in range(len(a)):
        for j in range(0, 3):
            r.append(a[i])

    y = []  # MIS Type 1,3,15
    for i in range(len(a)):
        sum = 1
        e = 3
        t = 12
        y.append(sum)
        y.append(e)
        y.append(t)
    #
    # for i in r:
    #     print(i)
    # i=1
    # p=d.iloc[[i],[1,2,3,4]]
    # print(p)
    #
    # q=d.iloc[[i],[4,5,6,7]]
    # r=d.iloc[[i],[8,9,10,11]]
    # print(q)
    # print(r)

    # for j in range(len(a)):
    #     p = d.iloc[[j], [1, 2, 3, 4]]
    #     q = d.iloc[[j], [5, 6, 7,8]]
    #     r = d.iloc[[j], [9, 10, 11,12]]
    #     print

    # code for PPM

    j=d['PPM 1MIS']
    k=d['PPM 3MIS']
    l=d['PPM 12 MIS']
    o=[]
    for i in range(len(a)):

        o.append([j[i],k[i],l[i]])
    z=[]

    for i in o:
         for j in i:
                z.append(j)

    # code for Failures

    j1 = d['Failures 1 MIS']
    k1 = d['Failures 3MIS']
    l1 = d['Failures 12 MIS']
    o1 = []
    for i in range(len(a)):
        o1.append([j1[i], k1[i], l1[i]])
    z1 = []

    for i in o1:
        for j in i:
            z1.append(j)

    # code for Fleet

    j2 = d['Fleet 1 MIS']
    k2 = d['Fleet 3 MIS']
    l2 = d['Fleet 12 MIS']
    o2 = []
    for i in range(len(a)):
        o2.append([j2[i], k2[i], l2[i]])
    z2 = []

    for i in o2:
        for j in i:
            z2.append(j)

    # code for Maturity

    j3 = d['Maturity 1MIS']
    k3 = d['Maturity 3MIS']
    l3 = d['Maturity 12 MIS']
    o3 = []
    for i in range(len(a)):
        o3.append([j3[i], k3[i], l3[i]])
    z3 = []

    for i in o3:
        for j in i:
            z3.append(j)

    print(z3)
    # root = ET.Element()
    # tree = ET.ElementTree(root)
    df1 = pd.DataFrame({'Production Month': r, 'MIS TYPE': y, 'PPM': z, "Failures": z1, "Fleet": z2, "Maturity": z3, "MODEL": "Compas ROw"})
    df1 = df1.set_index('Production Month')
    datatoexcel = pd.ExcelWriter('templates/Domastic1.xlsx')
    # b1='xml_files/Domastic1.xlsx'
    output_filename = df1.to_excel(datatoexcel)
    print(output_filename)
    datatoexcel.book.save()
    b=df1.to_html('templates/test.html')

    # output_filename=df1.to_excel("Domatic_Demo.xlsx")
    # tree.write(output_filename, encoding="UTF-8", xml_declaration=True)
    return render_template('xml_file.html',b=df1, er=b)

# @app.route('/download/<filename>', methods=['GET'])
# def download(filename):
#     directory = os.getcwd()
#     return send_from_directory(directory, filename, as_attachment=True)

@app.route('/download')
def download ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "templates/Domastic1.xlsx"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')
