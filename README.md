# Recomendador de Livros com KNN - ReadNear

Este projeto implementa um sistema de recomendação de livros utilizando o algoritmo **K-Nearest Neighbors (KNN)** com **filtragem colaborativa**. O objetivo é recomendar livros a partir de um título escolhido pelo usuário, utilizando as avaliações de outros usuários para sugerir opções relevantes.

![Dashboad Preview](https://github.com/gxbriellops/books-recomendation/blob/main/Desktop-2025.02.27-14.57.01.01.gif)

## Objetivo do Projeto

O propósito deste projeto é criar um sistema que recomenda livros de forma personalizada. O usuário escolhe um título de livro, e o modelo, com base nas avaliações de outros usuários, sugere outros livros que façam sentido, utilizando técnicas de **filtragem colaborativa**.

## Funcionalidades Principais

- **Recomendação de Livros**: O modelo gera recomendações com base em um título fornecido pelo usuário, utilizando uma **tabela pivot** e o algoritmo **KNN**.
- **Filtragem Colaborativa**: As sugestões são baseadas nas avaliações de outros usuários, identificando padrões de preferência.
- **Algoritmo KNN**: Utiliza o KNN com o parâmetro `"auto"` e a métrica de **similaridade de cosseno** para encontrar livros semelhantes.
- **Entrada de Dados**: Os índices de cada livro são usados como dados de entrada para o modelo.

## Dados Utilizados

O modelo foi construído com base em um banco de dados de avaliações de livros obtido do **Kaggle**. [O link para o dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset/data).

## Tecnologias

O projeto utiliza as seguintes tecnologias e bibliotecas:

- **Python**: Linguagem principal do projeto.
- **pickle**: Para serialização de dados.
- **pandas**: Manipulação de dados e criação da tabela pivot.
- **numpy**: Operações numéricas.
- **sklearn**: Implementação do algoritmo KNN.
- **math (floor)**: Cálculos matemáticos auxiliares.
- **Streamlit**: Construção e deploy do webapp.

## Como Funciona

O sistema é disponibilizado por meio de um **webapp** desenvolvido com **Streamlit**, uma biblioteca amplamente utilizada na área de dados para criar aplicativos interativos de forma simples e com deploy fácil. Para acessar o aplicativo, visite: [read-near.streamlit.app](https://read-near.streamlit.app).

**Nota**: O Streamlit pode hibernar o aplicativo devido a poucos acessos, uma medida para reduzir a carga no servidor. Caso esteja hibernado, seria necessário que eu reative manualmente.

## Status do Projeto

O projeto está **quase finalizado**, faltando apenas pequenos ajustes, como melhorar a exibição das estrelas de avaliação de alguns livros, que ainda não utilizam o melhor parâmetro para essa funcionalidade.

## Instruções de Uso

Usar o recomendador é simples:
1. Acesse o [webapp](https://read-near.streamlit.app).
2. Insira o título de um livro.
3. Veja as recomendações geradas pelo modelo.

**Atenção**: Se o aplicativo estiver hibernado, aguarde alguns minutos para que ele volte a ficar ativo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests** no repositório com sugestões ou melhorias.

## Licença

Este projeto está sob a licença [MIT License](https://opensource.org/licenses/MIT).
