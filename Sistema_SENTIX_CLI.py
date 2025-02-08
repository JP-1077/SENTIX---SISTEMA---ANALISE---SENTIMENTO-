'''
📌 IMPORTAÇÃO DE BIBLIOTECAS NECESSÁRIAS PARA O DESENVOLVIMENTO DO MODELO CLI.
    🔹 joblib: Essa biblioteca é crucial para carregar modelos de machine learning previamente treinados e salvar objetos em Python.
    🔹 re: Utilizada ára expressões regulares, permitindo manipular e extrair informações de texto de forma eficiente.
'''
import joblib
import re
import sys
import time
from colorama import Fore, Style, init


init(autoreset=True)

# CARREGAMENTO DO MODELO E VETORIZADOR.
    # Aqui iremos importar o modelo que foi desenvolvido (SVM) e o vetorizador (TF - IDF) a partir dos arquivos com a extensão pkl.
model = joblib.load(r'C:\Users\jmend\OneDrive\Documentos\Projetos\Analise Sentimento\Machine Learning\svm_model.pkl')
tfidf = joblib.load(r'C:\Users\jmend\OneDrive\Documentos\Projetos\Analise Sentimento\Machine Learning\tfidf_vectorizer.pkl')

'''
 📌 CRIAÇÃO DA FUNÇÃO CLEAN_TEXT
    Essa função tem o objetivo de pré - processar o texto, preparando - o para a análise e definição de sentimentos. Realizando as seguinte operações:
    🔹 Remove URLs (Links);
    🔹 Remove Menções (@);
    🔹 Remove Hashtags (#);
    🔹 Remove Caracteres Especiais (!, ?, &);
    🔹 Conversão de Maiscula para Minúscula;
'''
def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text) 
    text = re.sub(r"@\w+", "", text) 
    text = re.sub(r"#", "", text) 
    text = re.sub(r"[^\w\s.,!?']", "", text) 
    text = re.sub(r"\s+", " ", text).strip() 
    return text.lower() 

'''
📌 CRIAÇÃO DA FUNÇÃO PREDICT_SENTIMENT
    O objetivo dessa função é capturar tudo aquilo que já foi realizado anteriormente e usar como base para conseguir realizar a predição.    
    🔹Limpeza do texto: Chama a função Clean_Text para processar e realizar a tratativa nos textos.
    🔹Vetorização: Utiliza o Vetor criado (TF-IDF) para transformar o texto que foi limpo em um vetor numérico.
    🔹Predição: Utilizado o modelo SVM treinado e carregado para realizar a predição sobre o vetor transformado
'''
def predict_sentiment(text):
    cleaned_text = clean_text(text)
    vectorized_text = tfidf.transform([cleaned_text])
    predict = model.predict(vectorized_text)
    return "Positivo" if predict[0] == 4 else "Negativo"

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


    print(Fore.GREEN + "\n💬 Digite um texto para análise e descubra seu sentimento!")
    print(Fore.LIGHTBLACK_EX + "(Digite 'sair' para encerrar o sistema.)\n")


type_effect("\n🌟Bem-vindo ao SENTIX - UM SISTEMA DE ANÁLISE DE SENTIMENTO! 🌟")

# Sistema CLI
while True:
    user_input = input(Fore.CYAN + "\n✍🏽 Digite um texto para análise:" + Fore.RESET)
    if user_input.lower() == "sair":
        print(Fore.RED + "\n❌ Encerrando o sistema... Até a próxima! 👋")
        break

    print(Fore.LIGHTBLACK_EX + "🔍 Analisando...", end="")
    time.sleep(1)
    print(Fore.LIGHTBLACK_EX + "✅")

    sentimento = predict_sentiment(user_input)

    if sentimento == "Positivo":
        print(Fore.GREEN + f"✅ Sentimento previsto: {sentimento} 😊")
    else:
        print(Fore.RED + f"❌ Sentimento previsto: {sentimento} 😞")

    print(Fore.LIGHTBLACK_EX + "-" * 60)  # Linha separadora    





