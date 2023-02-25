from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def homepage():
    return render_template("homepage.html")


@app.route("/autenticar", methods=['POST', 'GET'])    
def autenticar():
    cpf = request.form.get('idcpf')

    a = [int(char) for char in cpf if char.isdigit()]

    if len(a) != 11:
        return "cpf inválido"

    if a == a[::-1]:
        return "cpf inválido"

    for i in range(9, 11):
        value = sum((a[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != a[i]:
            return "cpf inválido"
    return render_template("tela.html")



   

if __name__ =="__main__":
    app.run(debug=True)