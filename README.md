<h1 align="center">Фреймворк для автоматизации тестирование онлайн кинотеатра Allplay"</h1>

<img align="center" src="resources/images/site.png"/>  

***
***Особенности проекта***  
-Оповещения о тестовых прогонах в Telegram  
-Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы  
-Сборка проекта в Jenkins  
-Отчеты Allure Report  
-Интеграция с Allure TestOps
-Запуск web/UI автотестов в Selenoid.


***
***Список проверок, реализованных в web/UI автотестах***

-Проверка регистрации на сайте   
-Вход в сайт с зарегестрированными данными     
-Переход в раздел ТВ по кнопке который находиться в шапке сайта  
-Переход в раздел Кинотеатр по кнопке   
-Поиск определленого фильма по называнию и   переход на карточку фильма    

***


***Используемый стэк***  
<p align="left">
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jira/jira-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" height="40" width="40" />
<img align="center" src="resources/images/allure.png" height="40" width="40" />
<img align="center" src="resources/images/selene.png" height="40" width="40" />
<img align="center" src="resources/images/selenoid.png" height="40" width="40" />
<img align="center" src="resources/images/appium.png" height="40" width="40" />
<img align="center" src="resources/images/telegram.png" height="40" width="40" />
<img align="center" src="resources/images/browserstack.png" height="40" width="40" />

***  
***Запуск тестов***  
---

<h2 id="run-tests"><img width="40" align="center" src="resources/run-tests.png" alt="run"> Run tests</h2>
<p><b>For web tests:</b></p>
<pre>
    pytest tests/ui
</pre>
<p><b>For API tests:</b></p>
<pre>
    pytest tests/api
</pre>
<p><b>For mobile tests on emulator:</b></p>
<pre>
    pytest tests/mobile --context=local_emulator
</pre>
<p><b>For mobile tests on bstack:</b></p>
<pre>
    pytest tests/mobile --context=bstack
</pre>

---

<p>To run tests in Jenkins you need to click on <b>Build with Parameters</b> button</p>
<img src="resources/images/build.png" alt="build">
<p>Сhoose parameters (<i>BROWSER_VERSION, ENVIRONMENT, COMMENT</i>) and click on <b>"Build"</b> button</p>
<img src="resources/images/parametrs.png" alt="parameters">
<p>After passing the tests report will be generated, you can see it by clicking on the <b>Allure report</b> and <b>Allure TestOps</b></p>
<p><a href="https://allure.autotests.cloud/project/4275/dashboards">TestOps</a></p>
<img src="resources/images/allure_report.png" alt="allure-report">
<img src="resources/images/allure-result.png" alt="allure-result">
<img src="resources/images/allure-testcases.png" alt="allure-testOps">

<p>Project in Jira</p>
<img src="resources/images/jira_integration.png" alt="jira">


---



---


***Видео прохождение UI автотестов*** 

<img align="center" src="resources/images/video_from-test.gif"/>  

***