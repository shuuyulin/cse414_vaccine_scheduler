import sys
sys.path.append("../db/*")
from datetime import datetime
from db.SQLs import *
from db.ConnectionManager import ConnectionManager
import pymssql

def execute_sql_command(sql_command: str, params: tuple = (), fetch: bool = False) -> any:
    """
    Executes an SQL command with proper connection management and error handling.

    Args:
        sql_command (str): The SQL command to execute.
        params (tuple): Parameters to pass to the SQL command.
        fetch (bool): Whether to fetch results from the query.

    Returns:
        any: Query results if `fetch` is True; None otherwise.
    """
    cm = ConnectionManager()
    conn = cm.create_connection()
    cursor = conn.cursor(as_dict=True if fetch else False)
    try:
        cursor.execute(sql_command, params)
        if fetch:
            return list(cursor)
        else:
            conn.commit()
    except pymssql.Error as e:
        print("Database error occurred:", e)
        raise
    except Exception as e:
        print("An error occurred:", e)
        raise
    finally:
        cm.close_connection()

# Refactored functions using execute_sql_command

def username_exists_caregiver(username: str) -> bool:
    result = execute_sql_command(select_Cusername_details, (username,), fetch=True)
    return len(result) > 0 and result[0]['Username'] is not None

def username_exists_patient(username: str) -> bool:
    result = execute_sql_command(select_Pusername_details, (username,), fetch=True)
    return len(result) > 0 and result[0]['Username'] is not None

def get_caregiver_by_name(username: str) -> list[str, str]:
    result = execute_sql_command(get_caregiver_details, (username,), fetch=True)
    return list(result[0]) if result else None

def get_patient_by_name(username: str) -> list[str, str]:
    result = execute_sql_command(get_patient_details, (username,), fetch=True)
    return list(result[0]) if result else None

def get_doses_by_vaccine_name(vaccine_name: str) -> int:
    sql_command = "SELECT Name, Doses FROM Vaccines WHERE Name = %s"
    result = execute_sql_command(sql_command, (vaccine_name,), fetch=True)
    return result[0]['Doses'] if result else None

def insert_patient(*args) -> None:
    sql_command = "INSERT INTO Patients VALUES (%s, %s, %s)"
    execute_sql_command(sql_command, args)

def insert_caregiver(*args) -> None:
    sql_command = "INSERT INTO Caregivers VALUES (%s, %s, %s)"
    execute_sql_command(sql_command, args)

def insert_vaccine(*args) -> None:
    sql_command = "INSERT INTO Vaccine VALUES (%s, %d)"
    execute_sql_command(sql_command, args)

def update_vaccine(*args) -> None:
    sql_command = "UPDATE vaccines SET Doses = %d WHERE name = %s"
    execute_sql_command(sql_command, args)

def insert_availabilities(*args) -> None:
    sql_command = "INSERT INTO Availabilities VALUES (%s , %s)"
    execute_sql_command(sql_command, args)

def insert_reservation(*args) -> int:
    sql_command = "INSERT INTO Reservations(Time, Cusername, Pusername, Vname) VALUES (%s, %s, %s, %s)"
    result = execute_sql_command(sql_command, args)
    
    # For fetching the last inserted ID
    return result.lastrowid if hasattr(result, 'lastrowid') else None

def search_caregiver_schedule(date: datetime) -> list[list]:
    result = execute_sql_command(search_caregiver_details, (date,), fetch=True)
    return list(result)

def search_doses(date: datetime) -> list[list]:
    result = execute_sql_command(search_doses_details, (date,), fetch=True)
    return list(result)

def make_reservation(date: datetime) -> list[list]:
    result = execute_sql_command(search_doses_details, (date,), fetch=True)
    return [[row['Name'], row['Doses']] for row in result]

def show_appointment(sql_command: str, username: str) -> list[list]:
    result = execute_sql_command(sql_command, (username,), fetch=True)
    return list(result)