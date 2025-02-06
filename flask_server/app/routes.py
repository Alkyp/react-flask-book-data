from app import app
from flask import render_template, request, jsonify
from app.controller import BarangController, PembeliController, TransaksiController


@app.route("/")
def index():
    return ' hello world'
    #return render_template("main.html")

@app.route("/barang", methods=['GET', 'POST'])
def barang():
    if request.method == 'GET':
        return BarangController.index()
    else:
        return BarangController.save()

@app.route("/barang/<id_barang>", methods=['GET','PUT','DELETE'])
def barangDetail(cust_id):
    if request.method == 'GET':
        return BarangController.detail(cust_id)
    elif request.method == 'PUT':
        return BarangController.update(cust_id)
    else :
        return BarangController.delete(cust_id)


@app.route("/pembeli", methods=['GET', 'POST'])
def pembeli():
    if request.method == 'GET':
        return PembeliController.index()
    else:
        return PembeliController.buatpembeli()

@app.route("/pembeli/<id_pembeli>", methods=['GET','PUT','DELETE'])
def pembeliDetail(vend_id):
    if request.method == 'GET':
        return PembeliController.detail(vend_id)
    elif request.method == 'PUT':
        return PembeliController.update(vend_id)
    else :
        return PembeliController.delete(vend_id)

@app.route("/transaksi", methods=['GET', 'POST'])
def pembeli():
    if request.method == 'GET':
        return TransaksiController.index()
    else:
        return TransaksiController.buatTransaksi()

@app.route("/transaksi/<id_transaksi>", methods=['GET','PUT','DELETE'])
def pembeliDetail(vend_id):
    if request.method == 'GET':
        return TransaksiController.detail(vend_id)
    elif request.method == 'PUT':
        return TransaksiController.update(vend_id)
    else :
        return TransaksiController.delete(vend_id)
