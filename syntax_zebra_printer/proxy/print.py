import os
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/syntax_zebra_printer/print', methods=['POST'])
def index():
    data_print = request.form['data_print']
    os.system('echo "%s" | lpr -l' % (data_print,))
    out = {'status':'OK'}
    return jsonify(out)
