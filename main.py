from flask import Flask, request, render_template
from TransactionGet import tx_get

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
        arr = tx_get(a, b)
        return render_template('index.html', arr=arr, title=title)


if __name__ == '__main__':
    app.run()
