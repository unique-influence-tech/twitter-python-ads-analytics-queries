"""
TODO: module docstrings
"""
from datetime import datetime, timedelta 
from twitter_ads.enum import METRIC_GROUP, PLACEMENT, GRANULARITY 
from twitter_ads_analytics_queries.query import get_campaigns

def yesterday(account=None):
    """
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]
    start = datetime.today()-timedelta(1)
    end = datetime.today()
    period = GRANULARITY.DAY
    ad_type = PLACEMENT.PUBLISHER_NETWORK

    return get_campaigns(
            account=account,
            start_time=start.strftime('%Y-%m-%d'),
            end_time=end.strftime('%Y-%m-%d'),
            metric_groups=metrics, 
            granularity=period, 
            placement=ad_type
           )


def last_14_days(account=None):
    """
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]
    start = datetime.today()-timedelta(14)
    end = datetime.today()-timedelta(1)
    period = GRANULARITY.DAY
    ad_type = PLACEMENT.PUBLISHER_NETWORK

    return get_campaigns(
            account=account,
            start_time=start.strftime('%Y-%m-%d'),
            end_time=end.strftime('%Y-%m-%d'),
            metric_groups=metrics, 
            granularity=period, 
            placement=ad_type
           )


def last_30_days(account=None):
    """
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]
    start = datetime.today()-timedelta(30)
    end = datetime.today()-timedelta(1)
    period = GRANULARITY.DAY
    ad_type = PLACEMENT.PUBLISHER_NETWORK

    return get_campaigns(
            account=account,
            start_time=start.strftime('%Y-%m-%d'),
            end_time=end.strftime('%Y-%m-%d'),
            metric_groups=metric_groups, 
            granularity=period, 
            placement=ad_type
           )
        
        
def custom_date_range(account=None, start=None, end=None):
    """
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]

    period = GRANULARITY.DAY
    ad_type = PLACEMENT.PUBLISHER_NETWORK

    return get_campaigns(
            account=account,
            start_time=start,
            end_time=end,
            metric_groups=metrics, 
            granularity=period, 
            placement=ad_type
           )




