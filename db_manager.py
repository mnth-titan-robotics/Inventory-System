import sqlite3


# Does db file exist?
# Yes:
#   Does schema need to be updated?
#       Yes:
#           make new db file of new schema
#           migrate old db to new schema
#           replace old db
#       No:
#           Do nothing
# No:
#   create new db file of latest schema
#   go back to start


class DatabaseManager:
    def __init__(self):
        self.db_file = "TEXPLOSION.db"
        self.db_connection = None
        self.db_cursor = None

        # Standard JSON Syntax
        # "TABLE NAME" : [COLUMN NAME 1, ...]
        self.db_schema = {
            "General Inventory": ["Item Name", "Item Type", "Item Stock", "Item Status"]
        }

        # "Startup" functions
        self._setup_db()
        self._define_db()
    
    def _setup_db(self):
        self.db_connection = sqlite3.connect(self.db_file)
        self.db_cursor = self.db_connection.cursor()

    def _define_db(self):
        for TABLE_NAME in self.db_schema:
            CMD = f"{TABLE_NAME}({",".join(self.db_schema[TABLE_NAME])})".replace(" ", "_")

            self.db_cursor.execute(f"CREATE TABLE {CMD}")