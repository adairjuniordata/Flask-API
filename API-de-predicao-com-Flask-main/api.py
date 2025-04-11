# import bibliotecas
from  flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Instancia do Flask
app = Flask(__name__)

# Carregamento do modelo preditivo salvo
model = joblib.load('Modelo_treinado.pkl')

# Configuração do end point
@app.route('/predict', methods=['POST'])
def repostas_IA():
    # receber os dados em formato JSOn
    data = request.get_json(force=True)

    # converter em data frame
    df = pd.DataFrame([data])

    # tratar esses dados
    df = df.astype(float)

    # faz as predições
    prediction = model.predict(df)

    # Estrutura Json
    output = {
        "prediction" : prediction.tolist() #converta o ndarray em uma lista
    }

    #retornar ao Usuario um Json de Output
    return jsonify(output)


if __name__ == '__main__':
    app.run(host= '127.0.0.1', port='5000')