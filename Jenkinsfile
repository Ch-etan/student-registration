
pipeline {
    agent any

    tools {
        jdk 'JDK25'
        maven 'Maven3'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Java and Maven') {
            steps {
                sh 'java -version'
                sh 'mvn -version'
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh 'mvn test'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: false,
                  testResults: 'target/surefire-reports/*.xml'
        }

        success {
            echo 'SUCCESS: All registration form tests passed.'
        }

        failure {
            echo 'FAILURE: Check the console output and test reports.'
        }
    }
}
