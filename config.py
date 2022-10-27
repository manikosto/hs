import os

class Config:

    config = {

        'hyperskill-prod-tests': {
            "DOMAIN": "hyperskill.org",  # Here we write domain for stage
        },

        'hyperskill-release-tests': {
            "DOMAIN": "release.hyperskill.org",
        }

    }

    links = {

        'hyperskill-prod-tests': {
            "DOMAIN": "hyperskill.org",  # Here we write domain for stage
            "TRACKS_PAGE": "/tracks", 
        },

        'hyperskill-release-tests': {
            "DOMAIN": "release.hyperskill.org", # Here we write domain for stage
            "TRACKS_PAGE": "/tracks",
            "LOGIN_PAGE": "/login",  
            "THEORY_TASK": "/learn/step/3500"
        }
    }