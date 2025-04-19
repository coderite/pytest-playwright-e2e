pipeline {
    agent any

    stages {
        //stage('Checkout PR') {
        //    steps {
        //        checkout scm
        //    }
        //}

        stage('Fetch Postman Tests') {
            steps {
                echo "Cloning Postman collection repo..."
                git(
                    url: "https://github.com/coderite/api-tests",
                    credentialsId: 'a0f751a3-494c-4a2a-8c6e-93e18a89f0fe',
                    branch: 'main'
                )
            }
        }

        stage('Run API Tests') {
            agent {
                docker {
                    image 'postman/newman:latest'
                    args '-u root:root'
                }
            }
            steps {
                echo "Running newman..."
                sh '''
                    mkdir -p newman-results
                    newman run postman_api_tests.json \
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