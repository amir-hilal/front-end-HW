import yaml
import os

class Client:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def print_server_ip(self):
        print(f"Server IP Address: {self.config['ServerIPAddress']}")

    def print_user_name(self):
        print("the username is amir")


if __name__ == "__main__":
    client = Client()
    client.print_server_ip()
    client.print_user_name()
    client.print_user_name()
