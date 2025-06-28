# 🌐 Modern Data Pipeline GCP

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Airflow](https://img.shields.io/badge/Airflow-2.x-blue)
![DBT](https://img.shields.io/badge/DBT-1.9.x-orange)
![GCP](https://img.shields.io/badge/GCP-ready-green)

---

## 📚 Table of Contents

- [🔍 Description](#-description)
- [🚀 Project Overview](#-overview)
    - [🔄 Pipeline Highlights](#-pipeline-highlights)
- [📁 `modern-data-pipeline-gcp` – Project Root](#-modern-data-pipeline-gcptransformations--project-root)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
    - [✅ Prerequisites](#-prerequisites)
    - [⚙️ Local Setup](#️-local-setup)
    - [🧭 Step-by-step guide to create a virtual environment in VS Code](#-step-by-step-guide-to-create-a-virtual-environment-in-vs-code)
    - [⚙️ Install Requirements ](#️-install-requirements)
    - [🚀 How to run the mock models](#-how-to-run-the-mock-models)
    - [🛠️ Additional notes](#️-additional-notes)
- [✅ Testing](#-testing)
- [📡 Monitoring & Logging](#-monitoring--logging)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [🧰 Resources](#-resources)
    - [🧱 DBT](#-dbt)
- [👩‍💻 Author](#-author)

---

## 🔍 Description

A production-grade, modular ETL pipeline built with **Apache Airflow**, integrated with **Google Cloud Platform (GCP)** services and **DBT** for transformation and modeling. This project demonstrates best practices in orchestration, cloud-native development, CI/CD, data quality, and monitoring — all in a real-world data pipeline context.

---

## 🚀 Project Overview

This repository contains an end-to-end ETL workflow designed for scalability, maintainability, and cloud readiness. It showcases how to orchestrate data pipelines using Airflow, enrich and transform data with DBT, and deploy the solution using containerized environments and CI/CD pipelines.

### 🔄 Pipeline Highlights:
- [X] Extracts data from a **PostgreSQL** source
- [X] Enriches it with **exchange rate data** from an external API
- [X] Loads the results to **CSV files** and **Google Sheets**
- [X] Optionally pushes transformed data to **BigQuery**
- [X] Includes **data quality checks** and **logging**
- [ ] Modular structure: `extract`, `transform`, `load`, `validate`, `notify`
- [ ] Uses **Docker + Docker Compose** for local orchestration
- [ ] Ready for deployment on **GCP Cloud Composer** or similar environments

---

## 📁 `modern-data-pipeline-gcp` – Project Root

```
.
├── .venv                               # Virtual environment 
├── logs
├── transformations                     # Data transformation logic
│   ├── .dbt
│   │   ├── users.yml
│   │   └── profiles.yml                # DBT profiles (often symlinked or referenced)
│   ├── analyses
│   ├── data                            # CSV exports
│   │   ├── mock_order_items.csv
│   │   ├── mock_orders.csv
│   │   ├── mock_products.csv
│   │   ├── mock_rates.csv
│   │   └── mock_users.csv
│   ├── logs
│   ├── macros
│   ├── models                          # DBT models
│   │   └── mock
│   │       ├── mock_order_items.sql
│   │       ├── mock_orders.sql
│   │       ├── mock_products.sql
│   │       ├── mock_users.sql
│   │       └── schema.yml
│   ├── scripts                         # Python scripts for pipeline steps
│   │   ├── export_tables.py
│   │   ├── load_exchange_rates.py
│   │   └── push_to_bigquery.py
│   ├── seeds
│   ├── snapshots
│   ├── target
│   ├── tests
│   ├── utils                           # Custom utility functions
|   |   └── quality_checks.py
│   ├── .env
│   ├── .gitignore
│   ├── dbt_project.yml                 # DBT project config
│   ├── README.md
│   ├── requirement-dev.txt             # Python dependencies
│   ├── requirements.txt                # Python dependencies
│   └── run.sh
├── .gitignore
├── LICENSE
└── README.md                           # Project documentation
```

---

## 🛠️ Tech Stack

- 🌀 **Airflow** – DAG orchestration & scheduling

    > Apache Airflow is used to define, schedule, and monitor workflows as Directed Acyclic Graphs (DAGs). Each task (e.g., extract, transform, load) runs in sequence or parallel depending on dependencies. In your pipeline, it can automate running Python scripts for ingestion, transformation, and loading at specific intervals (e.g., daily at 1am).

- 🧱 **DBT** – SQL transformations inside BigQuery
    
    > DBT (Data Build Tool) enables modular, version-controlled data transformations using SQL. It runs inside your warehouse (e.g., BigQuery), letting you build models with dependencies, test logic, and document results. Ideal for transforming raw data into analytics-ready datasets in BigQuery.

- ☁️ **GCP** – BigQuery 📈, Sheets API 📄, Secret Manager 🔐

    > BigQuery: Serverless data warehouse for fast querying and analytics.

    > Google Sheets API: Used to export or update transformed data directly into shared spreadsheets for reporting or stakeholder access.

    > Secret Manager: Securely stores credentials and API keys (e.g., DB passwords, service account tokens) for safe access from scripts or containers.

- 🐳 **Docker** – Containerized development environments

    > Docker ensures consistent, reproducible environments for running your pipeline—locally or in the cloud. It packages dependencies, Python versions, and configuration into a container image, avoiding "works on my machine" issues.

- 🐍 **Python** – Core logic, APIs, transformations
    
    > Python powers the core business logic of the pipeline—API ingestion, data transformation (Pandas or PySpark), error handling, logging, and exporting results. It's also used for integrating with GCP, PostgreSQL, and 3rd-party APIs.

- 🐘 **PostgreSQL** – Source database

    > PostgreSQL is the primary data source for the pipeline. Python scripts connect via SQLAlchemy or psycopg2 to extract records, which are then cleaned and loaded into BigQuery or other destinations.

- 🤖 **CI/CD** – GitHub Actions automation

    > GitHub Actions will enable automated workflows for testing, linting, building, and deploying pipeline components on every code change. You can set up jobs to run Pytest, build Docker images, deploy Airflow DAGs, or validate DBT models on push or pull requests.

---

## 🚀 Quick Start

#### ✅ Prerequisites

- Docker & Docker Compose
- Python 3.9+
- `make` (optional, for using the Makefile)
- GCP account, permissions, CLI tools, credentials.

---

#### ⚙️ Local Setup

- Clone the repo

```
# Clone the repository
git clone https://github.com/CamilaJaviera91/modern-data-pipeline-gcp.git
cd modern-data-pipeline-gcp
```

#### 🧭 Step-by-step guide to create a virtual environment in VS Code

1. Open the command palette
Press `Ctrl + Shift + P` to open the command palette.

2. Select the Python interpreter
Type and select **"Python: Select Interpreter"**.

3. Create a virtual environment

    - Click on "+ Create Virtual Environment..."

    - Choose the environment type: select "Venv"

    - Select the Python version you want to use (e.g., Python 3.10.17)

4. Wait for the virtual environment to be created
VS Code will automatically create a `.venv` folder in your project and configure the environment.

5. Activate the virtual environment
Once it's created, we can activate it.

```
source .venv/bin/activate
```

- (Opcional) If you don't want to create the enviroment in VSCode you can use this script:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 🛠️ Create .env file 

It should contain variables like:

```
DBT_HOST=host
DBT_USER=user_name
DBT_PASSWORD=password
DBT_DBNAME=bd_name
DBT_SCHEMA=schema_name
DBT_PORT=0000
EXCHANGE_API_KEY=000000000000000
GOOGLE_CREDENTIALS_PATH=/your/path/file.json
BQ_PROJECT_ID=id
BQ_DATASET=data_set_name
```

#### 📦 Install Requirements

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

#### 🐘 Start Postgres Services:

```
sudo systemctl start postgresql
```

#### 🆕 Initialize Project

```
dbt init transformations
```

- DBT will ask you a few questions:

    - project name: (you can keep transformations)

    - profile: use the default one, or configure it later

- This will create a transformations/ folder with all the base files.

#### 🚀 How to run the mock models

- To run the models inside the `mock` directory, use the following command:

```
python transformations/scripts/load_exchange_rates.py      # 🔌 loads exchange rates
./run.sh run --select enrich_exchange_rates                # 🛠️ transforms data
```

- This command runs DBT and processes only the models located in the `models/mock` folder.

#### 🛠️ Additional notes

- Make sure you have a `.env` file with the necessary environment variables to connect to the database.

- The `run.sh` script automatically loads these variables and runs DBT with the proper configuration.

- To run all models, simply use:

```
./run.sh run
```

---

## 🧪 Testing

- **DBT tests** for schema, uniqueness, and relationships
- **Airflow DAG validation**: `airflow dags list`, `airflow dags test`
- **Unit tests** for custom Python functions in `/scripts` or `/dags`
- **CI pipeline** (planned): Linting, formatting, DAG validation, DBT compile

Run tests to validate your pipeline:

```
./run.sh test
# or
dbt test --select mock
```

---

## 📡 Monitoring & Logging

- Airflow task logs viewable via the web UI
- Custom loggers for API responses and ETL steps
- Optionally integrates with **Stackdriver Logging** and **Alerting**

---

## 🗺️ Roadmap

- [ ] Add unit tests for transformation logic
- [ ] Set up CI/CD with GitHub Actions
- [ ] Auto-deploy to Cloud Composer
- [ ] Add support for other destinations (e.g., Snowflake, S3)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  

---

## 🧰 Resources:

### 🧱 DBT

- [DBT Docs](https://docs.getdbt.com/docs/introduction)
- [DBT QA](https://discourse.getdbt.com/)
- [DBT Chat](https://community.getdbt.com/)
- [DBT Events](https://events.getdbt.com)
- [DBT blog](https://blog.getdbt.com/) 

---

## 👩‍💻 Author

**Camila Javiera Muñoz Navarro**  
Data Engineer & Analyst | BigQuery | Airflow | Python | GCP  
[GitHub](https://github.com/CamilaJaviera91) | [LinkedIn](https://www.linkedin.com/in/camilajavieramn/) | [Portfolio](https://camilajaviera91.github.io/camila-portfolio/)

---

> ⭐ If you find this project useful, give it a ⭐️ and share your feedback or ideas in [Issues](https://github.com/CamilaJaviera91/modern-data-pipeline-gcp/issues)!