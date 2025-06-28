from flask import Flask, render_template, request, jsonify
from ping3 import ping,verbose_ping

app = Flask(__name__)

@app.route("/",methods=('GET','POST'))
def index():
  data = []
  for i in range(1,256):
    ip = "192.168.1." + str(i)
    response = ping(ip, timeout=0.3)
    if not response == False:
      data.append(ip)
    else:
      continue
  return render_template("index.html",data = data)

if __name__ == "__main__":
  from waitress import serve
  serve(app, host = "0.0.0.0", port=9999)