import json
from datetime import datetime


# to insert the application into the db
def insert(cursor, first_name, last_name, upload_date, upload_cv, email, departmentID, yearsOfExperience, bdate):
    cursor.execute(
        "INSERT INTO usersApplications (first_name,last_name,upload_date,upload_cv,email,departmentID,"
        "yearsOfExperience,bdate) VALUES (?, ?,?, ?,?, ?,?,?)",
        (first_name, last_name, upload_date, upload_cv, email, departmentID, yearsOfExperience, bdate))
    print("inserted", "--------" * 5)


# get all applications
def findAllApplicants(cursor):
    cursor.execute(
        "select ID, first_name,last_name,upload_cv,email,departmentID,yearsOfExperience,bdate from usersApplications "
        "order by upload_date desc")
    # serialize results into JSON
    row_headers = [x[0] for x in cursor.description]
    # fetches all the rows ofa query result
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        # make the data a list of dicts
        json_data.append(dict(zip(row_headers, result)))
    # return the results as str, because the datetime not serializable!
    return json.dumps(json_data, indent=4, sort_keys=True, default=str)


# get the path of the requested cv
def findCvById(cursor, id):
    cursor.execute(
        "select upload_cv from usersApplications where ID=\"" + id + "\"")
    row_headers = [x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    # return the results!
    return json.dumps(json_data, default=str)
