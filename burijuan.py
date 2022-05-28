from flask import Flask
import doThis

app = Flask(__name__)

#gg2ez
@app.route('/')
def hello_world():
	return {"message": "tis but a scratch"}

@app.route('/push/<gituser>/<gitrepo>')
def push(gituser,gitrepo):
	doThis.addRepo(gituser+'/'+gitrepo)
	doThis.cleandir()
	doThis.sequence()
	return {"message": "bna bna"}

if __name__ == '__main__':
    
	app.run(host='0.0.0.0')