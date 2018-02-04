import json

from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

users = json.load(open('users.json'))
print str(users)


@app.route('/')  # Runs at server/
def hello_world():
    return 'Hello, World!'


@app.route('/test')  # Runs at server/test
def test_route():
    return "this was a test"


def user_exists(username, password):
    for user in users:
        login_det = str(user[u'username']) + " : " + str(user[u'password'])
        print "%s : %s" % (username, password)
        print login_det
        if login_det == "%s : %s" % (username, password):
            return True
    return False


@app.route('/login')  # Runs at server/login
def login():
    username = request.args['username']
    password = request.args['password']
    print "login:\t%s:%s" % (username, password)

    if user_exists(username, password):  # Replace with 'user exists' check
        return redirect('https://jamesevickery.github.io/ruhacking?user=%s' % username, code=302)
    else:
        return redirect('https://jamesevickery.github.io/ruhacking/login?error=1')


@app.route('/get-recommended-films')
def get_r():
    un = request.args['username']
    if un == "james":
        return "Monsters, Inc."
    else:
        return jsonify({
            'status': 'bad',
            'error': 'no login'
        })


# Note: You can also return status codes (look them up to see what they mean)


if __name__ == '__main__':
    app.run('0.0.0.0')
