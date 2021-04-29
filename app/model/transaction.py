from app import db

class Transaction(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Transaction {}>'.format(self.name)