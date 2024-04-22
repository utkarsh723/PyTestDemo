pipeline{
    agent any
    stages{
        stage('Checkout '){
            steps{
                checkout scm
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'pytest --alluredir=allure_report -v -s'
            }
        }
        stage('Generate Reports'){
            steps{
                sh 'allure generate allure_report -o allure_report_html --clean'
            }
        }
        stage('Publish Reports'){
            steps{
                archiveArtifacts 'allure_report_html/**'
            }
        }
    }
}