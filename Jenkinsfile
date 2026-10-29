
pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                bat '"C:\\Users\\dhore\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '.venv\\Scripts\\python.exe hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Data Drift Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe generate_report.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }
    }
}
