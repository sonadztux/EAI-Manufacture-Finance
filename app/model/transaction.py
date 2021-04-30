from app import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    department = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum('Debet', 'Credit'), nullable=False)
    total_amount = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    invoice = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Transaction {}>'.format(self.id)