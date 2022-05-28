import os
import json

jsonctx = open('repolist.json', 'r+')
loadedjson = json.load(jsonctx)

def addRepo(htli):
    loadedjson["reponame"]["http"] = htli
    jsonctx.seek(0)
    json.dump(loadedjson, jsonctx)
    jsonctx.truncate()
    return 0

def cleandir():
    os.system('./cleandir.sh')
    return 0

def sequence():
    os.system('touch phatballs.sh')
    os.system('echo "#!/bin/bash" > phatballs.sh')
    os.system('echo "cd workdir" >> phatballs.sh')
    os.system('echo "git init" >> phatballs.sh')
    os.system(f'echo "git pull --no-rebase --allow-unrelated-histories https://github.com/{loadedjson["reponame"]["http"]}" >> phatballs.sh')
    os.system('echo "python3 kanjar.py" >> phatballs.sh')
    os.system('chmod +x phatballs.sh')
    os.system('./phatballs.sh')
    return 0

