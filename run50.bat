rd /s /q "allure_results"
py.test -s --count=10 --alluredir allure_results -Wignore::DeprecationWarning
allure generate --clean -o allure-report allure_results
