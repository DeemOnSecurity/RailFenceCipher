from fence import *
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    result = ''
    if request.method == 'POST':
        text, key, direction = [r for r in request.form.values()]
        if direction == 'encode':
            result = encode(text, int(key))
        else:
            result = decode(text, int(key))
    return render_template('form.html', result=result)


if __name__ == "__main__":
    app.debug = True
    app.run()
