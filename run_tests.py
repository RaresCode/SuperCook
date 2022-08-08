import os
import time

allure_report = input("Do you want to generate allure report? (Yes/No):")

if allure_report == "Yes":
    os.system("behave -f allure_behave.formatter:AllureFormatter -o reports/ features")
    os.system("allure serve reports")
else:
    os.system("behave.exe .\\features\\")