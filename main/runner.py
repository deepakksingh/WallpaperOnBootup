"""
contains code to initiate the process
"""
import sys
sys.path.append('../../')

from api_base.api_framework import APIFramework
from configReader import ConfigReader
#TODO: Fix the import statements, APIFramework is not being imported


CONFIG_PATH = 'configs/config.yaml'

api_framework = APIFramework()
cfg_reader = ConfigReader(CONFIG_PATH)

cfg = cfg_reader.getConfig()
print(cfg)
