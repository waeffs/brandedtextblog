from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class BlogPostForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = SelectField('Category', choices=[('news', 'News'),('business','Business'), ('lifestyle', 'Lifestyle'),('sports','Sports')], validators=[DataRequired()])
    blog_image = FileField('Cover Photo', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('BlogPost')
