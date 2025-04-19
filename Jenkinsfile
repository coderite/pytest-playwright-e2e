pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                echo 'Hello from the pytest-playwright-e2e repo!'
                echo "Build number: ${currentBuild.number}"
            }
            post {
                success {
                    script {
                        currentBuild.result = "SUCCESS"
                    }
                }
            }
        }
    }
    post {
        always {
            echo currentBuild.currentResult
        }
    }
}