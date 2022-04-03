from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


# td.title {
#     background-color: "#dddddd";
#     align: "center";
#     font-size: 14pt;
#     padding: 5px;
# }
# td.ordinary {
#     background-color: "#eeeeff";
#     align: "center";
#     font-size: 14pt;
#     padding: 5px;
# }
# h4 {
#     color: #cccccc;
#     padding: 20px;
# }
# p {
#     font-size: 14pt;
# }