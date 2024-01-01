# DevOps Cloud Project

A simple project for a DevOps Course 

### TODO: Documentation

# Pipeline

При Merge в master branch-a използваме pipeline, който след успешно изпъление deploy-ва приложението ни в AWS EKS.

### Стъпки в pipeline-a:
  - **Static Code Analysis (Flake8, MyPy, Ruff)** - използвани са инструменти за статичен анализ на кода за проверка за съответствие със стандартите.
  - **Security Scanning (SonarCloud, Snyk, Grype)** - използвани са инстументи за откриване на потенциални проблеми със сигурността и проблеми в кода и в docker image-a.
  - **Run Python Tests** - за проверка на функционалността и коректността на кода стартираме тестове.
  - **Create and Scan Docker Image** - създава се docker image, който се сканира за потенциални проблеми със сигурността с Trivy.
  - **Create and Upload Docker Image** - качва създадения docker image в публично repository в DockerHub.
  - **Deploy to AWS EKS** - приложението се deploy-ва върху AWS EKS cluser, като за създаването на контейнера се използва предварително съзададения docker image.
