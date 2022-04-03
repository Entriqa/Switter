from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.login_form import LoginForm
from data.register import RegisterForm
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'switterry_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
    return render_template('register.html', tittle='Registration', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
    db_sess = db_session.create_session()
    form = LoginForm()
    if form.validate_on_submit():
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('index.html', message="Wrong login or password", form=form)
    return render_template('index.html', title='Authorization', form=form)


# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     return render_template("login.html", title='Switter')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/users.sqlite")
    app.run()


if __name__ == '__main__':
    main()
