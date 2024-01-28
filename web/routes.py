from flask import Blueprint, render_template, request
from .forms import PredictionForm
from model import preprocess_input, extract_features, predict_diabetes

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = PredictionForm()
    if form.validate_on_submit():
        input_data = form.input_data.data
        preprocessed_data = preprocess_input(input_data)
        features = extract_features(preprocessed_data)
        prediction = predict_diabetes(features)
        return render_template('results.html', prediction=prediction)
    return render_template('index.html', form=form)
