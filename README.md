# Health Insurance Cross Sell - Classifier

## PORTUGUESE PT-BR VERSION BELOW

# Project

This project aims to analyze a customer base, creating a score based on their behavior and ordering them by propensity to purchase a product.
In this context, the company has a base of health insurance customers, and intends to evaluate within that base customers with a propensity to purchase a new added product, car insurance.

# Metrics

With the wide customer base, the company's commercial department needs to make telephone contacts to offer the new product, however with a limited number of calls, these contacts need to have the highest degree of effectiveness in acquiring these new customers for the new product.
Some emails were previously sent as a form of market research to assess customer interest, and based on the response, the data science team can develop an analysis and a Machine Learning algorithm to effectively reduce errors and increase accuracy in the approach. of the customer.

The strategy designed to solve the problem was to technically follow the data through steps such as:

- Check data consistency (type of variables, check volume of data [duplicates, null or missing]);

- Perform descriptive statistics and outliers;

- Generate a Feature Engineering;

- Exploratory data analysis to evaluate behavior and generate insights;

- Follow the best Features in order of importance;

- Track training and testing data for the Machine Learning model;

- Evaluate the performance metrics of this algorithm;

- Deploy this model on a cloud;

- Use a decision-making tool for the sales team to contact these customers selected based on purchasing propensity.

Among the variables used in commercial research:

- Gender

- Age

- Driving_License

- Region_Code

- Previously_Insured

- Vehicle_Age

- Vehicle_Damage

- Annual_Premium

- Policy_Sales_Channel

- Vintage

- Response

# Tools

The following tools were used for this project:

- Visual Code Studio

- Python v3.10.9

- Virtual Environment

- Data manipulation libraries (Pandas and Numpy)

- Data visualization libraries (Maptplotlib, Seaborn and Scikit plot)

- Model Serialization Library (Pickle)

- Machine Learning Libraries (Scikit Learn)

- Python API for requesting the Machine Learning model

- Render for Machine Learning Model Deployment

- Google Sheets App Script to create the API call using JavaScript

- Google Sheets for request, visualization and model results.

# Insights

After the entire data cleaning stage, Feature Engineering, Feature Selection using an Extra Trees algorithm and monitoring of model testing and training, some results were obtained. The K-Nearst Neighbors, Logistc Regression and Decision Tree models were used to evaluate the data and.

The KNN (K-Nearst Neighbors) Algorithm presented a good gain curve. By approaching 40% of the base, we will have 86% of customers interested in purchasing the new product.
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/knn.png">

However, the Logistic Regression Algorithm, in addition to indicating greater Precision and Recall, by addressing 54% of the base, we will have 100% of interested customers. And to achieve this 100% using KNN, it would be necessary to address the entire base.
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/regression.png">

The Extra Trees Algorithm proved to be as efficient as Logistic Regression, however, due to scalability, project allocation and performance, the RL algorithm was chosen.
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/extra.png">

When deploying the Model using Render Cloud, it was decided to deliver the results obtained from this algorithm through a functional product for the Commercial department and team, thus having viable ways of measuring and obtaining customers more likely to purchase the new product.
This product would be a spreadsheet listing these customers in order of propensity. To do this, an API request was created for Render Cloud using JavaScript integrated into the GoogleSheets Apps Script tool. After this application was carried out, the customer list was created to reach those most likely to join and contract the new service.

In the Google Sheets interface, a button was created to perform the prediction:
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/p1.png">

After clicking on Propensity Score, the 'Score' column of the table will be filled with the score and ordered with the highest propensity

<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/p2.png">


# Final product

