# 🌐 Modern Data Pipeline GCP

A production-grade, modular ETL pipeline built with **Apache Airflow**, integrated with **Google Cloud Platform (GCP)** services and **DBT** for transformation and modeling. This project demonstrates best practices in orchestration, cloud-native development, CI/CD, data quality, and monitoring — all in a real-world data pipeline context.

---

## 🚀 Overview

This repository contains an end-to-end ETL workflow designed for scalability, maintainability, and cloud readiness. It showcases how to orchestrate data pipelines using Airflow, enrich and transform data with DBT, and deploy the solution using containerized environments and CI/CD pipelines.

### 🔄 Pipeline Highlights:
- Extracts data from a **PostgreSQL** source
- Enriches it with **exchange rate data** from an external API
- Loads the results to **CSV files** and **Google Sheets**
- Optionally pushes transformed data to **BigQuery**
- Includes **data quality checks** and **logging**
- Modular structure: `extract`, `transform`, `load`, `validate`, `notify`
- Uses **Docker + Docker Compose** for local orchestration
- Ready for deployment on **GCP Cloud Composer** or similar environments

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

---

## 👩‍💻 Author

**Camila Javiera Muñoz Navarro**  
Data Engineer & Analyst | BigQuery | Airflow | Python | GCP  
[GitHub](https://github.com/CamilaJaviera91) | [LinkedIn](https://www.linkedin.com/in/camilajavieramn/) | [Portfolio](https://camilajaviera91.github.io/camila-portfolio/)

---

> ⭐ If you find this project useful, give it a ⭐️ and share your feedback or ideas in [Issues](https://github.com/CamilaJaviera91/modern-data-pipeline-gcp/issues)!