
import os
import pandas as pd

from datetime import datetime

from config import (
    SOURCE_DIR,
    TARGET_DIR,
    TARGET_CLASS_MAP,
    ETL_DIR
)

from typing import TypeVar

from src.Sources.S1 import S1

T = TypeVar('T')


class SourceProcessor(object):
    
    def __init__(self, file_path:str) -> None:
        self._file_path=file_path
        
    @property
    def target_class(self) -> T:
        source_name = self._file_path.split('/')[-2]
        return TARGET_CLASS_MAP[source_name]
        
    @property
    def source_name(self) -> str:
        source_name = self._file_path.split('/')[-2]
        return source_name
        
    def get_target_file(self) -> str:
        source_file_name = self._file_path.split('/')[-1]
        target_file = os.path.join(TARGET_DIR, self.source_name, source_file_name)
        return target_file
    
    def get_source_obj(self, data) -> T:
        return {
            'S1' : S1(**data)
        }[self.source_name]
        
    def save_target(self, target_df:pd.DataFrame) -> None:
        target_file = self.get_target_file()
        
        # make sure dir exists
        target_dir_source = '/'.join(target_file.split('/')[:-1])
        os.makedirs(target_dir_source, exist_ok=True)
        
        target_df.to_csv(target_file, index=False)
        
        
    def generate_target(self)->None:
        sclass = getattr(self.target_class,'__init__')
        
        # to save time I am reading using pandas
        # we can also implement dict csv reader and read line by line and process
        
        inputdf = pd.read_csv(self._file_path)
        
        target_data = []
        for row in inputdf.to_dict(orient='records'):
            sobj = self.get_source_obj(data=row)
            target_obj = sobj.get_outreach_obj()
            target_data.append(
                target_obj.dict()
            )
            
        target_df = pd.DataFrame.from_records(target_data)
        
        # add metadata
        target_df['source'] = self.source_name
        target_df['source_file'] = self._file_path
        target_df['_create_ts'] = datetime.now()
        self.save_target(target_df=target_df)
        
        self.target_df = target_df
        
    def save_to_db(self,  dbcon) -> None:
        
        self.target_df.to_sql(
            con=dbcon,
            name=self.source_name + '_stg',
            if_exists = 'replace'
        )
        
    def get_etl_dir(self) -> str:
        return os.path.join(ETL_DIR,self.source_name)
        
    def etl(self, db) -> None:
        """
        do incremental append into prod table from staging table
        """
        source_etl_dir = self.get_etl_dir()
        etl_files = []
        for _, _, files in os.walk(source_etl_dir):
            for _file in files:
                etl_files.append(os.path.join(source_etl_dir,_file))
                
        status = { etl_file: db.execute_sql_from_file(etl_file) for etl_file in etl_files }
        print(f"""
              ETL status"
              {status}
              """)
        return True

        
                    
        