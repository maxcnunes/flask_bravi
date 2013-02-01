# third party imports
from flask.ext.wtf import Form, TextField, TextAreaField, Required


class NewsCreateForm(Form):
	title = TextField('Title', [Required()])
	text = TextAreaField('Text', [Required()])
