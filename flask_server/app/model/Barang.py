from app import db

class Barang(db.Model):
    id_barang = db.Column(db.Integer, primary_key = True)
    name_barang = db.Column(db.VARCHAR(250), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Barangs {}>'.format(self.name)