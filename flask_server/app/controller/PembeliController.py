from app.model.Pembeli import Pembeli
from app.model.Transaksi import Transaksi
from app.model.Transaksi import Transaksi
from app import response, app, db 
from flask import request
from datetime import datetime, timedelta


def index():
    try:
        pembeli = Pembeli.query.all()
        data = formatarray(pembeli)
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
        'id_pembeli': data.id_pembeli,
        'nama_pembeli': data.nama_pembeli,
        'jk': data.jk,
        'no_telp': data.no_telp,
        'alamat': data.alamat,
            }
    return data

def detail(id_pembeli):
    try:
        pembeli = Pembeli.query.filter_by(id_pembeli=id_pembeli).first()
        transaksi  = Transaksi.query.filter(Transaksi.id_pembeli == id_pembeli) 

        if not pembeli:
            return response.badrequest([], "Tidak ada data Pembeli")
        datatransaksi = formatTransaksi(transaksi)
        data = singleDetailPembeli(pembeli, datatransaksi)
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


def singleDetailPembeli(pembeli,transaksi ):
    
    data = {
        'id_pembeli': pembeli.id_pembeli,
        'nama_pembeli': pembeli.nama_pembeli,
        'jk': pembeli.jk,
        'no_telp': pembeli.no_telp,
        'alamat': pembeli.alamat,

        'transaksi' : transaksi

    }
    
    return data


def buatpembeli():
    try:
        id_pembeli       = request.form.get('id_pembeli')
        nama_pembeli     = request.form.get('nama_pembeli')
        jk           = request.form.get('jk')
        no_telp            = request.form.get('no_telp')
        alamat            = request.form.get('alamat')
        #Tampung pada sebuah variable
        savePembeli = Pembeli(id_pembeli=id_pembeli, nama_pembeli = nama_pembeli, jk=jk, no_telp=no_telp, alamat=alamat)
        
        db.session.add(savePembeli)
        db.session.commit()
        
        return response.success('', 'Sukses menambah data Pembeli')
    except Exception as e:
      print(e)
      

def update(id_pembeli):
    try:
        nama_pembeli       = request.form.get('nama_pembeli')
        jk    = request.form.get('jk')
        no_telp       = request.form.get('no_telp')
        alamat    = request.form.get('alamat')
        input = {
            'nama_pembeli'   : nama_pembeli,
            'jk'         : jk,
            'no_telp'          : no_telp,
            'alamat'          : alamat,        
            }
        pembeli = Pembeli.query.filter_by(id_pembeli=id_pembeli).first()
        pembeli.nama_pembeli    = nama_pembeli,
        pembeli.jk = jk,
        pembeli.no_telp    = no_telp,
        pembeli.alamat    = alamat,
        db.session.commit()
        return response.success(input, 'Sukses update data Pembeli')
    except Exception as e:
        print(e)
    
def delete(id_pembeli):
    try:
        pembeli = Pembeli.query.filter_by(id_pembeli=id_pembeli).first()
        if not pembeli:
            return response.badRequest([],'data Pembeli kosong...')
        db.session.delete(pembeli)
        db.session.commit()
        return response.success('','berhasil menghapus data Pembeli')
    except Exception as e:
        print(e)