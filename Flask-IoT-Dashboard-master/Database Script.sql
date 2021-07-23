
    
    use ARMS;
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

    create table Devices (deviceID varchar(255), username varchar(255), field_name varchar(255), temperature int, humidity int, moisture int, light TEXT, 
    foreign key (username) references users(username), primary key (deviceID));
    select * from Node;
    select field_name, temperature, humidity, moisture, light from Devices where username="nageshbansal";

    insert into Devices (deviceID, username, field_name, temperature, humidity, moisture, light)
    values('ROOM', 'nageshbansal', 'ROOM', 45, 54, 100, "ON");

    UPDATE Devices (deviceID, username, field_name, temperature, humidity, moisture, light)
    values('ROOM', 'test', 'ROOM', 46, 48, 54, "OF");
    
    insert into Devices (deviceID, username, field_name, temperature, humidity, moisture, light)
    values('ROOM1', 'test', 'ROOM', 46, 48, 54, "OF");

    select * from Node;

   
  

