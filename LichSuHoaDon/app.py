from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample bill data
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

@app.route('/')
def bill_history():
    return render_template("lichSuHoaDon.html", bills=bills)

@app.route('/cancel/<int:bill_id>')
def cancel_bill(bill_id):
    # Logic to cancel bill here, updating the status and database as needed
    return redirect(url_for('bill_history'))

if __name__ == '__main__':
    app.run(debug=True)
