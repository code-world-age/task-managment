from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_db_connection():
    print("This is db connection function")
    db_user = "onkarkodape"
    db_pwd = "i4Sb6uOhFfys"
    db_host = "ep-round-pine-a3wca0wp.il-central-1.aws.neon.tech"
    db_port = "5432"  # Replace with your actual port
    db_name = "python_db"
    db_connection_string = (
        f"postgresql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?sslmode=require"
    )

    return db_connection_string


def get_cursor():
    """Return cursor and connection object."""
    print("****************************************Inside: get_cursor***********************.")
    try:
        connection = db.engine.raw_connection()
        cursor = connection.cursor()
        return cursor, connection
    except Exception as e:
        print("Error from get_cursor- db_function", e)


def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict.

    :param cursor: cursor object
    :return: all rows in a dict format enclosed in a list
    """
    print("Inside dictfetchall.")
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_object(query, cursor, param: list = None):
    """Get object based on param list."""
    print("Inside db function: get_object.")
    try:
        if param:
            cursor.execute(query, param)
        else:
            cursor.execute(query)
        obj_dict = dict_fetch_all(cursor)
    except Exception as e:
        print("Error in executing query from get_object-", e)
        obj_dict = []
    print("get_object:{}".format(obj_dict))
    return obj_dict
