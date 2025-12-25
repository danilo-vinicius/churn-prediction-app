import streamlit as st
import pandas as pd
import joblib

# ============================================
# 1. CARREGAR A INTELIGÊNCIA (MODELO E DADOS)
# ============================================
# O decorator @st.cache_resource deixa o app rápido (não recarrega o modelo a cada clique)
@st.cache_resource
def carregar_arquivos():
    modelo = joblib.load('modelo_churn.pkl')
    colunas = joblib.load('colunas_modelo.pkl')
    return modelo, colunas

modelo, colunas_modelo = carregar_arquivos()

# ============================================
# 2. ESTRUTURA DO SITE (INTERFACE)
# ============================================
st.set_page_config(page_title="Churn Predictor", page_icon="🔮")

st.title("🔮 Previsão de Cancelamento (Churn)")
st.write("Simulador de Inteligência Artificial para retenção de clientes.")

# Criando um formulário na barra lateral para ficar elegante
st.sidebar.header("📝 Dados do Cliente")

# --- Inputs do Usuário ---
# Vamos focar nos principais inputs. O modelo precisa de todos, 
# então vamos criar valores padrão para os menos importantes ou pedir tudo.
# Aqui vou colocar os críticos para simplificar a demo.

tenure = st.sidebar.slider("Meses de Contrato (Tenure)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Valor Mensal ($)", 0.0, 200.0, 50.0)
total_charges = st.sidebar.number_input("Valor Total Gasto ($)", 0.0, 10000.0, monthly_charges * tenure)

# Inputs Categóricos (Texto)
contract = st.sidebar.selectbox("Tipo de Contrato", ["Month-to-month", "One year", "Two year"])
internet_service = st.sidebar.selectbox("Tipo de Internet", ["DSL", "Fiber optic", "No"])
payment_method = st.sidebar.selectbox("Pagamento", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# Botão para calcular
botao = st.sidebar.button("Calcular Probabilidade")

# ============================================
# 3. O CÉREBRO (LÓGICA DE PREVISÃO)
# ============================================
if botao:
    # 1. Criar um DataFrame com os dados inseridos (exatamente como era o original)
    # Nota: Precisamos passar valores para as outras colunas que não perguntamos
    # Para simplificar, vou assumir "No" para serviços extras nesse exemplo.
    
    dados_entrada = pd.DataFrame({
        'Tenure': [tenure],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges],
        'Contract': [contract],
        'InternetService': [internet_service],
        'PaymentMethod': [payment_method],
        # Colunas extras que o modelo exige (Preenchendo com padrão para não quebrar)
        'SeniorCitizen': [0], 'Partner': ['No'], 'Dependents': ['No'], 
        'PhoneService': ['Yes'], 'MultipleLines': ['No'], 'OnlineSecurity': ['No'],
        'OnlineBackup': ['No'], 'DeviceProtection': ['No'], 'TechSupport': ['No'],
        'StreamingTV': ['No'], 'StreamingMovies': ['No'], 'PaperlessBilling': ['Yes'],
        'gender': ['Male'] 
    })

    # 2. Pré-processamento (A Mágica do "Reindex")
    # Transformamos texto em número igual fizemos no treino
    dados_tratados = pd.get_dummies(dados_entrada)
    
    # GARANTIR que as colunas sejam IGUAIS as do treino
    # Se faltar coluna (ex: o usuário não escolheu "Fiber Optic"), adicionamos com 0
    dados_finais = dados_tratados.reindex(columns=colunas_modelo, fill_value=0)

    # 3. Previsão
    predicao = modelo.predict(dados_finais)
    probabilidade = modelo.predict_proba(dados_finais) # Pega a % de certeza

    # ============================================
    # 4. MOSTRAR RESULTADO
    # ============================================
    col1, col2 = st.columns(2)
    
    chance_churn = probabilidade[0][1] * 100 # Probabilidade de ser 1 (Sair)
    
    if chance_churn > 50:
        st.error(f"🚨 ALERTA: Alto Risco de Cancelamento")
        st.metric("Probabilidade de Saída", f"{chance_churn:.1f}%")
        st.progress(int(chance_churn))
        st.write("Recomendação: Oferecer desconto ou upgrade imediato.")
    else:
        st.success(f"✅ Cliente Seguro")
        st.metric("Probabilidade de Saída", f"{chance_churn:.1f}%")
        st.progress(int(chance_churn))
        st.write("Recomendação: Manter relacionamento padrão.")

    # Mostrar os dados brutos (opcional, bom para debug)
    with st.expander("Ver dados processados pela IA"):
        st.write(dados_finais)