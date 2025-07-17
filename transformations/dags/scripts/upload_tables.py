import subprocess

def run_dbt_mock_models():
    print("🚀 Running DBT models: mock")
    try:
        result = subprocess.run(
            ["/usr/local/bin/dbt", "run", "-s", "mock"],
            check=True,
            capture_output=True,
            text=True
        )
        print("✅ DBT models ran successfully")
    except subprocess.CalledProcessError as e:
        stderr = e.stderr or ""
        if "already exists" in stderr or "relation" in stderr:
            print("⚠️ Tables or schema already exist. Continuing gracefully.")
        else:
            print(f"❌ DBT command failed with exit code {e.returncode}")
            print(stderr)
            raise
