from flask import Flask, request, jsonify
import string
import random
import re

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return 'A API está online'

@app.route("/criarsenha")
def gerador_de_senhas():
    comprimento = int(request.args.get('comprimento', 16))
    senha = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(comprimento))
    return senha

@app.route("/verificarsenha")
def verificador_de_senha():
    senha = request.args.get('senha')
    
    if len(senha) < 16:
        return jsonify({"valido": False, "mensagem": "A senha deve ter pelo menos 16 caracteres."})
    if not re.search(r'[A-Z]', senha):
        return jsonify({"valido": False, "mensagem": "A senha deve conter pelo menos uma Letra maiuscula."})
    if not re.search(r'[a-z]', senha):
        return jsonify({"valido": False, "mensagem": "A senha deve conter pelo menos uma Letra minuscula."})
    if not re.search(r'\d', senha):
        return jsonify({"valido": False, "mensagem": "A senha deve conter pelo menos um digito."})
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return jsonify({"valido": False, "mensagem": 'A senha deve conter pelo menos um caracter especial.'})
    
    return jsonify({"valido": True, "mensagem": "A senha atende a todos os requisitos."})

@app.route("/criarsenha/<usuario>/<senha>")
def criar_senha(usuario, senha):
    senhas[usuario] = senha
    return f'senha criada para o usuario {usuario}'

@app.route("/obtersenha/<usuario>")
def obter_senha(usuario):
    if usuario in senhas:
        return f'senha do usuario {usuario}: {senhas[usuario]}'
    else:
        return f'usuario {usuario} não encontrado'
    
if __name__ == '__main__':
    app.run(debug=True)