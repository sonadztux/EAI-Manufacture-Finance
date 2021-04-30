from app.model.transaction import Transaction

from app import response, app, db
from flask import request


def getAll():
    try:
        transactions = Transaction.query.all()
        data = formatarray(transactions)
        return response.success(data, 'success')
    except Exception as error:
        print(error)


def getDetail(id):
    try:
        transaction = Transaction.query.filter_by(id=id).first()
        if not transaction:
            return response.badRequest([], 'Data not found')
        data = singleObject(transaction)
        return response.success(data, 'success')
    except Exception as error:
        print(error)


def getByDepartment(dept):
    try:
        transactions = Transaction.query.filter_by(department=dept).all()
        data = formatarray(transactions)
        return response.success(data, 'success')
    except Exception as error:
        print(error)

def save():
    try:
        department = request.form.get('department')
        type = request.form.get('type')
        total_amount = request.form.get('total_amount')
        datetime = request.form.get('datetime')
        description = request.form.get('description')
        invoice = request.form.get('invoice')

        transaction = Transaction(department=department, type=type, total_amount=total_amount, datetime=datetime, description=description, invoice=invoice)
        db.session.add(transaction)
        db.session.commit()

        return response.success('', 'Data successfully added')
    except Exception as error:
        print(error)


def update(id):
    try:
        transaction = transaction = Transaction.query.filter_by(id=id).first()
        if not transaction:
            return response.badRequest([], 'Data not found')

        transaction.department = request.form.get('department')
        transaction.type = request.form.get('type')
        transaction.total_amount = request.form.get('total_amount')
        transaction.datetime = request.form.get('datetime')
        transaction.description = request.form.get('description')
        transaction.invoice = request.form.get('invoice')


        db.session.commit()

        data = singleObject(transaction)
        return response.success(data, 'Data successfully updated')
    except Exception as error:
        print(error)


def delete(id):
    try:
        transaction = Transaction.query.filter_by(id=id).first()
        if not transaction:
            return response.badRequest([], 'Data not found')

        db.session.delete(transaction)
        db.session.commit()
        
        return response.success('', 'Data successfully deleted')
    except Exception as error:
        print(error)

def formatarray(datas):
    array = []

    for data in datas:
        array.append(singleObject(data))
    
    return array


def singleObject(data):
    data = {
        'id' : data.id,
        'department' : data.department,
        'type' : data.type,
        'total_amount' : data.total_amount,
        'datetime' : data.datetime,
        'description' : data.description,
        'invoice' : data.invoice
    }
    return data


    