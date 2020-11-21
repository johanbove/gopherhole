# How to get SonarQube running with Docker

First install Docker and set up an account on the Docker repository.

> We assume you already have Docker installed and have a working account.
> The explanation below is for running a local SonarQube server and is not
meant to be used in production.
> It also assumes that you've set up your Web project with Vue.js and
Jest.js spec files.
> It assumes you are keeping your source code in the `./src` folder.

Get sonarqube Docker image and run it:

    docker run -d --name SonarQube -p 9000:9000 -p 9092:9092 sonarqube

Download the sonar-scanner from here and install:

https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner

Create a file and name it ``myproject.properties`` in the root folder of the project.

> **Note:** The paths in the properties below are relative to the root folder.

Set up the project with these properties:

```text
sonar.projectKey=MyProject
sonar.projectName=My Project
sonar.sources=./src
sonar.coverage.exclusions=**/*.spec.js
sonar.sourceEncoding=UTF-8
sonar.flex.cobertura.reportPath=./coverage/clover.xml
sonar.javascript.lcov.reportPaths=./coverage/lcov.info
sonar.scm.provider=git
```

Run sonar-scanner with:

    sonar-scanner -Dproject.settings=myproject.properties

Open http://localhost:9000 in your browser of choice.

Log in with ``admin:admin`` and see the project "My Project" show up there.

---

EOF.
