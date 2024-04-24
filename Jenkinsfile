pipeline{
    agent any
    stages{
        stage('Checkout '){
            steps{
                checkout scm
            }
        }

        stage('Run Tests'){
            steps{
                bat 'pytest -k test_LoginPage.py --alluredir=allure_report'
            }
        }
        stage('Generate Reports'){
            steps{
                bat 'allure generate allure_report -o allure_report_html --clean'
            }
        }
        stage('Publish Reports'){
            steps{
                archiveArtifacts 'allure_report_html/**'
            }
        }
    }
}