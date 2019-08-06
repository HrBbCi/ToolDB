from randomm import Randomm
from connectdb import Connect

class DBB:
    def __init__(self):
        self.test = None
    def toolInsert(self):
        connect = Connect()
        connect.connectMySQL()
if __name__ == '__main__':
    tool = DBB()
    tool.toolInsert()
