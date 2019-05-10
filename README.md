## **Setup**

```
git clone https://github.com/pbezrukov/selenium_tests_bdd.git
cd path/to/selenium_tests_bdd 
docker build -t selenium .
```
***
## **Run tests**

```docker run -p 5000:5000 -it -v $(pwd)/selenium_ui_tests_bdd/results:/selenium_ui_tests_bdd/results selenium```

***
## **Look of report**

Open browser and go to url ```localhost:5000```

