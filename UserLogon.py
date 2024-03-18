from flask import Flask, request, jsonify, send_file, redirect
import pwd
import grp
app = Flask(__name__)

USERNAME = 'test'
PASSWORD = 'abcABC123'

def authenticate():
	auth = request.authorization
	if not auth or auth.username != USERNAME or auth.password != PASSWORD:
		return False
	return True

@app.route('/api/users', methods = ['POST'])
def users(): 
	if rquest.method != 'POST':
		return jsonify({'error': 'Method Not Allowed'}), 405
	if not authenticate():
		return jsonify({'error': 'Unauthorized access1111'}), 401
	user_info = {}
	for user in pwd.getpwall():
		users_info[str(user.pw_uid)] = user.pw_name
	return jsonify(users_info)

@app.route('/api/groups', methods = ['POST'])
def groups(): 
	if request.method != 'POST':
		return jsonify({'error': 'Method Not Allowed'}), 405
	if not authenticate():
		return jsonify({'error': 'Unauthorized access2222'}), 401
	groups_info = {}
	for group in grp.getgrall():
		groups_info[str(group.gr_gid)] = group.gr_name
	return jsonify(groups_info)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 3000)
@app.route('/')
def index():
	return send file('index.html')
if_name_=='_main_':
	app.run(host='10.0.2.15',port=3000)

