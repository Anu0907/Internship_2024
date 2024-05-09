# step 1 - import flask
from flask import Flask, request, render_template
import re

# step 2 - create a flask object __name__ parameter
app = Flask(__name__)

##############################################################
# step 3 - create a route and bind it to some functionality

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']        
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)

@app.route('/validate', methods=['GET','POST'])
def validate():
    if request.method == 'POST':
        email = request.form.get('email')
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return render_template('email_validation.html', email=email, valid=True)
        else:
            return render_template('email_validation.html', email=email, valid=False)
    return render_template("email_validation.html")
##############################################################

# step 4 - run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')