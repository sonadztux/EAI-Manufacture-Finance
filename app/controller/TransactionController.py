from app.model.transaction import Transaction

from app import response, app, db
from flask import request

def index():
    try:
        transactions = Transaction.query.all()
        data = formatarray(transactions)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))
    
    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name
    }

    return data