# API de Predição com Flask e Modelo de Machine Learning  

Este repositório contém uma API desenvolvida em Flask para realizar previsões utilizando um modelo de machine learning previamente treinado.  

## 📌 Funcionalidades  
- 📥 Recebe dados via requisições `POST` no endpoint `/predict`  
- 🔄 Converte os dados recebidos em um `DataFrame`  
- 🤖 Realiza predições usando um modelo carregado (`Modelo_treinado.pkl`)  
- 📤 Retorna os resultados em formato `JSON`  

## 🛠 Tecnologias Utilizadas  
- [Flask](https://flask.palletsprojects.com/)  
- [Pandas](https://pandas.pydata.org/)  
- [NumPy](https://numpy.org/)  
- [Joblib](https://joblib.readthedocs.io/)  

## 🚀 Como Executar  

### 1️⃣ Instale as dependências necessárias  
```bash
pip install flask pandas numpy joblib
