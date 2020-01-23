import wtforms
from wtforms import validators
from models import User, Snippet
from flask_wtf import HiddenField
import g

from app import app

class CSRFMixin(object):
    @staticmethod
    @app.before_request
    def add_csrf():
        self._csrf_token = HiddenField(default=g._csrf_token)

class LoginForm(wtforms.Form, CSRFMixin):
    email = wtforms.StringField("Email", validators=[validators.DataRequired()])
    password = wtforms.PasswordField("Password", validators=[validators.DataRequired()])
    remember_me = wtforms.BooleanField("Remember me?", default=True)

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        self.user = User.is_authenticated(self.email.data, self.password.data)
        if not self.user:
            self.email.errors.append("Invalid email or password.")
            return False

        return True

class SnippetForm(wtforms.Form):
    title = wtforms.StringField('Title', validators=[DataRequired()])
    body = wtforms.TextAreaField('Body', validators=[DataRequired()])
    status = wtforms.SelectField('Entry status', 
                           choices=(
                               (Snippet.STATUS_PUBLIC, 'Public'),
                               (Snippet.STATUS_DRAFT, 'Draft')
                           ), coerce=int)

    def save_entry(self, entry):
        self.populate_obj(entry)
        entry.generate_slug()
        return entry