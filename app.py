from flask import Flask, render_template, request
import opencc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['input_text']
    cc = opencc.OpenCC('s2t')
    output_text = cc.convert(input_text)
    return render_template('index.html', output_text=output_text)

if __name__ == '__main__':
    app.run(port=8080)
