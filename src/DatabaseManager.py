#DatabaseManager.py
import sqlite3 as sl

def does_table_exist(DB_CONNECTION, TABLE_NAME):
   DATA = DB_CONNECTION.cursor() 
   DATA.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (TABLE_NAME,))
   return DATA.fetchone()[0] == 1

class Squire_Data:
    """This class is used to hold all of the Sqlite3 commands for Squire 
        mostly so the Squire.py file stays less messy"""
    def __init__(self):
        self.DATABASE = sl.connect('squire-data.db');
                
        if not does_table_exist(self.DATABASE, "QUOTE"):
            self.DATABASE.execute("""
                CREATE TABLE QUOTE (
                    Id INTEGER PRIMARY KEY,
                    ServerId INTEGER NOT NULL,
                    QuoteText TEXT NOT NULL,
                    AddedByUserId INTEGER NOT NULL
                );
            """)

        if not does_table_exist(self.DATABASE, "ERROR_LOG"):
            self.DATABASE.execute("""
                CREATE TABLE ERROR_LOG (
                    Timestamp TEXT NOT NULL,
                    ServerId INTEGER NOT NULL,
                    CmdSentByUserID INTEGER NOT NULL,
                    ErrorText TEXT NOT NULL,
                    PRIMARY KEY(Timestamp, ServerId, CmdSentByUserId)
                );
            """)

    def addQuote(self, SERVER_ID, USER_ID, QUOTE_TEXT):
        sql = """INSERT INTO QUOTE (ServerId, QuoteText, AddedByUserID)
                 VALUES(?, ?, ?);"""
        self.DATABASE.execute(sql, (SERVER_ID, QUOTE_TEXT, USER_ID))
        self.DATABASE.commit()

    def getQuotes(self, SERVER_ID):
        sql ="""SELECT QuoteText
                FROM QUOTE
                WHERE ServerId=?"""
        quotes = self.DATABASE.execute(sql, (SERVER_ID,))
        return quotes.fetchall()