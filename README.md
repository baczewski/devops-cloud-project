# DevOps Cloud Project

Финален проект за курса **Съвременни DevOps практики**, чиято цел е да упражним и приложним някои съвременни DevOps практики върху семпло приложение реализиращо Movie API.

## Достъп до услугата:
http://a88689c0a4dba4aa4ab9326f66d65dae-1833740573.eu-north-1.elb.amazonaws.com/

Възможни пътища са:
`/movies` и `/shows`

Всеки от тези пътища разполага с параметър с името `time`.
Приема стойностите `day` и `week`. Държанието по подразбиране е `day`.

Пример за използване на заявка: `http://a88689c0a4dba4aa4ab9326f66d65dae-1833740573.eu-north-1.elb.amazonaws.com/movies?time=week`

## Използвани Технологии

Проектът използва съвременни технологии и инструменти, които поддържат ефективната разработка и доставка на приложението. Важни технологии включват:

- `Docker` - Използване с цел улесняване пакетирането на приложението и осигурява консистентна и преносима среда.

- `Flask` - Използване на Flask с цел подпомагане за лесното изграждане на сървъра на приложението.

- `AWS` - Използване облачните услуги на AWS, за доставка и управление на контейнеризирани приложения в облака.

Тези технологии съчетават функционалността и устойчивостта, осигурявайки надеждност и лесна мащабируемост на проекта.

## CI/CD Pipeline

При сливане на промени в `master` branch-a използваме цялостен CI/CD pipeline, който автоматизира различните етапи от разработката до доставката на приложението в AWS EKS.

![master-ci-pipeline](/blob/master-ci.png)

### Етапи в CI/CD Pipeline-а:

1. **Static Code Analysis (MyPy, Ruff):**
   - Използваме инструменти за статичен анализ на кода, като `MyPy` и `Ruff`, за да проверим съответствието със стандартите за писане на код.

2. **Run Python Tests:**
   - Започваме изпълнение на тестове, които проверяват функционалността и коректността на кода.

3. **Security Scanning (SonarCloud, Snyk, Grype):**
   - Използваме инструменти за сигурностен сканинг като `SonarCloud`, `Snyk` и `Grype`, за да открием потенциални сигурностни и кодови проблеми както в кода.

4. **Create and Scan Docker Image:**
   - Създаваме Docker image, след което извършваме сканиране с инструментите `Trivy` и `Grype`, за да открием потенциални сигурностни проблеми в контейнера.

5. **Create and Upload Docker Image:**
   - Създаденият Docker image се качва в публичен репозиторий на `DockerHub`, гарантирайки достъпност и лесно управление на контейнерите.

6. **Deploy to AWS EKS:**
   - При успешно преминаване през предходните стъпки, приложението се автоматично деплойва в AWS EKS cluster. За създаването на контейнера се използва предварително създадения Docker image.

Този CI/CD pipeline не само гарантира високо качество на кода и сигурност на приложението, но и улеснява и ускорява процеса на доставка на нови версии в продукцията.

## Диаграма на работата с AWS EKS

![aws-eks-communication-diagram](/blob/aws-communication-diagram.jpg)

## Стартиране на локално приложение с Docker

Следните команди трябва да бъдат изпълнени в тази последователност, за да се стартира приложението:

Предварителни изисквания:
 - Инсталиран Docker
 - Клонирано repository

```bash
# Стъпка 1: Изграждане на Docker Image
docker build -t image-name .

# Стъпка 2: Стартиране на Контейнера
docker run -p 80:8080 --env MOVIE_API_KEY=your-api-key image-name
```
### Важно
> При стартиране на контейнера е нужно да се подаде API ключ издаден от [The Movie Database](https://www.themoviedb.org/)

> Възможно е да се подаде и environment variable със същото име при пускане на контейнера.
## Contributors

Проектът е разработен от:

- [Denislav Manahov](https://github.com/poinp)
- [Martin Marinov](https://github.com/baczewski)

PS: We are 100$ behind, because poinp didn't stop the large nodes...
