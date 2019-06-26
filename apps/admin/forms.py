import wtforms


class LoginForm(wtforms.Form):
    email = wtforms.StringField(
        'Email Address', [
            wtforms.validators.Length(min=6, max=35),
            wtforms.validators.DataRequired()
        ])
    password = wtforms.PasswordField(
        'Password', [
            wtforms.validators.Length(min=6, max=16),
            wtforms.validators.DataRequired()
        ])


class ForgotPasswordForm(wtforms.Form):
    email = wtforms.StringField(
        'Email Address', [
            wtforms.validators.Length(min=6, max=35),
            wtforms.validators.DataRequired()
        ])


# class UserCreateForm(wtforms.Form):
