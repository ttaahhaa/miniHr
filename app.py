from datetime import datetime
import os.path

import flask
from flask import Flask, Response, request, jsonify, send_file
from werkzeug.utils import secure_filename
import json
from database import database_connection
from database.database_models import insert, findAllApplicants, findCvById
from utils.helper import get_file, root_dir

app = Flask(__name__)
# uploaded_dir to save the path from root of file system to media.
# the root_dir() function exist in the helper file in the utils package
app.config['upload_dir'] = os.path.join(root_dir(), 'media')
# create upload_dir to config if not exist
if not os.path.exists(app.config['upload_dir']):
    os.makedirs(app.config['upload_dir'])


# download the cv file to the client device
@app.route("/hr/<id>")
def download_file(id=1):
    try:
        # connect to the database
        conn = database_connection.db_driver()
        # if connection alive
        if conn:
            # get the cv path from db based on the cv clicked on the client machine
            data = findCvById(conn.cursor(), id)
            # slicing the path from returned data from db e.g. /home/taha/Documents/liwa/media/Exchanging_books.docx
            reqCvPath = data[16:-3]
            # return the file to the client
            return send_file(reqCvPath, as_attachment=True)

    except Exception as e:
        res = jsonify({"message": "Failed to connect to database."})
        res.status_code = 500
        return res
    finally:
        conn.close()


# route for applicant portal
@app.route('/applicant', methods=['GET'])
def applicant():
    # get_file function is in the helper function to read the file
    content = get_file('templates/applicant.html')
    # response with the html file
    return Response(content, mimetype="text/html")


# route for hr agent portal
@app.route('/hr', methods=['GET'])
def get_hr_Page():
    # get_file function is in the helper function to read the file
    content = get_file('templates/hr.html')
    return Response(content, mimetype="text/html")


# when the hr tried to show the applications
@app.route('/data', methods=['GET'])
def getData():
    # check if the user is the admin based on the header sent
    if flask.request.headers["X-Admin"] == "1":
        try:
            conn = database_connection.db_driver()
            if conn:
                # get all applications
                data = findAllApplicants(conn.cursor())
                # convert the str to json
                res = jsonify(data)
                # status code OK
                res.status_code = 200
                # return the data and the status code
                return res
        except Exception as e:
            res = jsonify({"message": "Failed to connect to database."})
            res.status_code = 500
            return res
        finally:
            conn.close()
    else:
        # if the header not equals to 1, the user will not be authntic to get the data
        res = jsonify({"message": "You are not authentic to enter"})
        res.status_code = 401
        return res


# return the home page
@app.route('/', methods=['GET'])
def home():
    # get_file function is in the helper function to read the file
    content = get_file('templates/root.html')
    return Response(content, mimetype="text/html")


# when user apply for the job
@app.route('/postApplication', methods=['POST'])
def postApplication():
    conn = database_connection.db_driver()
    if conn:
        # another authntication level of the file types. (The first layer exist in the javascript)
        ALLOWED_EXTENTIONS = [".pdf", ".PDF", "docx", "DOCX"]
        # get the data send from the body
        first_name = request.form['firstName']
        last_name = request.form["lastName"]
        email = request.form["email"]
        years_of_experience = request.form["yearsOfExperience"]
        department = request.form["department"]
        bdate = request.form["bdate"]
        cv = request.files["cv"]
        # to safely name the file
        file_name = os.path.join(app.config['upload_dir'], secure_filename(cv.filename))
        # check the file uploaded type
        if cv and file_name[-4:] in ALLOWED_EXTENTIONS:
            # save the cv into media folder
            cv.save(file_name)
            # insert the allication into the database using isert function in the database_models python file in the database package
            insert(conn.cursor(), first_name, last_name, datetime.now(), file_name, email, department,
                   years_of_experience, bdate)
            conn.commit()
            # if the application added successfully
            res = jsonify({"message": "application submitted successfully"})
            res.status_code = 201
            return res
        res = jsonify({"message": "You have to upload a pdf or docx file."})
        res.status_code = 400
        return res
    res = jsonify({"message": "Failed to connect to database."})
    res.status_code = 500
    return res


if __name__ == '__main__':
    app.run(debug=True)
