import sqlite3


class db:

    def __init__(self):
        try:
            self.db = sqlite3.connect("user.sqlite")
            self.cursor = self.db.cursor()
            print('[result] Database connected!')

        except Exception as e:
            print('[error] error connecting database!')
            print(e)

    def user(self, username, api):
        try:
            query = "select * from users where username='{}' and api_key='{}'".format(
                username, api)
            self.cursor.execute(query)
            output = self.cursor.fetchall()
            return output[0]
        except Exception as e:
            print('[error] ' + e)

    def add_user(self, username, password, first_name, last_name, email, phone_number):

        checkusername = self.cursor.execute(
            "SELECT username FROM users WHERE username=?", (username,))
        if checkusername is None:

            try:

                query = "insert into users (username, password, first_name, last_name, email, phone_number, last_login, api_key) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', now(), '{6}');".format(
                    username, password, first_name, last_name, email, phone_number, "api_key")
                # print(query)
                self.cursor.execute(query)
                self.db.commit()
                return True
            except Exception as e:
                print(e)
        else:
            return "USERNAME already exists"

    def update_values(self, apikey, fieldname, deviceID, temp, humidity, moisture, light):
        try:
            self.cursor.execute("select api_key from users;")
            output = self.cursor.fetchall()
            dummy = []
            for i in output:
                dummy.append(i[0])
            if apikey in dummy:

                query = 'insert into {0} (deviceID, temperature, humidity, moisture, light, date_time) values("{1}", {2}, {3}, {4}, {5}, now());'.format(
                    fieldname, deviceID, temp, humidity, moisture, light)
                self.cursor.execute(query)
                self.db.commit()

                query = 'update Node set temperature={0}, humidity={1}, moisture = {2}, light={3} where deviceID="{4}";'.format(
                    temp, humidity, moisture, light, deviceID)
                self.cursor.execute(query)
                self.db.commit()

                return True

            else:
                print("not available")

        except Exception as e:
            print("[ERROR!]")
            print(e)
