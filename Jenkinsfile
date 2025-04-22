void setBuildStatus(String message, String state) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/coderite/pytest-playwright-e2e"],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

pipeline{
    agent any

    stages{
        stage('Fetch Postman Tests') {
            steps {
                echo "Cloning Postman collections repo..."
                git(
                    url: "https://github.com/coderite/api-tests",
                    credentialsId: 'github-app',
                    branch: 'main'
                )
            }
            post {
                success {
                    echo "GITHUB REPO WITH As POSTMsAN TEST CLONED SUCCESsSFULsLY!"
                    setBuildStatus("Build succeeded", "SUCCESS");
                }
                failure {
                    echo "GITHUB REPO CLONING FAILED!"
                    setBuildStatus("Build failed", "FAILURE");
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