"""
Configuration module to keep your credentials stored locally.
"""
import yaml
import subprocess
import os.path

from twitter_ads.client import Client

class EasyAuth:
    """ The <[EasyAuth]> class is used to hold a client and account class.

    You can load in manually by supplying various arguments for 
    Twitter credentials or you can supply an environment variable 
    pointing to a YAML file containing credentials.

    :params account: str, alphanumeric string 
    :params from_env_var: str, part of variable name 
                               that contains credentials file
    :params creds: str, args related to twitter credentials
    """
    def __init__(self, account, from_env_var=None, **creds):
        if creds:
            self._client = Client(
                creds['CONSUMER KEY'],
                creds['CONSUMER SECRET'],
                creds['ACCESS TOKEN'],
                creds['ACCESS TOKEN SECRET']) 
        elif from_env_var is not None:
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
            from config import TWITTER
            if all(TWITTER.values()):
                self._client = Client(
                    TWITTER['CONSUMER KEY'],
                    TWITTER['CONSUMER SECRET'],
                    TWITTER['ACCESS TOKEN'],
                    TWITTER['ACCESS TOKEN SECRET'])
        self._account = self._client.accounts(account)
        
    @property
    def account(self):
        return getattr(self, '_account')
    
    def __repr__(self):
        return "<account name=[{name}] and id=[{id}]>".format(
            name=self._account.name,
            id=self._account.id)

    def __str__(self):
        return ("<[EasyAuth] located at mem_addr=[{id}]>").format(id=id(self))


class YAMLFileWriter:
    """ <[TwitterYAMLFileWriter]> class is an over-engineered 
    callable class to write a hidden yaml file.

    :params consumer_key: str, alphanumeric string
    :params consumer_secret: str, alphanumeric string
    :params access_token: str, alphanumeric string
    :params access_token_secret: str, alphanumeric string
    """
    def __init__(self, 
        consumer_key,
        consumer_secret, 
        access_token, 
        access_token_secret,
        path=os.path.dirname(os.path.dirname(__file__))):

        self._path = os.path.join(path,'.twitter.yaml')
        self._store = {
            'CONSUMER KEY':consumer_key, 
            'CONSUMER SECRET':consumer_secret,
            'ACCESS TOKEN':access_token,
            'ACCESS TOKEN SECRET':access_token_secret
        }

    def __call__(self):
        with open(self._path, 'w') as new_yaml_file:
            yaml.dump(self._store, new_yaml_file, default_flow_style=True)

    @property
    def success(self):
        return os.path.exists(self._path)

    def __repr__(self):
        return ("<[TwitterYAMLFileWriter] " 
                "located at mem_addr=[{id}]>").format(id=id(self))





