"""
This script lets users generate YAML credentials.
"""
import sys

from .credentials import YAMLFileWriter

if __name__ == '__main__':
    
    if len(sys.argv) == 5:
        twitter_creds_writer = YAMLFileWriter(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sys.argv[4])
    elif len(sys.argv) == 6:
        twitter_creds_writer = YAMLFileWriter(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4],
            sys.argv[5])
    
    twitter_creds_writer()
    
    if not twitter_creds_writer.success:
        raise ValueError("YAML write didn't work.")
    else:
        print('YAML write successful.')










    

	
