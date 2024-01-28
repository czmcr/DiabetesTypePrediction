from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PredictionForm(FlaskForm):
    input_data = TextAreaField('Input Data', validators=[DataRequired()])
    submit = SubmitField('Predict')
