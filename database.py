import sqlite3
from datetime import datetime

DATABASE_NAME = "prompts.db"


class PromptDatabase:

    def __init__(self):
        self.create_table()

    def connect(self):
        return sqlite3.connect(DATABASE_NAME)

    def create_table(self):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            role TEXT,

            task TEXT,

            output_format TEXT,

            examples TEXT,

            prompt TEXT,

            score INTEGER,

            created_at TEXT

        )
        """)

        conn.commit()

        conn.close()

    def save_prompt(
            self,
            role,
            task,
            output_format,
            examples,
            prompt,
            score
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO prompts(

            role,
            task,
            output_format,
            examples,
            prompt,
            score,
            created_at

        )

        VALUES(?,?,?,?,?,?,?)

        """,

        (

            role,
            task,
            output_format,
            examples,
            prompt,
            score,
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        ))

        conn.commit()

        conn.close()

    def get_all_prompts(self):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT
            id,
            role,
            task,
            output_format,
            score,
            created_at

        FROM prompts

        ORDER BY id DESC

        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

    def delete_prompt(self, prompt_id):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            "DELETE FROM prompts WHERE id=?",

            (prompt_id,)

        )

        conn.commit()

        conn.close()