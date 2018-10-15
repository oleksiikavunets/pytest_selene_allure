rd /s /q "allure_results"
py.test -s  --alluredir allure_results
allure generate --clean -o allure-report allure_results
