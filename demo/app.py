import os
import warnings
warnings.filterwarnings('ignore')
import atexit
from flask import Flask, request, jsonify, render_template, redirect, url_for
import csv
import re


app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html')

# @app.route("/sender")
# def sender():
#         main = "/home/user/volepsi/out/build/linux/frontend/frontend"
#         args = " -in /home/user/volepsi/dev/senderData.csv -r 0 -out /home/user/volepsi/dev/out1.csv -csv"
#         command = main + args
#         r_v = os.system(command)
                  
#         return jsonify(
#             status='Running',
#             message='Done',
#             )

# @app.route("/receiver")
# def receiver():
#         main = "/home/user/volepsi/out/build/linux/frontend/frontend"
#         args = " -in /home/user/volepsi/dev/receiverData.csv -r 1 -out res.csv -csv"
#         command = main + args
#         os.system(command)
#         res = []
#         with open('res.csv', 'rb') as csvfile: 
#             csvtext = csvfile.readlines()
#         for line in csvtext:
#             num = re.sub(u"([^\u0030-\u0039])", "", str(line))
#             res.append(num)
                                                                    
#         return jsonify(
#             status='Running',
#             message=res,
#             )

@app.route("/runpsi", methods=["POST"])
def run():
    id = request.form.get("id")
    ip = request.form.get("ip")
    if (request.form.get("mode")=="hybrid"):
         mode = 1
    else:
         mode = 0
    file = request.files['file']
    file.save("files/"+ file.filename)
    # print(id, ip)
    if id == "sender":
        main = "../out/build/linux/frontend/frontend"
        args = " -in files/" + file.filename + " -r 0 -ip " + str(ip) + "-csv -hybrid " + str(mode)
        command = main + args
        try:
            r_v = os.system(command)
            return redirect(url_for('sender_success'))
        except:
            print("Error!")
            return jsonify(status='Error', message='Error!')
    elif id == "receiver":
        main = "../out/build/linux/frontend/frontend"
        args = " -in files/" + file.filename + " -r 1 -ip 0.0.0.0:3001 -out res.csv -csv -hybrid " + str(mode)
        command = main + args
        try:
            os.system(command)
            return redirect(url_for('receiver_success'))
        except:
            print("Error!")
            return jsonify(status='Error', message='Error!')	

@app.route("/sender_success")
def sender_success():
    # file = open("sender_comm.txt", "r")
    # sentBytes = file.readline()
    # receivedBytes = file.readline()

    with open('sender_comm.txt', 'r') as file:
        comm =[int(float(number))
                for line in open('sender_comm.txt', 'r')
                for number in line.split()]
    return render_template('sender_success.html', comm=comm)
     
@app.route("/receiver_success")
def receiver_success():
    res = []
    with open('res.csv', 'rb') as csvfile: 
        csvtext = csvfile.readlines()
    for line in csvtext:
        line = line.rstrip()
        item = str(line.decode())
        # item = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str(line))
        res.append(item)
    
    with open('receiver_comm.txt', 'r') as file:
        comm = [int(float(number))
                for line in file
                for number in line.split()]
         
    return render_template('receiver_success.html', comm=comm, data=res, length=len(res))     

if __name__ == "__main__":
        # app.run(host='0.0.0.0', port=3000, debug=True)
        app.run(host='0.0.0.0', port=3000)
