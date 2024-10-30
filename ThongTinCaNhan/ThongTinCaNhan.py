from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def ThongTinCaNhan():
    return render_template('ThongTinCaNhan.html')


if __name__ == '__main__':
    app.run(debug=True)