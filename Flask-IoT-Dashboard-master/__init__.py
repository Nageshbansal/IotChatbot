from flask import Flask, render_template, jsonify, redirect, request
import json, database, base64
from random import choice
from datetime import datetime
import person
import os, binascii
import sqlite3
app = Flask(__name__)

logged_in = {}
api_loggers = {}
mydb = database.db()

#test api key aGFja2luZ2lzYWNyaW1lYXNmc2FmZnNhZnNhZmZzYQ==


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        user = person.user(request.form['username'], request.form['password'])
        if user.authenticated:
            user.session_id = str(binascii.b2a_hex(os.urandom(15)))
            logged_in[user.username] = {"object": user}
            return redirect('/overview/{}/{}'.format(request.form['username'], user.session_id))
        else:
            error = "invalid Username or Passowrd"
       
    return render_template('Login.html', error=error)

@app.route('/register',methods=['GET','POST'])
def register():
   if request.method == "POST":
       user = database.db.add_user(
           request.form['username'], request.form['password'], request.form['first_name'], request.form['last_name'], request.form['email'],request.form['phone_number'])




#this link is for the main dashboard of the website
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='HOME - Landing Page')

@app.route('/overview/<string:username>/<string:session>', methods=['GET', 'POST'])
def overview(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,  
            "session" : session
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "Device1"
            }
        ]
        return render_template('overview.html', title='Overview', user=user, devices=devices)
    
    else:
        return redirect('/login')
        

#this part is for the profile view
@app.route('/profile/<string:username>/<string:session>', methods=['GET', 'POST'])
def profile(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            
            "session" : session,
            "firstname": logged_in[username]["object"].first,
            "lastname": logged_in[username]["object"].last,
            "email":logged_in[username]["object"].email,
            "phone":logged_in[username]["object"].phone,
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "ARMS12012"
            }
        ]
        return render_template('profile.html', title='API-Settings', user=user, devices=devices)
    
    else:
        return redirect('/login')


@app.route('/logout/<string:username>/<string:session>', methods=['GET', 'POST'])
def logout(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        logged_in.pop(username)
        # print("logged out")
        return redirect('/')
    else:
        return redirect('/login')



#get all the devices information from the user
@app.route("/api/<string:user>/listdevices", methods=['GET', 'POST'])
def listdevices(user):
    global mydb
    if not(apikey in api_loggers):
        try:
            query = "select username from users where username = '{}'".format(user)
            mydb.cursor.execute(query)
            username = mydb.cursor.fetchall()
            username = username[0][0]
            apiuser = person.user(username, "dummy")
            apiuser.authenticated = True
            devices_list = apiuser.get_devices()
            api_loggers[apikey] = {"object" : apiuser}
            return jsonify(devices_list)
        except Exception as e:
            print (e)
            return jsonify({"data":"Oops Looks like api is not correct"})
    
    else:
        data = api_loggers[apikey]["object"].get_devices()
        return jsonify (data)

randlist = [i for i in range(0, 100)]

@app.route('/api/<string:apikey>/deviceinfo/<string:deviceID>', methods=['GET', 'POST'])
def device_info (apikey, deviceID):
    global api_loggers
    global mydb
    if not(apikey in api_loggers):
        try:
            query = "select username from users where api_key = '{}'".format(apikey)
            mydb.cursor.execute(query)
            username = mydb.cursor.fetchall()
            username = username[0][0]
            apiuser = person.user(username, "dummy")
            apiuser.authenticated = True
            data = apiuser.dev_info(deviceID)
            api_loggers[apikey] = {"object" : apiuser}
            #this part is hard coded so remove after fixing the issue
            data = list(data)
            data[2] = "Rosegarden"
            return jsonify(data)
        except Exception as e:
            print (e)
            return jsonify({"data":"Oops Looks like api is not correct"})
    
    else:
        data = api_loggers[apikey]["object"].dev_info(deviceID)

        #this part is hard coded so remove after fixing the issue
        data = list(data)
        data[2] = "Rosegarden"
        return jsonify (data)



@app.route('/api/<string:user>/update/<string:data>', methods=['GET','POST'])
def update_values(user, data):
    global mydb
    try:
        data = decode(data)
        output = mydb.get_apikeys()
        if apikey in output:
            if (len(data) == 6) and (type(data) is list):
                fieldname = data[0]
                deviceID = data[1]
                temp = data[2]
                humidity = data[3]
                moisture = data[4]
                light = data[5]
                mydb.update_values(apikey, fieldname, deviceID, temp, humidity, moisture, light)
                return ("Values Updated")
            else:
                return "Data Decoding Error!"
        else:
            return "Api key invalid"

    except Exception as e:
        print (e)
        return jsonify({"data":"Oops Looks like api is not correct"})


def get_temperature(user):
    with sqlite3.connect("user.sqlite") as con:
        cur = con.cursor()
        query = "select temperature from Devices where username = '{}'".format(user)
        cur.execute(query)
        randData = choice(randlist)
        temperature = cur.fetchall()
        temp = temperature[0][0] + 0.01*randData
        
        print(temperature)
        return temp

def get_moisture(user):
    
   with sqlite3.connect("user.sqlite") as con:
       cur = con.cursor()
       query = "select moisture from Devices where username = '{}'".format(
           user)
       cur.execute(query)
       randData = choice(randlist)
       moisture = cur.fetchall()
       moist = moisture[0][0] + 0.01*randData
      
       return moist

def get_humidity(user):
    
    with sqlite3.connect("user.sqlite") as con:
       cur = con.cursor()
       query = "select humidity from Devices where username = '{}'".format(
           user)
       cur.execute(query)
       randData = choice(randlist)
       humidity = cur.fetchall()
       hum = humidity[0][0] + 0.01*randData

       return hum

@app.route("/api/<string:apikey>/light", methods=["GET", "POST"])
def get_light(user):
    with sqlite3.connect("user.sqlite") as con:
       cur = con.cursor()
       query = "select light from Devices where username = '{}'".format(
           user)
       cur.execute(query)
      
       light = cur.fetchall()
       li = light[0][0]

       return li


@app.route('/api/<string:user>/data/', methods=['GET', 'POST'])
def data(user):
        temperature = get_temperature(user)
        moisture = get_moisture(user)
        light = get_light(user)
        humidity = get_humidity(user)
        time = datetime.now()
        time = time.strftime("%H:%M:%S")
        response = {"temperature":temperature, "light" :light,"humidity":humidity,"moisture":moisture,"time":time}
        return response


def encode(data):
    data = json.dumps(data)
    message_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return json.loads(message)


if __name__ == "__main__":
    app.run(debug=True)
