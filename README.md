#  🌐 **SENTIX - Um Sistema de Análise de Sentimento**

## **Introdução**

🌟 Bem - vindo ao SENTIX, um sistema CLI de análise de sentimentos desenvolvido para processar textos e classificar suas emoções como positivo e negativo! Este projeto segue uma abordagem baseada em Machine Learning e Processamento de Linguagem Natural (NLP).

---

## 📌 **Visão Geral do Projeto**
Este projeto foi divido em duas etapas principais:

  1️⃣ **`Pipeline de Desenvolvimento do Modelo:`** Constução do modelo de Machine Learning para classificação de sentimentos

  2️⃣ **`Sistema CLI:`** Implementação de um sistema interativo que permite ao usuário inserir textos para análise de sentimentos.

---

## 🚀 **Funcionalidades**

  ✅ **`Análise de Sentimento:`** Baseada em um modelo de aprendizado de máquina (SVM).

  ✅ **`Interface Simples:`** Realizada via linha de comando para fácil de interação.

---

## 📊 1º Etapa - Desenvolvimento do Modelo
A construção do modelo foi realizada utilizando uma sequêcia de etapas:

* **`Coleta de Dados:`** Utilização de um dataset com diversos tweets rotulados com sentimentos positivos e negativos

* **`Pré - Processamento:`** Remoção de Stop Words, Tokenização, Lematização, Normalização e Seleção de Atributos.

* **`Vetorização:`** Conversão de texto em vetores usando TF - IDF.

* **`Treinamento do Modelo:`** Algoritmo SVM para classificação dos sentimentos.

* **`Validação e Testes:`** Avaliação do modelo com métricas de acurácia e entre outros.

O modelo treinado foi salvo utilizando a biblioteca joblib, permitindo sua reutilização na interface CLI.

---

## 📊 2º Etapa - Sistema CLI

O *SENTIX* foi projetado para ser simples e intuitivo. Ao rodar o sistema, o usuário digita um texto, e o programa retorna a classificação de sentimento.

---

## 📂**Estrutura do Projeto**
|- README.MD (Epílogo Projeto)

|- Pipeline_Sentix.ipynb (Notebook que obtém o Pré - Processamento, analises e o modelo criado)

|- Sistema_SENTIX_CLI.py (Sistema desenvolvido em Interface em Linha de Comando)

|- Sistema_SENTIX_CLI.py (Sistema desenvolvido em Interface em Linha de Comando)

