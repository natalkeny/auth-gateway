import logging
import os
from auth_gateway.config import Config
from auth_gateway.server import Server
from auth_gateway.utils import setup_logging

def main():
    # Load configuration
    config = Config(os.path.join(os.path.dirname(__file__), 'config.json'))

    # Setup logging
    setup_logging(config.log_level)

    # Initialize server
    server = Server(config)

    # Start server
    try:
        server.start()
    except KeyboardInterrupt:
        logging.info('Stopping server...')

if __name__ == '__main__':
    main()