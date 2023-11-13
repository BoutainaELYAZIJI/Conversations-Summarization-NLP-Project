from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity.config_entity import DataIngestionConfig


class ConfigurationManager:

    # constructor initialised by config & params filepaths
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
    #Read yaml files & return it's content
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
    #Create dirctory artfacts_root => for "config.artifacts_root" here is the use of ConfigBox
        create_directories([self.config.artifacts_root])
        

    # return of this method is DataIngestionConfig    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
    # creating root_dir
        create_directories([config.root_dir])
    
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config        
        