pipeline {
    agent any
    environment {
        GOOGLE_PROJECT_ID = 'callback-demons';
        GOOGLE_SERVICE_ACCOUNT_KEY = credentials('google_cloud');
    }
    tools {
        nodejs 'NodeJS 14.3.0'
    }
    stages {
        stage('Deploy') {
            steps {
                sh """
					#!/bin/bash
					ssh gerardo_marquez_carmona@api.callback-news.com -p 2222 'ls'
				"""
            }
        }
    }
}