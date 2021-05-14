from flask import Flask, request, make_response, send_file

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def index():
    return send_file('./static/index.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('./static/favicon.ico')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
