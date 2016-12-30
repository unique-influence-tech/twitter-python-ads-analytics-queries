#!/bin/bash
# Export a variable pointing to a Twitter YAML file 
# User should supply CREDS_DIR and ENV_FILE 

set -e; 

CREDS_DIR=$1 # absolute path to credentials directory
ENV_FILE=$2 # absolute path to environment file

echo "----------------------------------<>";
echo "Adding TWITTER_CREDENTIALS variable to environment file.."

if [[ ! -z "$CREDS_DIR" ]] && [[ ! -z "$ENV_FILE" ]];
    then
        echo 'Paste your consumer key here:'
        read CONSUMER_KEY
        
        echo 'Paste your consumer secret key here:'
        read CONSUMER_SECRET
        
        echo 'Paste your access key here:'
        read ACCESS_TOKEN
        
        echo 'Paste your access secret key here:'
        read ACCESS_TOKEN_SECRET

        if [[ ! -z "$CONSUMER_KEY" ]] && [[ ! -z "$CONSUMER_SECRET" ]] && [[ ! -z "$ACCESS_TOKEN" ]] && [[ ! -z "$ACCESS_TOKEN_SECRET" ]];
            then 
                python -m twitter_ads_analytics_queries._write_yaml_creds "$CONSUMER_KEY" "$CONSUMER_SECRET" "$ACCESS_TOKEN_SECRET" "$ACCESS_TOKEN_SECRET" "$CREDS_DIR";
                sed -i '' '/TWITTER_CREDENTIALS/d' "$ENV_FILE";
                echo 'Add variable to environment..';
                echo $'\n' >> $ENV_FILE;
                echo "export TWITTER_CREDENTIALS=${CREDS_DIR// /\\ }/.twitter.yml" >> $ENV_FILE;
            else
                echo 'TWITTER_CREDENTIALS variable adding: FAILED';
                echo 'Reason: One of required Twitter credentials is blank.';
                echo '----------------------------------<>';  
                return;
        fi;
    else
        echo 'TWITTER_CREDENTIALS variable adding: FAILED';
        echo 'Reason: You must supply a credentials directory and environment file.';
        echo '----------------------------------<>';  
        return;
fi;
echo 'TWITTER_CREDENTIALS variable adding: SUCCESS';     
echo "$ENV_FILE sourced."
echo '----------------------------------<>';
return;

