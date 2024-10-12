# ETL Python SQL

## Descrição do Projeto

Este projeto demonstra minhas habilidades em manipulação de dados com **Python**, **Pandas** e **SQL Server**. O pipeline de ETL (Extração, Transformação e Carga) é implementado utilizando um dataset baixado do Kaggle, onde os dados são tratados e posteriormente, carregados em um banco de dados SQL Server local. Por fim, os dados são extraídos do banco e exportados para um arquivo CSV.

## Estrutura do Projeto

```bash
ETL_PYTHON_SQL
│
├── data
│   ├── processed
│   │   └── order_processed.csv        # Dados processados
│   └── raw
│       └── orders.csv                 # Dados brutos do Kaggle
│
├── notebooks
│   └── retail_orders.ipynb            # Notebook de tratamento de dados
│
├── scripts
│   └── extract_from_db.py             # Script para extrair dados do SQL Server
│
├── venv                               
├── .gitignore                         
├── LICENSE                            # Licença do projeto
├── README.md                          
└── requirements.txt                   # Dependências do projeto
```

## Instalação

### Pré-requisitos
- Python 3.12.4
- SQL Server
- `pip` instalado para gerenciar dependências

### Passos de Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ETL_PYTHON_SQL.git
   cd ETL_PYTHON_SQL
   ```
2. Crie e ative o ambiente virtual:
   ```bash
    python -m venv venv
    source venv/bin/activate        # Para Linux/Mac
    venv\Scripts\activate           # Para Windows
   ```

3. Instale as dependências:
   ```bash
    pip install -r requirements.txt
   ```

4. Configure a conexão com o banco de dados SQL Server no arquivo de script `extract_from_db.py`, adicionando suas credenciais de banco.

## Uso

### 1. Extração de Dados
Os dados são extraídos diretamente do Kaggle e armazenados na pasta `data/raw`. Este processo é feito diretamente no notebook `retail_orders.ipynb`.

### 2. Transformação de Dados
Dentro do notebook `retail_orders.ipynb`, os dados brutos são carregados, tratados e transformados usando a biblioteca Pandas.

### 3. Carga dos Dados no SQL Server
Após o processamento, os dados tratados são carregados em um banco de dados SQL Server local.

### 4. Extração para CSV
O script `scripts/extract_from_db.py` é usado para extrair os dados do banco SQL e gerar o arquivo `order_processed.csv`, que é salvo na pasta `data/processed`.

### Executando o Script
Execute o script de extração da seguinte forma:
```bash
python scripts/extract_from_db.py
```

## Dependências

As principais bibliotecas utilizadas neste projeto estão listadas no arquivo `requirements.txt`. Algumas delas incluem:
- pandas
- sqlalchemy
- pyodbc

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.


