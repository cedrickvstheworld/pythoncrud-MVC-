try:
    from dbconfig import dbcon
except Exception as ex:
    print(ex)


class Db:
    def __init__(self, data):
        self.data = data

    def insertdata(self):
        if any([i == '' for i in self.data]):
            return 'complete the fields dude'
        elif self.data[2] != self.data[3]:
            return 'passwords didn\'t match'
        else:
            xxx = self.checkdbinstance(self.data[0])
            if xxx is False:
                x = dbcon.cursor()
                sql = "INSERT INTO tbluser (username, password, name) VALUES ('%s', '%s', '%s')" \
                      % (self.data[0], self.data[2], self.data[3])
                x.execute(sql)
                dbcon.commit()
                y = self.searchid(self.data[0])
                x.close()
                dbcon.close()
                return True, y
            else:
                return 'username already exists'

    def checkdbinstance(self, username):
        x = dbcon.cursor()
        sql = "SELECT * FROM tbluser WHERE username = '%s'" % username
        x.execute(sql)
        if x.fetchone() is None:
            return False
        else:
            return True

    def searchid(self, username):
        x = dbcon.cursor()
        sql = "SELECT * FROM tbluser WHERE username = '%s'" % username
        x.execute(sql)
        a = x.fetchone()
        return a[3]

    def searchuser(self):
        if any([i == '' for i in self.data]):
            return 'complete the fields dude'
        else:
            x = dbcon.cursor()
            sql = "SELECT * FROM tbluser WHERE person_id = '%s' AND password = '%s'"\
                  % (self.data[0], self.data[1])
            x.execute(sql)
            data = x.fetchone()

            if data is None:
                return 'Username or Password is incorrect'
            else:
                return True, data

    def updateinfos(self):
        if any([i == '' for i in self.data]):
            return 'complete the fields dude'
        elif self.data[2] != self.data[3]:
            return 'passwords didn\'t match'
        else:
            x = dbcon.cursor()
            sql = "UPDATE tbluser SET username = '%s', password = '%s', name = '%s'" \
                  % (self.data[0], self.data[2], self.data[3])
            x.execute(sql)
            dbcon.commit()
            x.close()
            dbcon.close()
            return True
