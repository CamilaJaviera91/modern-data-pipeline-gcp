# 🌐 Modern Data Pipeline GCP

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Airflow](https://img.shields.io/badge/Airflow-2.x-blue)
![DBT](https://img.shields.io/badge/DBT-1.9.x-orange)
![GCP](https://img.shields.io/badge/GCP-ready-green)
![Docker](https://img.shields.io/badge/Containerized-Docker-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-blueviolet)

---

## 📚 Table of Contents

- [🔍 Description](#-description)
- [🚀 Project Overview](#-overview)
    - [🔄 Pipeline Highlights](#-pipeline-highlights)
    - [✅ Features](#-features)
- [📁 `modern-data-pipeline-gcp` – Project Root](#-modern-data-pipeline-gcptransformations--project-root)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Quick Start](#-quick-start)
    - [📋 Requirements](#-requirements)
    - [⚙️ Setup & Usage](#️-setup--usage)
        - [1. Clone & Navigate](#1-clone--navigate)
        - [2. Environment Setup](#2-environment-setup)
        - [3. Install Locally (optional)](#3-install-locally-optional)
        - [4. Start Services (Postgres + Airflow)](#4-start-services-postgres--airflow)
        - [5. Initialize DBT](#5-initialize-dbt)
        - [6. Run Pipeline](#6-run-pipeline)
- [🐳 Using Docker Compose with Airflow](#-using-docker-compose-with-airflow)
    - [💻 Commands](#-commands)
        - [1. Stop and clean everything](#1-stop-and-clean-everything)
        - [2. Initialize Airflow](#2-initialize-airflow)
        - [3. Build airflow and postgres](#3-build-airflow-and-postgres)
        - [4. Start Airflow in the background](#4-start-airflow-in-the-background)
    - [ 🔄 Typical workflow](#-typical-workflow)
        -[💡 Tips](#-tips)    
- [🧪 Testing](#-testing)
- [📡 Monitoring & Logging](#-monitoring--logging)
- [🚀 CI/CD](#-cicd)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing Guidelines](#-contributing-guidelines)
    - [🧰 How to Contribute](#-how-to-contribute)
    - [🧪 Testing](#-testing-1)
- [🧰 Resources](#-resources)
    - [🧱 DBT](#-dbt)
- [👩‍💻 Author](#-author)

---

## 🔍 Description

A production-grade, modular **ETL** workflow built with **Apache Airflow**, **DBT**, and **Google Cloud Platform** (GCP) services. 
<br>
Designed for orchestrated **extraction**, **transformation**, and **loading**, with integrated data quality, **monitoring**, and **CI/CD** best practices.

---

## 🚀 Project Overview

This repository contains an end-to-end **ETL workflow** designed for scalability, maintainability, and cloud readiness. 
<br>
It showcases how to orchestrate data pipelines using Airflow, enrich and transform data with DBT, and deploy the solution using containerized environments and CI/CD pipelines.

#### 🔄 Pipeline Highlights

This repository delivers an end-to-end data pipeline with:
- **Extraction** from a PostgreSQL source and external exchange rate API  
- **Enrichment** and **Transformation** using DBT models  
- **Loading** to CSV, Google Sheets, and optionally to BigQuery  
- **Orchestration** via Airflow DAGs — modular and containerized  
- Built-in **data quality checks**, logging, and alerts

#### ✅ Features

- Modular structure: `extract`, `transform`, `load`, `validate`, `notify`  
- Docker + Docker Compose for consistent local execution  
- DBT for SQL-based modeling and schema tests  
- Airflow DAG to sequence the pipeline steps  
- Integration with GCP services: BigQuery, Sheets API, Secret Manager  
- Robust logging and optional Stackdriver integration

---

## 📁 `modern-data-pipeline-gcp` – Project Root

```
.
├── .venv                               # Virtual environment 
├── transformations                     # Data transformation logic
│   ├── dags
│   │   ├── dag_etl.py
│   │   ├── dag_rates.py
│   │   └── dag_reports.py
│   ├── data                            # CSV exports
│   │   ├── mock_order_items.csv
│   │   ├── mock_orders.csv
│   │   ├── mock_products.csv
│   │   ├── mock_rates.csv
│   │   └── mock_users.csv
│   ├── dbt
│   │   └── .dbt
│   │       ├── .user.yml
│   │       └── profiles.yml
│   ├── models                          # DBT models
│   │   └── mock
│   │       ├── mock_order_items.sql
│   │       ├── mock_orders.sql
│   │       ├── mock_products.sql
│   │       ├── mock_users.sql
│   │       └── schema.yml
│   ├── reports
│   │   ├── active_clients_without_sales.csv
│   │   ├── order_by_status.csv
│   │   └── sales_by_clients.csv
│   ├── scripts                         # Python scripts for pipeline steps
│   │   ├── export_csv.py
│   │   ├── export_sheets.py
│   │   ├── load_exchange_rates.py
│   │   ├── push_to_bigquery.py
│   │   ├── run.sh
│   │   └── upload_tables.py
│   ├── utils                           # Custom utility functions
|   |   └── quality_checks.py
│   ├── airflow
│   ├── dbt_project.yml                 # DBT project config
│   ├── requirement-dev.txt             # Python dependencies
│   ├── requirements.txt                # Python dependencies
│   ├── run_pipeline.py
│   └── wait-for-postgres.sh
├── .gitignore
├── LICENSE
└── README.md                           # Project documentation
```

---

## 🛠️ Tech Stack

| Layer            | Technologies                                  |
|------------------|-----------------------------------------------|
| Orchestration    | Airflow on Docker (locally) or Cloud Composer |
| Transformation   | DBT models deployed to BigQuery               |
| Source data      | PostgreSQL                                    |
| Destinations     | CSV, Google Sheets, BigQuery                  |
| Cloud infra      | GCP: BigQuery, Sheets API, Secret Manager     |
| Containerization | Docker & Docker Compose                       |
| Language         | Python                                        |
| CI/CD            | GitHub Actions                                |

---

## 🚀 Quick Start

### 📋 Requirements

- Docker & Docker Compose  
- Python 3.9+ (for local development)  
- GCP project with access to BigQuery, Sheets API, and Secret Manager  
- PostgreSQL instance for source data  
- `make` (optional, if using Makefile shortcuts)

---

### ⚙️ Setup & Usage

#### 1. Clone & Navigate

```
git clone https://github.com/CamilaJaviera91/modern-data-pipeline-gcp.git
cd modern-data-pipeline-gcp
```

#### 2. Environment Setup

Copy `.env.example` to `.env` and supply:

```
# ⚙️ Airflow
AIRFLOW_UID=...
AIRFLOW__CORE__EXECUTOR=...
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=...
AIRFLOW__CORE__DAGS_FOLDER=...
AIRFLOW__LOGGING__BASE_LOG_FOLDER=...
AIRFLOW__WEBSERVER__SECRET_KEY=...

# 🐘 DBT / Database (PostgreSQL)
DBT_HOST=...
DBT_HOST_TEST=...
DBT_USER=...
DBT_PASSWORD=...
DBT_DBNAME=...
DBT_SCHEMA=...
DBT_PORT=...

# 💱 Exchange Rates API
EXCHANGE_API_KEY=...

# ☁️ Google Cloud / BigQuery
GOOGLE_CREDENTIALS_PATH=...
BQ_PROJECT_ID=...
BQ_DATASET=...
```

#### 3. Install Locally (optional)

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

#### 4. Start Services (Postgres + Airflow)

```
sudo systemctl start docker 
sudo systemctl status docker #verify if it's running

docker-compose up --build
```

#### 5. Initialize DBT

```
cd transformations
dbt init
```

#### 6. Run Pipeline
For a daily production run:
```
./run.sh run
```
Mock mode only:
```
./run.sh run --select enrich_exchange_rates
```

---

## 🐳 Using Docker Compose with Airflow

This guide shows the basic commands to start and manage Airflow using Docker Compose.

### 💻 Commands

#### 1. Stop and clean everything

```
docker compose down -v --remove-orphans
```

- Stops and removes containers, networks, and volumes.

- Use this to reset your environment completely.
 
#### 2. Initialize Airflow

```
docker compose run airflow-init
```

- Runs a one-time container to set up Airflow’s database and config.

- Run this once before starting Airflow.

#### 3. Build Airflow and Postgres

```
docker compose build  
```

#### 4. Start Airflow and Postgres in the background

```
docker compose up -d
```

- Starts all services defined in `docker-compose.yml`.

- Runs containers in detached mode (background).

### 🔄 Typical workflow

Run these commands in order to start fresh:

```
docker compose down -v --remove-orphans
docker compose run airflow-init #just once
docker compose build
docker compose up -d --remove-orphans
```

#### 💡 Tips

- Make sure Docker and Docker Compose are installed.

- To see logs, use:

```
docker compose logs -f
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

## 🚀 CI/CD

- GitHub Actions triggers include:
  - Linting + formatting checks
  - DBT compilation and tests
  - Docker image builds
  - Deployment to Cloud Composer (planned)

---

## 🗺️ Roadmap

- ✅ Initialize core modular pipeline  
- 🧪 Add unit tests for Python & DBT logic  
- 🔁 Implement full CI/CD with automated deploy to GCP  
- 🔄 Extend support to additional sinks (Snowflake, S3, etc.)  
- ⏰ Enable scheduling on Cloud Composer

---

## 🤝 Contributing Guidelines

Thank you for your interest in contributing to this project!

#### 🧰 How to Contribute:

1. **Fork** the repository.
2. **Clone** your fork:  
   `git clone https://github.com/<your-username>/modern-data-pipeline-gcp.git`
3. Create a new branch:  
   `git checkout -b feature/your-feature-name`
4. Make your changes and **commit**:  
   `git commit -m "Add new feature"`
5. Push to your fork:  
   `git push origin feature/your-feature-name`
6. Submit a **pull request** to the `main` branch.

---

## 🧰 Resources

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

---

## 📄 License
This project is licensed under the MIT License.