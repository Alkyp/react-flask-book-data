from app.model.Transaksi import Transaksi
from app import response, app, db 
from flask import request
from datetime import datetime, timedelta


def index():
    try:
        transaksi = Transaksi.query.all()
        data = formatarray(transaksi)
        return response.success(data, "Success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array


def singleObject(data):
    data = {
        'id_transaksi': data.id_transaksi,
        'id_barang': data.id_barang,
        'id_pembeli': data.id_pembeli,
        'tanggal': data.tanggal,
        'keterangan': data.keterangan,
            }
    return data

def detail(id_transaksi):
    try:
        transaksi = Transaksi.query.filter_by(id_transaksi=id_transaksi).first()
        
        if not transaksi:
            return response.badrequest([], "Tidak ada data Transaksi")
        data = singleDetailTransaksi(transaksi)
        return response.success(data, "Success")
    
    except Exception as e:
        print(e)
        
def singleTransakis(transaksi):
    data = {
        'id_transaksi': transaksi.id_transaksi,
        'id_barang': transaksi.id_barang,
        'id_pembeli': transaksi.id_pembeli,
        'tanggal': transaksi.tanggal,
        'keterangan': transaksi.keterangan,
    }
    
    return data

def formatTransaksi(data):
    array = []
    for i in data:
        array.append(singleTransakis(i))
    return array


def singleDetailTransaksi(transaksi ):
    
    data = {
        'id_transaksi': transaksi.id_transaksi,
        'id_barang': transaksi.id_barang,
        'id_pembeli': transaksi.id_pembeli,
        'tanggal': transaksi.tanggal,
        'keterangan': transaksi.keterangan,

    }
    
    return data


def buatTransaksi():
    try:
        id_transaksi       = request.form.get('id_transaksi')
        id_barang     = request.form.get('id_barang')
        id_pembeli           = request.form.get('id_pembeli')
        tanggal            = request.form.get('tanggal')
        keterangan            = request.form.get('keterangan')
        #Tampung pada sebuah variable
        savetransaksi = Transaksi(id_transaksi=id_transaksi, id_barang = id_barang, id_pembeli=id_pembeli, tanggal=tanggal, keterangan=keterangan)
        
        db.session.add(savetransaksi)
        db.session.commit()
        
        return response.success('', 'Sukses menambah data Transaksi')
    except Exception as e:
      print(e)
      

def update(id_transaksi):
    try:
        id_barang       = request.form.get('id_barang')
        id_pembeli    = request.form.get('id_pembeli')
        tanggal       = request.form.get('tanggal')
        keterangan    = request.form.get('keterangan')
        input = {
            'id_barang'   : id_barang,
            'id_pembeli'         : id_pembeli,
            'tanggal'          : tanggal,
            'keterangan'          : keterangan,        
            }
        transaksi = Transaksi.query.filter_by(id_transaksi=id_transaksi).first()
        transaksi.id_barang    = id_barang,
        transaksi.id_pembeli = id_pembeli,
        transaksi.tanggal    = tanggal,
        transaksi.keterangan    = keterangan,
        db.session.commit()
        return response.success(input, 'Sukses update data Transaksi')
    except Exception as e:
        print(e)
    
def delete(id_transaksi):
    try:
        transaksi = Transaksi.query.filter_by(id_transaksi=id_transaksi).first()
        if not transaksi:
            return response.badRequest([],'data Transaksi kosong...')
        db.session.delete(transaksi)
        db.session.commit()
        return response.success('','berhasil menghapus data transaksi')
    except Exception as e:
        print(e)