## Introduction

This package acts like an add-on to the [Twitter Ads SDK](http://twitterdev.github.io/twitter-python-ads-sdk/). It is designed to make Twitter
Ads Analytics requests more simple by doing two things:

* Performing multiple asynchronous request and retrieval to the Twitter Analytics endpoint 
* Aggregating and transforming responses into a `list` of mappings that include id, date and campaign name

The mappings are daily records: 

`{campaign_name:'', 'id':'', 'date':'', metric_1:'', metric_2:'', metric_3:''}` 

This makes importing into a database very easy.:thumbsup::thumbsup::thumbsup:

## Installation

Coming soon

## Usage

#### Abstracted Credentials :white_check_mark:

One of the most annoying parts of making requests is constantly providing credentials. :sweat: 

I've given options to the user to remove that process. You can supply credentials in the following ways:

* Find the `/your/pip/installed/package/directory` and manually add credentials to the `config.py` 

* Generate a `TWITTER_CREDENTIALS` variable in your environment file that points to a yaml version of your credentials:

```
$ cd /your/pip/installed/package/directory
$ source secure_twitter_creds.bash/where/you/want/to/store/creds /your/shell/environment/.file
---------------------------------<>
Adding TWITTER_CREDENTIALS variable to environment file..
Paste your consumer key here:
XXXXXX
Paste your consumer secret key here:
XXXXXX
Paste your access key here:
XXXXXX
Paste your access secret key here:
XXXXXX
YAML write successful.
Add variable to environment..
TWITTER_CREDENTIALS variable adding: SUCCESS
/your/shell/environment/.file sourced.
----------------------------------<>
```

If you don't want to use these options, you can bootstrap calls by supplying a `creds={}` argument to  `get_campaigns` and `get_line_items` in the `query.py` file.

#### Simplified Querying :white_check_mark:

```
$ python
>>> import twitter_ads_analytics_queries
>>> request = twitter_ads_analytics_queries.twitter.campaigns.yesterday(account='xxxxxx')
>>> request.records
[{'conversion_sign_ups_metric':0, 'conversion_site_visits_order_quantity_view': 0, ... }, ...] 
```

## Testing

Coming soon

## Additional Notes

Coming soon
