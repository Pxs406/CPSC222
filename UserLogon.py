from flask import Flask, request, jsonify
import pwd
import grp
app = Flask(__name__)

USERNAME = "test"
PASSWORD = "abcABC123"

def authenticate():
	auth = request.authorization
	if not auth or auth.username != USERNAME or auth.password!= PASSWORD:
		return False
	return True

@app.route('/api/users', methods = ['GET', 'POST'])
def users(): 
	if not authenticate():
		return jsonify({'error': 'Unauthorized acess1111'}), 401
	
	user.info = {}
	for user in pwd.getpwall():
		users_info[str(user.pw_uid)] = user.pw_name
	return jsonify(users_info)

@app.route('/api/groups', methods = ['GET', 'POST'])
def groups(): 
	if not authenticate():
		return jsonify({'error': 'Unauthorized acess2222'}), 401
	
	groups.info = {}
	for group in grp.getpwall():
		groups_info[str(group.gr_gid)] = group.gr_name
	return jsonify(groups_info)
	
if__name__ == '__main__':
	app.run(host'0.0.0.0', port = 3000)

