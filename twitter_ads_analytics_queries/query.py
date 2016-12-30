"""
TODO: module doc-strings
"""
import time 

from twitter_ads.campaign import LineItem, Campaign
from twitter_ads.enum import METRIC_GROUP, PLACEMENT, GRANULARITY

from twitter_ads_analytics_queries.response import TwitterAnalyticsResponse
from twitter_ads_analytics_queries.credentials import EasyAuth
from twitter_ads_analytics_queries.utils import (
    format_time, 
    handle_response, 
    line_item_generator
)

def get_line_items(account, metric_groups, **kwargs):
    """ Get stats for all line items for a given account.

    :params account: str, alphanumeric string
    :params metric_groups: list, 1 or more metric groups
    :params kwargs: args related to analytics queries
    """
    try:
        entry = EasyAuth(account, "TWITTER_CREDENTIALS")
    except:
        entry = EasyAuth(account)
    finally:
        if kwargs.get('creds', None):
            creds = kwargs.get('creds')
            entry = EasyAuth(account, creds)
    
    start = kwargs.get('start_time')
    end = kwargs.get('end_time')
    if start and end:
        kwargs.update({
            'start_time':format_time(start),
            'end_time':format_time(end)
            })

    line_item_resources = list(entry.account.line_items())
    campaigns = list(entry.account.campaigns())
    lookup = {campaign.id:campaign.name for campaign in campaigns}
    line_items = {line_item.id: lookup.get(line_item.campaign_id)
        for line_item in line_item_resources}
    line_item_ids = list(line_items.keys())

    response = []

    for ids in line_item_generator(line_item_ids):
        job = LineItem.queue_async_stats_job(
            account=entry.account, 
            ids=ids,
            metric_groups=metric_groups,
            **kwargs)

        result = LineItem.async_stats_job_result(
            entry.account, job['id'])
    
        while not result['url']:
            result = LineItem.async_stats_job_result(
                entry.account, job['id'])
            time.sleep(5)
        
        batch = LineItem.async_stats_job_data(
            entry.account, result['url'])

        response += batch['data']

    data = handle_response(response, start, end, line_items)
    
    return TwitterAnalyticsResponse('Line Item', data)
    

def get_campaigns(account, metric_groups, **kwargs):
    """ Get stats for all campaigns for a given account.

    :params account: str, alphanumeric string
    :params metric_groups: list, 1 or more metric groups
    :params kwargs: args related to analytics queries
    """
    try:
        entry = EasyAuth(account, "TWITTER_CREDENTIALS")
    except:
        entry = EasyAuth(account)
    finally:
        if kwargs.get('creds', None):
            creds = kwargs.get('creds')
            entry = EasyAuth(account, creds)

    start = kwargs.get('start_time')
    end = kwargs.get('end_time')
    if start and end:
        kwargs.update({
            'start_time':format_time(start),
            'end_time':format_time(end)
            })

    campaign_resources = list(entry.account.campaigns())
    campaigns = {campaign.id:campaign.name 
        for campaign in campaign_resources}
    campaign_ids = list(campaigns.keys())

    response = []

    for ids in line_item_generator(campaign_ids):
        job = Campaign.queue_async_stats_job(
            account=entry.account, 
            ids=ids,
            metric_groups=metric_groups,
            **kwargs)

        result = Campaign.async_stats_job_result(
            entry.account, job['id'])
    
        while not result['url']:
            result = Campaign.async_stats_job_result(
                entry.account, job['id'])
            time.sleep(5)
        
        batch = Campaign.async_stats_job_data(
            entry.account, result['url'])

        response += batch['data']

    data = handle_response(response, start, end, campaigns)

    return TwitterAnalyticsResponse('Campaign', data)














