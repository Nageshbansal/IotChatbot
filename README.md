# ***IoTChatbot***
![image](https://user-images.githubusercontent.com/76246968/127762969-0b0b08ea-84e5-41cd-a843-ae954c220526.png)


## Abstract 
 It is a chatbot which integrates with Iot Devices(home appliances) and show their live status , give commands to change status. 
    
## Networking 
 ### Creation of IoT Network Using MQTT (Message Queuing Telemetry Transport)
   - Established a connection between server and client using Socket programmed in  python.
   - For adding multiple client requires threading and has overhead if we havemany IoT applications.So, we used MQTT protocol which is suitable for IoT network. 
   - We used Paho MQTT module in python library to create clients(sensors and IoT devices).They continuously send their data to their respective topic to the broker in small      time intervals. 
   - This data is then received by flask server which acts as subscriber in this case. MQTT has been implemented in flask with the help of flask-mqtt module in python.
  ![image](https://user-images.githubusercontent.com/76246968/127762697-35ea25c1-0845-4827-a4b0-a41863896f34.png)

## Chatbot
  - We used Flask-python Framework for creating Chatbot and Dashboard
  - We also added auth login system for security measures
  - Sqlite3 act as an database in backend
  - ***Microsoft Azure App services act as Cloud based hosting platform*** 
 
## WORKFLOW
 ### IoT-chatbot Architecture

  ![Screenshot (376)](https://user-images.githubusercontent.com/76246968/127763126-a25261c6-256c-4462-b347-6034bd148757.png)

## Limitation 
  - Currently our broker/server can handle upto 8 clients/Iot devices 

## Future Improvments : 
 - ML model for better User expreince and which can give best suggestions to user by analysing  previous user input.
 - More clients can be connected
 - Raspberry Pi and Sensors usage so that we can deal with realtime data.
 






## Installation
 >By Using Hosted Website 
   - Download the all files from folder [sensors](https://github.com/Nageshbansal/IotChatbot/tree/main/sensors) 
   -  Install Python 
   -  Install Paho-mqtt
      ``` 
      pip install paho-mqtt
      ```
   - Run each files in a seperate terminal 
   
     ```
     python pub_temp.py
     python pub_humidity.py
     python pub_fan.py
     python pub_light.py
     ```
     
   - Open the link [IotChatbot](https://iotchatbot.azurewebsites.net/)
   - Use following credentials
       ```
       Username: test
       Password : 1234 
        ```
>By Using Local Host
   - Downlaod the code as a zip file 
     or clone the repo By using following command in git bash
     ```
      git clone https://github.com/Nageshbansal/IotChatbot.git
      ```
   - create venv (optional)
   - Install required python-packages 
      ```
        pip install -r requirements.txt
      ```
   - Go to Iotchatbot directory in command line and run flask app
      ```
      python app.py
     ```
   - Go to sensors directory and  Run each files in a seperate terminal 
     ```
     python pub_temp.py
     python pub_humidity.py
     python pub_fan.py
     python pub_light.py
     ```
     
   - Open the link in browser 
      ```
        http://127.0.0.1:5000/
       ```
   - Use following credentials
       ```
       Username: test
       Password : 1234 
        ```
  ## TEAM MEMBERS
  1. [Vaishnavi Gupta](https://github.com/vaishnavi-gupta18)
  2. [Nagesh Bansal](https://github.com/Nageshbansal)
  3. [Khushi Kumavat](https://github.com/khushi861)
  4. [Kushagra Agarwal](https://github.com/Kushagra-Agarwal44)
  
  ## MENTORS
  1. [Sanjeev Krishnan R.](https://github.com/SanjeevKrishnan)
  2. [Pradnesh Chavan](https://github.com/theobscuredev)
  
