import subprocess

def run_dbt_mock_models():
    print("🚀 Running DBT models: mock")
    try:
        subprocess.run(["dbt", "run", "--select", "mock"], check=True)
        print("✅ DBT models ran successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ DBT command failed with exit code {e.returncode}")
        raise