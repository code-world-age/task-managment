from flask import request
from flask import (
    jsonify,
    make_response
)
from src.___init__ import app
from src.utils.db_function import get_cursor,get_object



@app.route("/user",methods = ['GET'])
def hello():
    cursor, connection = get_cursor()
    print("Inside To get basic set up details")
    try:
        if request.method == 'GET':
            query = """ select * from api.api_user """
            user_details = get_object(
                query=query,
                cursor=cursor
            )
            return make_response(jsonify(user_details))
    except Exception as e:
        print(e)
