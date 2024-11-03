from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Kiểm tra xem email và password có được nhập không
        if not email or not password:
            flash("Vui lòng nhập email và mật khẩu!", "danger")
        elif email == "admin@example.com" and password == "password":
            flash("Đăng nhập thành công!", "success")
            return redirect(url_for('home'))  # Chuyển hướng đến route 'home'
        else:
            flash("Email hoặc mật khẩu không đúng!", "danger")

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
