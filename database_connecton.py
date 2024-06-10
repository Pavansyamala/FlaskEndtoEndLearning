import mysql 
import mysql.connector as conn 

class Connection:
    def __init__(self) :
        try :
            self.conn = conn.connect(host = "localhost", user = "root" , password = "" , database = "signupdetails")
            self.cursor = self.conn.cursor()
        except Exception as e :
            print ( " Connection failed !")
        else : 
            print("Connection Was Successfull")
