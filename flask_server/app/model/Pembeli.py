from app import db

class Pembeli(db.Model):
    id_pembeli = db.Column(db.Integer, primary_key=True)
    nama_pembeli = db.Column(db.VARCHAR(30),nullable=False)
    jk = db.Column(db.CHAR(1), nullable = False )
    no_telp = db.Column(db.CHAR(14), nullable = False )
    alamat = db.Column(db.VARCHAR(50), nullable = False )
   

    def __repr__(self):
        return '<Pembeli {}>'.format(self.name)