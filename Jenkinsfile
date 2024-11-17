pipeline {
    agent any

    stages {
        stage('Preparar Ambiente') {
            steps {
                script {
                    // Verificar conexión
                    sh 'docker -H tcp://host.docker.internal:2375 version'
                }
            }
        }

        stage('Construir Contenedores') {
            steps {
                script {
                    sh 'docker-compose -H tcp://host.docker.internal:2375 build'
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    sh 'docker-compose -H tcp://host.docker.internal:2375 up --abort-on-container-exit'
                }
            }
        }

        stage('Desplegar') {
            steps {
                echo 'Despliegue exitosoOWo'
            }
        }
    }
}
