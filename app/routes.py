from app import app
from app.controller import TransactionController

@app.route('/')
def index():
    return 'Hello'

@app.route('/finance/transactions', methods=['GET'])
def transactions():
    return TransactionController.index()