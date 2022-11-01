import os

class Config:

    config = {

        'hyperskill-prod-tests': {
            "DOMAIN": "hyperskill.org",  # Here we write domain for stage
            "ACCOUNT_LOGIN": "auto@test.hyperskill.org",
            "ACCOUNT_PASSWORD": "512"
        },

        'hyperskill-release-tests': {
            "DOMAIN": "release.hyperskill.org",
            "ACCOUNT_LOGIN": "auto@test.hyperskill.org",
            "ACCOUNT_PASSWORD": "512"
        }

    }

    links = {

        'hyperskill-prod-tests': {
            "DOMAIN": "hyperskill.org",  # Here we write domain for stage
            "TRACKS_PAGE": "/tracks", 
            "TRACKS_PAGE": "/tracks",
            "LOGIN_PAGE": "/login",
        },

        'hyperskill-release-tests': {
            "DOMAIN": "release.hyperskill.org", # Here we write domain for stage
            "TRACKS_PAGE": "/tracks",
            "LOGIN_PAGE": "/login",  
            "THEORY_TASK": "/learn/step/3500"
        }
    }