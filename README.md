# IotChatbot



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
  
