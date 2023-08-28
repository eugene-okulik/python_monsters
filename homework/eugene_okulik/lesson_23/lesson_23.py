import config
import os
import dotenv

dotenv.load_dotenv()


def log_in(username, password):
    print(username, password)


login = os.getenv('LOGIN')
passw = os.getenv('PASSWORD')
# log_in(config.login, config.password)
log_in(login, passw)
print(os.getenv('TEST'))
