import mysql.connector 
from contextlib import contextmanager


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    
    cursor = connection.cursor(dictionary=True)
    yield cursor
    
    if commit:
        connection.commit()
        
    cursor.close()
    connection.close()
    
def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses 
    
def delete_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
        
def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes)  VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )
        
def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total 
            FROM expenses WHERE expense_date
            BETWEEN %s and %s
            GROUP BY category;''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-10-11")
    # print(expenses)
    
    # insert_expense("2024-10-11", 200, "Food", "Eat Dosa")
    
    # delete_expenses_for_date("2024-10-11")
    
    summary = fetch_expense_summary("2024-08-01", "2024-08-11")
    for record in summary:
        print(record)