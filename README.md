# Apache Airflow Project

Este projeto utiliza [Apache Airflow](https://airflow.apache.org/) para orquestração de workflows de dados.

## Pré-requisitos

- Python 3.7+
- Apache Airflow
- Docker (opcional)

## Instalação

```bash
pip install apache-airflow
```

## Estrutura do Projeto

```
.
├── dags/
│   └── exemplo_dag.py
├── requirements.txt
└── README.md
```

## Como iniciar o Airflow

```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
airflow webserver --port 8080
airflow scheduler
```

## Como adicionar novas DAGs

Coloque seus arquivos `.py` na pasta `dags/`.

# Uso com docker no windows

Para utilizar o airflow com o windows, primeiramente baixe o arquivo .yml do curl abaixo

    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'

Em seguida, execute o comando 

    docker-compose up -d

 Para criar um usuario inicial use o seguinte comando.

    docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin



## Licença

Este projeto está sob a licença MIT.