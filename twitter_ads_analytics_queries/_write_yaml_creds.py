"""
This script lets users generate YAML credentials.
"""
import sys

from twitter_ads_analytics_queries.credentials import YAMLFileWriter

if __name__ == '__main__':
    
    if len(sys.argv) == 5:
        write_twitter_creds = YAMLFileWriter(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sys.argv[4])
    elif len(sys.argv) == 6:
        write_twitter_creds = YAMLFileWriter(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4],
            sys.argv[5])
    
    
    write_twitter_creds()
    
    if not write_twitter_creds.success:
        raise ValueError("YAML write didn't work.")
    else:
        print('YAML write successful.')










    

	
