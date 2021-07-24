
    

    create table users (username varchar(255), password varchar(255), first_name varchar(255), Last_name varchar(255), email varchar(255), phone_number varchar(255), last_login datetime, api_key varchar(255));
    show tables;
    select * from users;
    alter table users add unique (username, api_key);
    alter table users add primary key (username, api_key);
    truncate users;

    insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) 
    values ('nageshbansal',"1234", 'nagesh', 'bansal', 'nagesh@gmail.com', '22304439', now(), 'abhikuchnhihai');

    insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) 
    values ('test',"1234", 'test', 'test', 'test@gmail.com', '22304439', "11:48", 'abhikuchnhihai');

    create table Devices (username varchar(255),temperature int, humidity int, fan TEXT, light TEXT);
    

    insert into Devices (username, field_name, temperature, humidity, moisture, light)
    values('ROOM', 'nageshbansal', 'ROOM', 45, 54, 100, "ON");

    UPDATE Devices (username,temperature, humidity, fan, light)
    values('test', 'ROOM', 46, 48, 54, "OF");
    
    insert into Devices (username,temperature, humidity, fan, light)
    values('test', 46, 48,"OFF", "OFF");

    select * from Node;

   
  

