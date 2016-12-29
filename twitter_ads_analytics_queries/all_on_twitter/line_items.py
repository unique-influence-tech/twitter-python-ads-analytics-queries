"""
TODO: module docstrings
"""
import query

from datetime import datetime, timedelta 
from twitter_ads.enum import METRIC_GROUP, PLACEMENT, GRANULARITY 


def yesterday(account=None):
    """ Get 'ALL_ON_TWITTER' campaign
    statstics for the last day.

    :params account: str, account id
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]
    start = datetime.today()-timedelta(1)
    end = datetime.today()
    period = GRANULARITY.DAY
    ad_type = PLACEMENT.ALL_ON_TWITTER

    return query.get_line_items(
            account=account,
            start_time=start.strftime('%Y-%m-%d'),
            end_time=end.strftime('%Y-%m-%d'),
            metric_groups=metrics, 
            granularity=period, 
            placement=ad_type
           )


def last_14_days(account=None):
    """Get 'ALL_ON_TWITTER' campaign
    statstics for the last 14 days.

    :params account: str, account id
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]
    start = datetime.today()-timedelta(14)
    end = datetime.today()-timedelta(1)
    period = GRANULARITY.DAY
    ad_type = PLACEMENT.ALL_ON_TWITTER

    return query.get_line_items(
            account=account,
            start_time=start.strftime('%Y-%m-%d'),
            end_time=end.strftime('%Y-%m-%d'),
            metric_groups=metrics, 
            granularity=period, 
            placement=ad_type
           )


def last_30_days(account=None):
    """Get 'ALL_ON_TWITTER' campaign
    statstics for the last 30 days.

    :params account: str, account id
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]
    start = datetime.today()-timedelta(30)
    end = datetime.today()-timedelta(1)
    period = GRANULARITY.DAY
    ad_type = PLACEMENT.ALL_ON_TWITTER

    return query.get_line_items(
            account=account,
            start_time=start.strftime('%Y-%m-%d'),
            end_time=end.strftime('%Y-%m-%d'),
            metric_groups=metric_groups, 
            granularity=period, 
            placement=ad_type
           )
        
        
def custom_date_range(account=None, start=None, end=None):
    """Get 'ALL_ON_TWITTER' campaign
    statstics for a custom date range.

    :params account: str, account id
    :params start: str, YYYY-MM-DD
    :params end: str, YYYY-MM-DD
    """
    metrics = [
        METRIC_GROUP.BILLING,
        METRIC_GROUP.ENGAGEMENT,
        METRIC_GROUP.WEB_CONVERSION
    ]

    period = GRANULARITY.DAY
    ad_type = PLACEMENT.ALL_ON_TWITTER

    return query.get_line_items(
            account=account,
            start_time=start,
            end_time=end,
            metric_groups=metrics, 
            granularity=period, 
            placement=ad_type
           )




