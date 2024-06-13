import requests
import logging

# Set up logging
logging.basicConfig(filename='/var/log/application_health.log', level=logging.INFO)

# URL of the application
APP_URL = 'http://yourapplication.com/health'

def check_application_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            logging.info('Application is UP')
        else:
            logging.warning(f'Application is DOWN, Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking application health: {e}')

if __name__ == '__main__':
    check_application_health()
