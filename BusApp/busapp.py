from flask import Flask, url_for, render_template, redirect, request
from main import login_blueprint
import sqlite3
app=Flask(__name__)
app.register_blueprint(login_blueprint)
@app.route('/datve')
def index():
    return render_template("datve.html")

@app.route('/')
def trang_chu():
    return render_template("home.html")

@app.route('/HomeAdmin')
def home_admin():
    return render_template("homeAd.html")

@app.route('/LoginAdmin')
def login_admin():
    return  render_template("loginAd.html")

@app.route('/ttcanhan')
def tt_ca_nhan():
    return render_template("ThongTinCaNhan.html")

@app.route('/vecuatoi')
def ve_cua_toi():
    data = getVe()
    return render_template("VeCuaToi.html", data = data)

def getVe():
    db_path = 'BusTicketSales/BusApp/data/database.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = 'SELECT Ben_Xe_Di.ten_ben_xe, Ben_Xe_Den.ten_ben_xe, TuyenDuong.khoangCach, LichTrinh.thoiGianDi, Ve.trangThaiVe FROM Ve JOIN  DonHang ON Ve.idDonHang  = DonHang.idDonHang JOIN LichTrinh ON LichTrinh.idLichTrinh = DonHang.idLichTrinh JOIN TuyenDuong ON TuyenDuong.idTuyenDuong = LichTrinh.idTuyenDuong JOIN Ben_Xe AS Ben_Xe_Di ON TuyenDuong.diemDi = Ben_Xe_Di.ben_xe_id JOIN Ben_Xe AS Ben_Xe_Den ON TuyenDuong.diemDen = Ben_Xe_Den.ben_xe_id; '
    cursor.execute(query)
    data = cursor.fetchall()
    return data


@app.route('/ttlienhe')
def tt_lien_he():
    return  render_template("ThongTinLienHe.html")

@app.route('/lichtrinh')
def lich_trinh():
    diemDi = request.args.get("diemDi")
    diemDen = request.args.get("diemDen")
    data = getLichTrinh(diemDi, diemDen)
    return render_template("lichtrinh.html", data = data )

def getLichTrinh(diemDi = None, diemDen = None):
    db_path = 'BusTicketSales/BusApp/data/database.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = 'SELECT  BenXeDi.ten_ben_xe AS ten_diem_di, BenXeDen.ten_ben_xe AS ten_diem_den, TuyenDuong.khoangCach, LichTrinh.thoiGianDi FROM LichTrinh JOIN  TuyenDuong ON LichTrinh.idTuyenDuong = TuyenDuong.idTuyenDuong JOIN Ben_Xe AS BenXeDi ON TuyenDuong.diemDi = BenXeDi.ben_xe_id JOIN Ben_Xe AS BenXeDen ON TuyenDuong.diemDen = BenXeDen.ben_xe_id; '
    cursor.execute(query)
    data = cursor.fetchall()
    if diemDi != None:
        data = [p for p in data if str(p[0]) == str(diemDi)]
    if diemDen != None:
        data = [p for p in data if str(p[1]) == str(diemDen)]
    conn.close()
    return data


bills = [
    {
        "trip_name": "Hanoi - Ho Chi Minh",
        "departure_time": "2024-11-15 08:00",
        "booking_time": "2024-11-01 14:30",
        "total_amount": 500000,
        "status": "Confirmed",
        "cancelable": False,
    },
    {
        "trip_name": "Da Nang - Hue",
        "departure_time": "2024-11-16 10:00",
        "booking_time": "2024-11-01 15:45",
        "total_amount": 200000,
        "status": "Pending",
        "cancelable": True,
    }
]
@app.route('/lshoadon')
def bill_history():
    return render_template("lshoadon.html", bills=bills)

@app.route('/cancel/<int:bill_id>')
def cancel_bill(bill_id):
    # Logic to cancel bill here, updating the status and database as needed
    return redirect(url_for('bill_history'))


if __name__ == '__main__':
    app.run(debug=True)
