import configparser

# config
path_settings = 'settings.ini'
config = configparser.ConfigParser()
config.read(path_settings)
# -------------------------------------------------
HOST = config.get('service', 'host')
PORT = config.get('service', 'port')



#path_others = 'others.ini'
#config = configparser.ConfigParser()
#config.read(path_others)
## -------------------------------------------------
#HOST = config.get('service', 'host')
#PORT = config.get('service', 'port')


