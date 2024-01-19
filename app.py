from flask import Flask, render_template,jsonify,request,send_file
from flask_cors import CORS

import pandas as pd
from io import BytesIO

app = Flask(__name__)

CORS(app)
import os



@app.route('/google', methods=['POST'])
def create_and_save_excel():
    data = request.json  
    if not data:
        return "No data received", 400

    df = pd.DataFrame(data)

    excel_file = BytesIO()
    file_path = 'static/google-data.xlsx'
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    excel_file.seek(0)

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'wb') as f:
        f.write(excel_file.getvalue())


    return jsonify('done')


@app.route('/linkedin', methods=['POST'])
def create_and_save_linkedin():
    data = request.json  
    if not data:
        return "No data received", 400

    df = pd.DataFrame(data)

    excel_file = BytesIO()
    file_path = 'static/linkedin-data.xlsx'
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    excel_file.seek(0)


    if os.path.exists(file_path):
        os.remove(file_path)


    with open(file_path, 'wb') as f:
        f.write(excel_file.getvalue())

    return jsonify('done')

@app.route("/google",methods=['GET'])
def index():
    file_path = 'static/google-data.xlsx'

    if os.path.exists(file_path):
        return send_file(
            file_path,
            as_attachment=True,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    else:
        return jsonify('No Google Data sheet yet')
    

@app.route("/linkedin",methods=['GET'])
def indexLinkedIn():
    file_path = 'static/linkedin-data.xlsx'

    if os.path.exists(file_path):
        return send_file(
            file_path,
            as_attachment=True,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    else:
        return jsonify('No LinkedIn Data sheet yet')


if __name__ == "__main__":
    app.run(debug=True)
