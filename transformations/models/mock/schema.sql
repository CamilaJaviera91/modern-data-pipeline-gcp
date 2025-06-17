version: 2

models:
  - name: mock_users
    description: "Mock table of users generated with random data"
    columns:
      - name: user_id
        description: "Unique identifier for the user"
        tests:
          - not_null
          - unique

      - name: username
        description: "Generated username"

      - name: email
        description: "Fake generated email address"

      - name: created_at
        description: "Randomly generated creation date"

      - name: status
        description: "User status (active or inactive)"
        tests:
          - accepted_values:
              values: ['active', 'inactive']