The objective of the project is to create an algorithm that has the best performance for ordering a list of customers based on their propensity to purchase products. This algorithm, through the features, generates a score for this propensity, to assist in effective decision making. The Realtime project can be accessed through this [Link](https://docs.google.com/spreadsheets/d/1R-ra8ysxxhgYXOhP0vZPfMHJSp8G0jdK2Slh8lE9xDI/edit#gid=0)



## VERSÃO PORTUGUES PT-BR

# Projeto

Este projeto visa analisar uma base de clientes elaborando um score baseado em seu comportamento e ordenando por propenção de aquição de produto.
Nesse contexto, a empresa possui uma base de clientes de seguro saude, e pretende avaliar dentr/e a base os clientes com propenção para aquisição de um novo produto agregado, seguro de automovel.


# Metricas

Com a ampla base de clientes, o departamento comercial da empresa necessita realizar contatos telefonicos para ofertar o novo produto, porem contando com um numero limitado de ligações, estes contatos precisão ter o maior grau de efetividade para a aquisição desses novos clientes para com o novo produto.
Previamente foi encaminhado alguns emails como forma de pesquisa de mercado para avaliar o interesse dos clientes, e com base na resposta o time de ciência de dados pode elaborar uma analise e um algoritmo de Machine Learning para efetivamente reduzir o erro e aumentar a acertividade na abordagem do cliente.

A estratégia elaborada para resolver o problema foi seguimentar técnicamente os dados por etapas como:

- Verificar a consistencia dos dados (Tipo de variaveis, verificar volumetria de dados [duplicados, nulos ou faltantes];

- Realizar uma estatistica descritiva e outliers;

- Gerar uma Feature Engineering;

- Analise exploratoria de dados para avaliar o comportamento e gerar insights;

- Seguimentar as melhores Features por ordem de importancia;

- Seguimentar dados de treino e teste para o modelo de Machine Learning;

- Avaliar as metricas de performance desse algortimo;

- Realizar o deploy desse modelo em uma cloud;

- Utilizar alguma ferramenta para tomada de decisão do time de comercial para acionar esses clientes selecionados por propenção de compra.

Dentre as variaveis utilizadas na pesquisa comercial:

- Gender

- Age	

- Driving_License	

- Region_Code	

- Previously_Insured
	
- Vehicle_Age	

- Vehicle_Damage	

- Annual_Premium	

- Policy_Sales_Channel
	
- Vintage	Response

 
# Ferramentas

Para este projeto foram utilizados as seguintes ferramentas:

- Visual Code Studio

- Python v3.10.9 

- Virtual Environment

- Bibliotecas de manipulação de dados (Pandas e Numpy)

- Bibliotecas de vizualização de dados (Maptplotlib, Seaborn e Scikit plot )

- Biblioteca de serialização do modelo (Pickle) 

- Bibliotecas de Machine Learning (Scikit Learn)

- API em Python para requisição do modelo de Machine Learning

- Render para Deploy do modelo de Machine Learning

- App Script do Google Sheets para criar a chamada da API usando JavaScript

- Google Sheets para requisição, visualização e resultados do modelo. 

# Insights

Após toda a etapa de limpeza de dados, Feature Engineering, Feature Selection utlizando um algoritmo de Extra Trees e seguimentação de teste e treino do modelo, foram obtidos alguns resultados. Foram utilizados os modelos de K-Nearst Neighbors, Logistc Regression e Decision Tree para avaliar os dados e .

O Algoritmo de KNN (K-Nearst Neighbors) apresentou uma boa curva de ganho. Ao abordar 40% da base teremos 86% dos clientes interessados na aquisição do novo produto.
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/knn.png">

No entanto, o Algoritmo de Logistic Regression alem de indicar um maior Precision e Recall, ao abordar 54% da base, teremos 100% dos clientes interessados. E para alcançar esses 100% utilizando o KNN, seria necessário abordar a totalidade da base. 
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/regression.png">

O Algoritmo de Extra Trees se mostrou tão eficiente quanto a Logistic Regression, no entanto por escalabilidade, alocagem do projeto e performance, foi escolhido o algoritmo de RL.
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/extra.png">

Ao realizar o Deploy do Modelo utilizando o Render Cloud, foi decidido entregar os resultados obtidos desse algoritmo atraves de um produto funcional para o departamento e time de Comercial, assim tendo formas viaveis de mensurar e obter os clientes mais propensos a fazer as aquisição do novo produto. 
Esse produto seria uma planilha com a listagem desses clientes em ordem de propensão. Para isso foi criado uma requisição de API para o Render Cloud utilizando JavaScript integrado a ferramenta de Apps Script do GoogleSheets. Após essa aplicação realizada, a lista de clientes foi criada para alcançar os mais cotados a aderir e contratar o novo serviço.

Na interface do Google Sheets, foi criado um botão para realizar a predição:
<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/p1.png">

Após clicar em Propensity Score, a coluna 'Score' da tabela será preenchida com o score e ordenado com a maior propenção

<img src="https://github.com/erickvieiras/health_insurence_classifier/raw/main/img/p2.png">


# Produto Final

O objetivo do projeto é criar um algoritmo que tenha a melhor permance para ordenar uma lista de clientes com base em sua propenção de aquisição de produtos, compra. Esse algoritmo atraves das features gera um score poara esta propenção, para auxiliar na tomada de decisão efetivamente. O projeto Realtime pode ser acessado através do deste [Link](https://docs.google.com/spreadsheets/d/1R-ra8ysxxhgYXOhP0vZPfMHJSp8G0jdK2Slh8lE9xDI/edit#gid=0)

