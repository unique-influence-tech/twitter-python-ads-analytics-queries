"""
Configuration module to keep your credentials stored locally.
"""
import yaml
import subprocess

from twitter_ads.client import Client


class EasyAuth:
    """ A class used to hold a client and account class.

    You can load in manually by supplying various arguments for 
    Twitter credentials or you can supply an environment variable 
    pointing to a YAML file containing credentials.

    :params account: str, alphanumeric string 
    :params from_env_var: str, part of variable name 
                               that contains credentials file
    :params creds: str, args related to twitter credentials
    """
    def __init__(self, account, from_env_var=True, **creds):
        if from_env_var:
            shell_command = "printenv | grep {search}".format(search=from_env_var)
            process = subprocess.Popen(
                 shell_command,
                 stdout=subprocess.PIPE,
                 shell=True)
            out = str(process.communicate()[0])
            result = out[out.find('/'):out.find('\\')]
            yml = yaml.load(open(result))
            self._client = Client(
                yml['CONSUMER KEY'],
                yml['CONSUMER SECRET'],
                yml['ACCESS TOKEN'],
                yml['ACCESS TOKEN SECRET'])
        else:
            self._client = Client(
                creds['CONSUMER KEY'],
                creds['CONSUMER SECRET'],
                creds['ACCESS TOKEN'],
                creds['ACCESS TOKEN SECRET'])
        self._account = self._client.accounts(account)
        
    @property
    def account(self):
        return getattr(self, '_account')
    
    def __repr__(self):
        return "<account name=[{name}] and id=[{id}]>".format(
            name=self._account.name,
            id=self._account.id)






