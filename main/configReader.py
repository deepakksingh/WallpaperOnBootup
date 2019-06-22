import yaml


class ConfigReader():
    '''defines utilities to read a yaml configuration file'''

    def __init__(self,configFileLocation):
        '''initializer method'''
        self.configFileLocation = configFileLocation

    def readConfigFile(self):
        '''reads a yaml configuration file'''
        cfgFile = yaml.safe_load(open(self.configFileLocation))
        return cfgFile
        
    def getConfig(self):
        '''returns the read configuration file'''
        cfg = self.readConfigFile()
        return cfg


