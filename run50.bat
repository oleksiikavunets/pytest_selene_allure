rd /s /q "allure_results"
py.test --count=10 --alluredir allure_results
allure generate --clean -o allure-report allure_results
