#!/bin/bash
pytest --alluredir=results
allure serve results/ -p 5000