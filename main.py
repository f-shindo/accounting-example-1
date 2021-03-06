from flask import Flask, request, render_template
from GetTransaction import tx_get
import os

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    title = 'ERC20送信のトランザクションハッシュを入力してください'

    if request.method == 'GET':
        arr = ['', '', '', '', '', '', '']
        return render_template('index.html', arr=arr, title=title)
    else:
        a = request.form.get('nw')
        b = request.form.get('list_data')
        arr, is_success = tx_get(a, b)
        return render_template('index.html', arr=arr, is_success = is_success, title=title)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
