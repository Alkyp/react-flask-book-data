from app.model.Barang import Barang
from app.model.Transaksi import Transaksi
from app.model.Transaksi import Transaksi
from app import response, app, db 
from flask import request
from datetime import datetime, timedelta


def index():
    try:
        barang = Barang.query.all()
        data = formatarray(barang)
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
        'id_barang': data.id_barang,
        'name_barang': data.name_barang,
        'harga': data.harga,
        'stok': data.stok,
            }
    return data

def detail(id_barang):
    try:
        barang = Barang.query.filter_by(id_barang=id_barang).first()
        transaksi  = Transaksi.query.filter(Transaksi.id_barang == id_barang) 

        if not barang:
            return response.badrequest([], "Tidak ada data Barang")
        datatransaksi = formatTransaksi(transaksi)
        data = singleDetailBarang(barang, datatransaksi)
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


def singleDetailBarang(barang,transaksi ):
    
    data = {
        'id_barang': barang.id_barang,
        'name_barang': barang.name_barang,
        'harga': barang.harga,
        'stok': barang.stok,

        'transaksi' : transaksi

    }
    
    return data


def buatbarang():
    try:
        id_barang       = request.form.get('id_barang')
        name_barang     = request.form.get('name_barang')
        harga           = request.form.get('harga')
        stok            = request.form.get('stok')
        #Tampung pada sebuah variable
        saveBarang = Barang(id_barang=id_barang, name_barang = name_barang, harga=harga, stok=stok)
        
        db.session.add(saveBarang)
        db.session.commit()
        
        return response.success('', 'Sukses menambah data Barang')
    except Exception as e:
      print(e)
      

def update(id_barang):
    try:
        name_barang       = request.form.get('name_barang')
        harga    = request.form.get('harga')
        stok       = request.form.get('stok')
        input = {
            'name_barang'   : name_barang,
            'harga'         : harga,
            'stok'          : stok,        
            }
        barang = Barang.query.filter_by(id_barang=id_barang).first()
        barang.name_barang    = name_barang,
        barang.harga = harga,
        barang.stok    = stok,
        db.session.commit()
        return response.success(input, 'Sukses update data Barang')
    except Exception as e:
        print(e)
    
def delete(id_barang):
    try:
        barang = Barang.query.filter_by(id_barang=id_barang).first()
        if not barang:
            return response.badRequest([],'data Barang kosong...')
        db.session.delete(barang)
        db.session.commit()
        return response.success('','berhasil menghapus data Barang')
    except Exception as e:
        print(e)