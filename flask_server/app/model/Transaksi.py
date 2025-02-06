from app import db
from datetime import datetime
from app.model.Barang import Barang
from app.model.Pembeli import Pembeli
class Transaksi(db.Model):
    id_transaksi = db.Column(db.CHAR(5), primary_key = True)
    id_barang = db.Column(db.Integer,db.ForeignKey(Barang.id_barang, ondelete='CASCADE'))
    id_pembeli = db.Column(db.Integer,db.ForeignKey(Pembeli.id_pembeli, ondelete='CASCADE'))
    tanggal = db.Column(db.DateTime,default=datetime.utcnow)
    keterangan = db.Column(db.VARCHAR(100), nullable=False)
    
    def __repr__(self):
        return '<Transaksi {}>'.format(self.name)