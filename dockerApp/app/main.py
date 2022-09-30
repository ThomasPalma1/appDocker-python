from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://thomaspalma:qwerty-thomas@192.168.43.153/appDocker'
db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employee'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name


db.create_all()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = (request.form.get("name"))

        if name:
            f = Employee(name)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("index"))


@app.route("/employees_list")
def employees_list():
    employees = Employee.query.all()

    return render_template("list.html", employees=employees)


@app.route("/delete/<int:id>")
def delete(id):
    employee = Employee.query.filter_by(_id=id).first()
    db.session.delete(employee)
    db.session.commit()

    employees = Employee.query.all()

    return redirect("/employees_list")
    # return render_template("list.html", employees=employees)


def redirect_user():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
