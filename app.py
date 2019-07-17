from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

orders = []
no = 1

## HTML을 주는 부분
@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   global orders
   global no

   name_receive = request.form['name_give']
   number_receive = request.form['number_give']
   address_receive = request.form['address_give']
   phone_receive = request.form['phone_give']

   order = {}
   order['name'] = name_receive
   order['number'] = number_receive
   order['address'] = address_receive
   order['phone'] = phone_receive
   order['no'] = no
   no = no+1
   orders.append(order)
   return jsonify({'result': 'success'})

## API 역할, 삭제용 route
@app.route('/del', methods=['POST'])
def del_post():
   global orders
   no_receive = request.form['no_give']
   del orders[int(no_receive)-1]
   return jsonify({'result': 'success'})



@app.route('/test', methods=['GET'])
def test_get():
   global name
   return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)