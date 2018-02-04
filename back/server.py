from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/') # Runs at server/
def hello_world():
    return 'Hello, World!'

@app.route('/test') # Runs at server/test
def test_route():
    return "this was a test"

@app.route('/login') # Runs at server/login
def login():
    print('username: ' + request.args['username'])
    print('password: ' + request.args['password'])
    return "done"

@app.route('/get-recommended-films')
def get_r():
    un = request.args['username']
    if un == "james":
        return "Monsters, Inc."
    else:
        return jsonify({
            'status':'bad',
            'error':'no login'
            })

# Note: You can also return status codes (look them up to see what they mean)


if __name__ == '__main__':
    app.run('0.0.0.0')

