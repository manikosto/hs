Web Autotests

# Local running example

STAGE=hyperskill-release-tests ENV=chrome_pc DB=sqlite pytest -s -v -m smoke

# CI Run

STAGE=hyperskill-release-tests SUITE=smoke ENV=chrome DB=sqlite docker-compose up pytest




<!-- 'ui-standalone-qa-tests'
'ui-standalone-qa-tests'
'combase1-qa-tests'
'combase1-prod-tests'
'combase2-qa-tests' 
'combase2-qa-tests' 
'integration-qa-tests' 
'integration-prod-tests' 
'api-qa-tests' 
'api-prod-tests' 
'mobile-qa-tests' 
'mobile-prod-tests' -->


