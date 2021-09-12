# Liwa Task Deployment
#------------------------------------------------
## Dependencies:
1. install docker
2. install docker-compose
3. flask == 2.0.1
4. mariadb == 1.0.7

## How to RUN
You do not have to create the database or the table, the docker will create it for you after you enter the following command.

`sudo docker-compose up -d`
* ###Database params 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. user="taha"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. password="password1"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. host="172.19.0.2"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. port=3306

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. database="miniHR"

* ### web application ip
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the web application on the http://127.0.0.1:5000/ , if you want to change that remember to change the ip also in the fetch statements in the javascript files 


