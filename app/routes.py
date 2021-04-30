from app import app
from app.controller import TransactionController

from flask import request

@app.route('/')
def index():
    return 'Hello'

@app.route('/api/finance/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'POST':
        return TransactionController.save()
    return TransactionController.getAll()


@app.route('/api/finance/transactions/<dept>', methods=['GET'])
def transaction_by_dept(dept):
    return TransactionController.getByDepartment(dept)


@app.route('/api/finance/transaction/<id>', methods=['GET', 'PUT', 'DELETE'])
def transaction_detail(id: int):
    if request.method == 'PUT':
        return TransactionController.update(id)
    elif request.method == 'DELETE':
        return TransactionController.delete(id)
    return TransactionController.getDetail(id)