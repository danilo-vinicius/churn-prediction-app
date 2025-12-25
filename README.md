# 🔮 Customer Churn Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://[SEU-LINK-DO-APP-STREAMLIT].streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)

> **Uma aplicação de Machine Learning End-to-End para prever o cancelamento de clientes (Churn) e auxiliar na tomada de decisão estratégica.**

---

## 📸 Demo do Projeto

![Demo do App](assets/demo-churn.gif) 
<img width="1570" height="864" alt="image" src="https://github.com/user-attachments/assets/148a1836-5984-4134-9e93-fe3cc8311ee9" />


---

## 📝 Visão Geral

Este projeto aborda um dos problemas mais críticos para empresas de serviços recorrentes: **a perda de clientes (Churn Rate)**. 

Utilizando dados históricos de uma empresa de telecomunicações, desenvolvi um modelo preditivo capaz de identificar clientes com alto risco de cancelamento. O projeto vai além do modelo, entregando uma interface web interativa (Streamlit) que permite a gestores simularem cenários e tomarem ações preventivas.

### 🎯 Objetivos
- Analisar os principais fatores que levam ao churn.
- Treinar um modelo de Machine Learning (Random Forest) com alta acurácia.
- Disponibilizar o modelo em produção através de uma aplicação Web simples e intuitiva.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes bibliotecas e ferramentas:

* **Linguagem:** Python 3.x
* **Análise de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest)
* **Interface Web:** Streamlit
* **Deploy:** Streamlit Cloud

---

## 🧠 O Modelo

O modelo foi treinado com o dataset **Telco Customer Churn**, contendo mais de 7.000 registros.

### Pipeline de Treinamento:
1.  **Limpeza de Dados:** Tratamento de valores nulos e conversão de tipos (ex: `TotalCharges`).
2.  **Pré-processamento:** One-Hot Encoding para variáveis categóricas (Internet, Contrato, etc.).
3.  **Modelagem:** Testes com algoritmos de classificação, optando pelo **Random Forest** pela sua robustez.
4.  **Avaliação:** O modelo final atingiu uma acurácia de **~79%** nos dados de teste.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação na sua máquina local:

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU-USUARIO/churn-prediction-app.git](https://github.com/SEU-USUARIO/churn-prediction-app.git)
cd churn-prediction-app
```

2. Crie um ambiente virtual (Opcional, mas recomendado)

```Bash
python -m venv venv
```

# No Windows:
```
venv\Scripts\activate
```
# No Mac/Linux:
```
source venv/bin/activate
```
3. Instale as dependências
```Bash

pip install -r requirements.txt
```
4. Execute a aplicação
```Bash

streamlit run app.py
```
O navegador abrirá automaticamente no endereço http://localhost:8501.

📂 Estrutura do Projeto
```
churn-prediction-app/
├── app.py               # Código principal da aplicação Streamlit
├── modelo_churn.pkl     # Modelo treinado salvo
├── colunas_modelo.pkl   # Lista de colunas para garantir integridade
├── requirements.txt     # Lista de bibliotecas necessárias
└── README.md            # Documentação do projeto
```
📊 Resultados e Insights
Contratos Mensais são os maiores preditores de churn. Clientes com contratos de 1 ou 2 anos são muito mais estáveis.

Clientes com Internet Fibra Óptica tendem a cancelar mais, possivelmente devido a custos mais elevados ou concorrência.

Métodos de Pagamento Automático reduzem drasticamente a chance de cancelamento.

✒️ Autor
Danilo Vinícius Data Scientist & BI Specialist
