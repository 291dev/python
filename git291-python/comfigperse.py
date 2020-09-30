import configparser

config = configparser.ConfigParser()
config['web_server'] = {
  'host': "localhost",
  'port': 80
}
config['db_server'] = {
  'host': "localhost",
  'port': 8080
}

with open('config.ini','w') as config_file:
  config.write(config_file)


config = configparser.ConfigParser()
config.read('config.ini')
print(config['web_server']['host'])
