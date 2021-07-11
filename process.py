from flask import Flask, render_template, request, url_for, jsonify
from numpy.lib.function_base import percentile
from werkzeug.utils import redirect
import test_program


app = Flask(__name__)


test = test_program.Test()

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def process():
    # status = False
    # #question1=' '
    # #question2=' '
    # if request.method =='POST':
    #     question1 = request.form['searchBox1']
    #     question2 = request.form['searchBox2']
    # else:
    #     question1 = request.args.get('searchBox1')
    #     question2 = request.args.get('searchBox2')

    question1 = request.form['question1']
    question2 = request.form['question2']

    print(question1)
    print(question2)
    # percentage = .10
    if (len(question1) != 0 and len(question2) != 0):
        percentage = test.predict(question1=question1, question2=question2)
        if percentage>1:
            percentage = 100
        elif int(percentage*100) == 0:
            percentage = 1
        else:
            percentage = int(percentage*100)
        #percentage = 100 if percentage>1 else int(percentage*100)
        status = True if percentage>50 else False
        print(percentage)
        # percentage = str(percentage) + '%'
        reply=''
        if status:
            reply = 'You are right statements<br>in your mind are <strong>same</strong>'
        else:
            reply = 'Sorry statements<br>in your mind are <strong>not same</strong>'

        return jsonify({'percentage': percentage, 'reply': reply})
    return jsonify({'error': 'Error'})


if __name__ == "__main__":
    app.run(debug=True)
