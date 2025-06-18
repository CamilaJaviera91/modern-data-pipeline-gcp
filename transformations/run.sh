#!/bin/bash

# Load environment variables
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
else
  echo "⚠️  .env file not found. Please create one with your environment variables."
  exit 1
fi

# Set DBT profile path
export DBT_PROFILES_DIR=$(pwd)/.dbt

# Run DBT with any passed arguments
dbt "$@"
