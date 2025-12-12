import sqlite3


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

    def _FETCH(self, command: str) -> list | Exception:
        try:
            self.db_cursor.execute(command)
            return self.db_cursor.fetchall()
        
        except Exception as e:
            return Exception(e)

    def _EXECUTE(self, command: str) -> None:
        self.db_cursor.execute(command)
    
    def _setup_db(self):
        self.db_connection = sqlite3.connect(self.db_file)
        self.db_cursor = self.db_connection.cursor()

    def _define_db(self):
        CMD_QUEUE = []

        # Create SQL Commands from db_schema variable
        for TABLE_NAME in self.db_schema:
            STRUCTURE = {
                "SQL_COMMAND": (f"{TABLE_NAME}({",".join(self.db_schema[TABLE_NAME])})".replace(" ", "_")),
                "TABLE_NAME": (TABLE_NAME),
                "TABLE_COLUMNS": (self.db_schema[TABLE_NAME])
            }

            CMD_QUEUE.append(STRUCTURE)

        # Execute SQL Commands from SQL_QUEUE

        # Main Cases
        # If table exists and needs to be deleted
        # If table does not exist and need to exist
        # If table exists and does exist
        # If table does not exist and needs to be deleted

        # If table needs to add rows which do not exist
        # If table needs to remove rows which do exist
        # If table needs to have rows which do not exist
        # If table needs to add rows which do exist
        # If table needs to remove rows which do not exist