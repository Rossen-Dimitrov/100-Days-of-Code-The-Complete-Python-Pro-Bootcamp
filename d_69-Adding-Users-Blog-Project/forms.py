from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields import PasswordField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=5)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    name = StringField(label='Name', validators=[DataRequired(), Length(min=3)])
    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=5)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(label='Log In')


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
