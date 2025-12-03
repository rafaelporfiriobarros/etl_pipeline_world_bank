# Projeto ETL – Integração e Preparação dos Dados do Banco Mundial

Este projeto tem como objetivo desenvolver um pipeline ETL completo para integrar, padronizar e armazenar dados provenientes do Banco Mundial, combinando indicadores socioeconômicos e informações históricas de projetos financiados pela instituição desde 1947.

## Fontes de Dados

O pipeline integra dados a partir de múltiplas origens heterogêneas:

**1. Indicadores do Banco Mundial**

Conjunto de dados contendo métricas socioeconômicas de países ao redor do mundo (ex.: população, terra arável, dívida do governo central).

**2. Projetos do Banco Mundial**

Dataset composto por informações detalhadas sobre empréstimos, valores financiados e características dos projetos.

---

## Escopo do Pipeline ETL

O fluxo de dados do projeto contempla três etapas principais:

**1. Extração (Extract)**

Coleta de dados a partir de múltiplos formatos e interfaces:

- Arquivos CSV

- Arquivos JSON

- APIs públicas

- Outras fontes estruturadas e semiestruturadas

Cada fonte é lida, validada e registrada para garantir rastreabilidade e reprodutibilidade do processo.

**2. Transformação (Transform)**

Processamento e higienização dos dados para garantir consistência e preparar o dataset final para análises e modelagem. A etapa inclui:

**Integração e Padronização**

- Combinação de dados provenientes de fontes distintas

- Normalização e padronização de colunas

**Limpeza e Qualidade dos Dados**

- Conversão e ajuste de tipos de dados

- Tratamento de datas com diferentes formatos

- Identificação e manejo de codificações variadas

- Tratamento de valores ausentes

- Remoção de registros duplicados

- Criação de variáveis dummies

- Remoção de outliers

- Escalonamento de variáveis conforme necessidade

- Engenharia de atributos relevantes ao modelo preditivo

---

## 3. Carga (Load)

Armazenamento dos dados já transformados em um banco de dados relacional, facilitando consultas, análises e uso posterior em modelos de Machine Learning.

A carga será realizada de maneira estruturada, garantindo que:

- A tabela final contenha os dados consolidados

- As operações sejam idempotentes e auditáveis

- O banco fique preparado para integrações futuras

## Pipeline ETL Integrado

Ao final do projeto, será desenvolvido um módulo Python unificado, responsável por:

1. Ler automaticamente todas as fontes de dados

2. Aplicar todas as transformações descritas

3. Carregar o dataset final no banco de dados, em uma única execução

## Objetivo Final

Unificar os conjuntos de dados do Banco Mundial em uma tabela única e limpa, adequada para análises estatísticas e desenvolvimento de modelos de Machine Learning — incluindo, por exemplo, **a previsão dos custos totais de projetos financiados.**

O projeto demonstra, de ponta a ponta, como construir um pipeline ETL robusto em Engenharia de Dados, lidando com desafios reais como qualidade, padronização, integração e automação de dados.