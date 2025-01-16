import os
import random
import traceback

from flask import Blueprint, request

data_route = Blueprint('data', __name__, url_prefix='/data')

@data_route.route('/test', methods=['POST'])
def test():
    try:
        # test = request.form['test']
        print("get request")

        return None
    except Exception as e:
        print(e)
        return 'Error while testing'
