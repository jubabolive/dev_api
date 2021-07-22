from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [ #desenvolvedores recebem uma lista de dicionario
    {
            'id':'0',
            'nome': 'Jonatas',
            'habilidades':['Python ', 'Flask']
     },

    {
            'id':1,
            'nome':'Oliveira',
            'habilidades':['Python', 'Django']}

]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELTE'])
def desenvolvedor(id):
    if request.method == 'GET':
            try:
                    #desenvolvedor = desenvolvedores[id]
                response = desenvolvedores[id]
            except IndexError:
                mensagem = 'Desenvolvedor de ID {} nao existe' .format(id)
                response = {'status': 'erro', 'mensagem':mensagem}
                print(desenvolvedor) #retorna a informacao aqui no pycharm
            except Exception:
                    mensagem = 'Erro desconhecido. Procure o administrador da API'
                    response = {'status':'erro', 'mensagem':mensagem}

            return jsonify(response)
            #return jsonify(desenvolvedor) #retorna informacao na pagina
    elif request.method == 'PUT':
            #dados = json.loads(request.data)
            #posicao = len(desenvolvedores)
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)  #return jsonify({'status':'sucesso'})
    elif request.method == 'DELETE':
            desenvolvedores.pop(id)
            return jsonify(desenvolvedores[posicao])
            #v({'status':'sucesso', 'mensagem':'Resgistro Excluido'})

    elif request.method == 'GET':
            return jsonify(desenvolvedores)




#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.load(request.data)  #insercao de dados
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso', 'mensagem':'Registro inserido'})






if __name__ == '__main__':
    app.run(debug = True)
