import mysql.connector
from mysql.connector import errorcode
from randomm import Randomm


class Connect:
    test = 0

    def __init__(self):
        self.test = 0

    def connectMySQL(self):
        try:
            cnx = mysql.connector.connect(
                user='root',
                password='',
                host='127.0.0.1',
                database='doanv2'
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Invalid credential. Unable to access database.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exists')
            else:
                print('Failed to connect to database')
        except:
            print("Unknown error occurred!")
        # insert operation
        try:
            # cursor
            cnxCursor = cnx.cursor()

            query = "INSERT INTO products(Id, HotPid, RecommendedPId, CategoryId, Name,Cover_price," \
                    " Origin_price, Figure, Description, Material, Title, Specifications, Rate) " \
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            # giá trị của một row được cung cấp dưới dạng tuple
            brand = ["Sam sung Galaxy S10", "Sam sung Galaxy S9", "Sam sung Note 9", "Sam sung Galaxy A7",
                     "Sam sung Galaxy A50", "Sam sung Galaxy J7", "Sam sung Galaxy Prime", "Sam sung Galaxy A80",
                     "Sam sung Galaxy Note 8", "Sam sung Galaxy A8", "Sam sung Galaxy A30", "Sam sung Galaxy M20",
                     "Sam sung Galaxy M21"];

            description = ["Mô tả kỹ thuật 1", "Mô tả kỹ thuật 2", "Mô tả kỹ thuật 3", "Mô tả kỹ thuật 4",
                           "Mô tả kỹ thuật 5", "Mô tả kỹ thuật 6", "Mô tả kỹ thuật 7", "Mô tả kỹ thuật 8",
                           "Mô tả kỹ thuật 9", "TMô tả kỹ thuật 10", "Mô tả kỹ thuật 11", "TMô tả kỹ thuật 12",
                           "Mô tả kỹ thuật 13"];
            spec = ["Thông số kỹ thuật 1", "Thông số kỹ thuật 2", "Thông số kỹ thuật 3", "Thông số kỹ thuật 4",
                    "Thông số kỹ thuật 5", "Thông số kỹ thuật 6", "Thông số kỹ thuật 7", "Thông số kỹ thuật 8",
                    "Thông số kỹ thuật 9", "Thông số kỹ thuật 10", "Thông số kỹ thuật 11", "Thông số kỹ thuật 12",
                    "Thông số kỹ thuật 13"];

            rd = Randomm()
            for x in range(1000, 1101):
                brand_rand = rd.ran(0, 13)
                rate = rd.ran(1, 6)
                idP ='SS'+str(x)
                values = (
                    idP, rd.ran(0, 2), rd.ran(0, 2), rd.ran(0, 2), brand[brand_rand],
                    round(rd.ranFloat(100.00, 200.00)),
                    round(rd.ranFloat(100.00, 200.00)), rd.ran(100, 200), description[brand_rand],
                    "Metal", brand[brand_rand], spec[brand_rand], str(rate) +"")

                cnxCursor.execute(query, values)
                cnx.commit()
                # total number of rows inserted
            print("Total rows inserted: %d" % cnxCursor.rowcount)
        except mysql.connector.Error as err:
            print("Error: %s", err)
        except:
            print("Unknown error occurred!")
        finally:
            cnxCursor.close()
            cnx.close()
