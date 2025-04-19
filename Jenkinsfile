pipeline {
    agent any

    stages {
        stage('Checkout PR') {
            steps {
                checkout scm
            }
        }

        stage('Fetch Postman Tests') {
            steps {
                echo "Cloning Postman collection repo..."

                git(
                    url: "https://github.com/coderite/api-tests",
                    credentialsId: 'github-app',
                    branch: 'main'
                )
            }
        }

        stage('Run API Tests') {
            steps {
                echo "Running newman against PR..."
                sh '''
                    npm init -y
                    npm install newman
                    mkdir -p newman-results
                    npx newman run api-tests/postman_api_tests.json \
                        --reporters cli,junit \
                        --reporter-junit-export newman-results/results.xml
                '''
            }

            post {
                always {
                    junit 'newman-results/results.xml'
                }
            }
        }
    }

  post {
    success {
      echo "🎉 All API tests passed! PR is clear to merge."
    }
    failure {
      echo "❌ Some API tests failed — build is FAILED, PR stays blocked."
    }
  }
}