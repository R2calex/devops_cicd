from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    with app.app_context():
        db.create_all()
except Exception as msg:
    print(msg)


class Myapp(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(500))


@app.route('/')
def home():
    return 'Hi everyone'


@app.route('/insert', methods=['POST'])
def insert():
    c_name = request.form.get("c_name")
    if c_name != '':
        new_c_name = Myapp(c_name=c_name)
        db.session.add(new_c_name)
        db.session.commit()
    return redirect(url_for("index"))


@app.route('/delete/<int:c_id>')
def remove(c_id):
    _obj = Myapp.query.filter_by(c_id=c_id).first_or_404()
    db.session.delete(_obj)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/base')
def index():
    my_lst = Myapp.query.all()
    var = 'Hello this is a variable'
    return render_template('base.html', var_pass=var, my_list=my_lst)


if __name__ == "__main__":
    app.run()
