import fire

from src.source_processor import SourceProcessor
from src.db import OutreachDB

class Commands:
    
    def process(self, file_path):
        sp = SourceProcessor(file_path=file_path)
        sp.generate_target()
        sp.save_to_db(dbcon=OutreachDB().con)
        sp.etl(db=OutreachDB())
        
        

if __name__ == '__main__':
    fire.Fire(Commands)