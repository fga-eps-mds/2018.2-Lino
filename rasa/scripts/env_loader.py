import os

variables = {
    'URI_TELEGRAM': os.getenv('URI_TELEGRAM', 'localhost'),
    'URI_FACEBOOK': os.getenv('URI_FACEBOOK', 'localhost'),
    'PSID': os.getenv('PSID', ''),
    'TELEGRAM_ACCESS_TOKEN': os.getenv('TELEGRAM_ACCESS_TOKEN', ''),
    'FACEBOOK_ACCESS_TOKEN': os.getenv('FACEBOOK_ACCESS_TOKEN', '')
}

with open('loaded-env.txt', 'w') as f:
    for name in variables:
        f.write(f'{name}={variables[name]}\n')
    f.close()
