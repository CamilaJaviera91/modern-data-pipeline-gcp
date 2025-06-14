# 🌐 Modern Data Pipeline GCP

A production-grade, modular ETL pipeline built with **Apache Airflow**, integrated with **Google Cloud Platform (GCP)** services and **DBT** for transformation and modeling. This project demonstrates best practices in orchestration, cloud-native development, CI/CD, data quality, and monitoring — all in a real-world data pipeline context.

---

## 🚀 Overview

This repository contains an end-to-end ETL workflow designed for scalability, maintainability, and cloud readiness. It showcases how to orchestrate data pipelines using Airflow, enrich and transform data with DBT, and deploy the solution using containerized environments and CI/CD pipelines.

### 🔄 Pipeline Highlights:
- [X] Extracts data from a **PostgreSQL** source
- [ ] Enriches it with **exchange rate data** from an external API
- [ ] Loads the results to **CSV files** and **Google Sheets**
- [ ] Optionally pushes transformed data to **BigQuery**
- [ ] Includes **data quality checks** and **logging**
- [ ] Modular structure: `extract`, `transform`, `load`, `validate`, `notify`
- [ ] Uses **Docker + Docker Compose** for local orchestration
- [ ] Ready for deployment on **GCP Cloud Composer** or similar environments

---

## 🛠️ Tech Stack

- **Airflow** – DAG orchestration and scheduling
- **DBT** – SQL-based transformations
- **Google Cloud** – BigQuery, Google Sheets API, Secret Manager
- **Docker** – Containerized development
- **Python** – Task logic and API integrations
- **PostgreSQL** – Source database
- **CI/CD** – GitHub Actions (coming soon)

---

## 🚀 Getting Started

#### ✅ Prerequisites

- Docker & Docker Compose
- Python 3.9+
- `make` (optional, for using the Makefile)

---

#### ⚙️ Local Setup

```
# Clone the repository
git clone https://github.com/CamilaJaviera91/modern-data-pipeline-gcp.git
cd modern-data-pipeline-gcp

# Create `.env` file with required variables
cp .env.example .env
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

---

## ✅ Testing

- **DBT tests** for schema, uniqueness, and relationships
- **Airflow DAG validation**: `airflow dags list`, `airflow dags test`
- **Unit tests** for custom Python functions in `/scripts` or `/dags`
- **CI pipeline** (planned): Linting, formatting, DAG validation, DBT compile

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

## 👩‍💻 Author

**Camila Javiera Muñoz Navarro**  
Data Engineer & Analyst | BigQuery | Airflow | Python | GCP  
[GitHub](https://github.com/CamilaJaviera91) | [LinkedIn](https://www.linkedin.com/in/camilajavieramn/) | [Portfolio](https://camilajaviera91.github.io/camila-portfolio/)

---

> ⭐ If you find this project useful, give it a ⭐️ and share your feedback or ideas in [Issues](https://github.com/CamilaJaviera91/modern-data-pipeline-gcp/issues)!