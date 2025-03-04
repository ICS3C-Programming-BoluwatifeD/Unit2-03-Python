##################################################

# Run Mr Raffin's Super Linter against code base #

##################################################

---

name: Ms Raffin's Super Linter

on: [push, pull_request]

jobs:

  run-linters:

    name: Ms Raffin's Super Linter

    runs-on: ubuntu-latest

    steps:

      - name: Check out Git repository 🚦

        uses: actions/checkout@main

      - name: Run GitHub Super Linter 🚀

        uses: mr-coxall/super-linter@master

        env:

          VALIDATE_ALL_CODEBASE: true

          LINTER_RULES_PATH: /

          VALIDATE_CLANG_FORMAT: false

          VALIDATE_JAVASCRIPT_STANDARD: false

          VALIDATE_GOOGLE_JAVA_FORMAT: false

          VALIDATE_PYTHON_FLAKE8: false

          VALIDATE_GITLEAKS: false # for secrets detection

          VALIDATE_JSON: false

          VALIDATE_JSCPD: false # for copy and paste detection

          DEFAULT_BRANCH: main

          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

