FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    wget \
    firefox \
    default-jre \
    python3.6 \
    python3-pip \
    allure \
    npm \
    default-jre

RUN npm install -g allure-commandline --save-dev

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/local/bin/ \
    && rm /tmp/geckodriver.tgz

RUN chmod +x /usr/local/bin/geckodriver

COPY ./ /

WORKDIR selenium_ui_tests_bdd/

RUN chmod +x start.sh

RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt

CMD ["./start.sh"]