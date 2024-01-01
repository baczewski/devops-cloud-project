# DevOps Cloud Project

Финален проект за курса **Съвременни DevOps практики**, чиято чел е да упражним и приложним някои съвременни DevOps практики върху семпло приложение реализиращо Movie API.

## CI/CD Pipeline

При сливане на промени в `master` branch-a използваме цялостен CI/CD pipeline, който автоматизира различните етапи от разработката до доставката на приложението в AWS EKS.

![master-ci-pipeline](https://github.com/baczewski/devops-cloud-project/blob/master/blob/master-ci.png)

### Етапи в CI/CD Pipeline-а:

1. **Static Code Analysis (Flake8, MyPy, Ruff):**
   - Използваме инструменти за статичен анализ на кода, като `Flake8`, `MyPy` и `Ruff`, за да проверим съответствието със стандартите за писане на код.

2. **Security Scanning (SonarCloud, Snyk, Grype):**
   - Използваме инструменти за сигурностен сканинг като `SonarCloud`, `Snyk` и `Grype`, за да открием потенциални сигурностни и кодови проблеми както в кода, така и в Docker image-a.

3. **Run Python Tests:**
   - Започваме изпълнение на тестове, които проверяват функционалността и коректността на кода.

4. **Create and Scan Docker Image:**
   - Създаваме Docker image, след което извършваме сканиране с инструмента `Trivy`, за да открием потенциални сигурностни проблеми в контейнера.

5. **Create and Upload Docker Image:**
   - Създаденият Docker image се качва в публичен репозиторий на `DockerHub`, гарантирайки достъпност и лесно управление на контейнерите.

6. **Deploy to AWS EKS:**
   - При успешно преминаване през предходните стъпки, приложението се автоматично деплойва в AWS EKS cluster. За създаването на контейнера се използва предварително създадения Docker image.

Този CI/CD pipeline не само гарантира високо качество на кода и сигурност на приложението, но и улеснява и ускорява процеса на доставка на нови версии в продукцията.

## Contributors

Проектът е разработен от:

- [Denislav Manahov](https://github.com/poinp)
- [Martin Marinov](https://github.com/baczewski)

PS: We are 100$ behind, because poinp didn't stop the large nodes...
