"""
TODO: module docstrings
"""
import json
import yaml
import sys

from pytz import timezone
from datetime import datetime, timedelta
from os.path import dirname, abspath, join



def format_time(date, from_tz='US/Central', to_tz='UTC'):
    """Put string date into acceptable Twitter form.
    
    For more detail see:
        https://dev.twitter.com/ads/basics/timezones

    :params date: str, date in YYYY-MM-DD
    :params from_tz: pytz.timezone obj, from timezone
    :params to_tz: pytz.timezone obj, to timezone
    """
    read = datetime.strptime(date, "%Y-%m-%d")
    CST = read.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=timezone(from_tz))
    UTC = CST.astimezone(timezone(to_tz))

    return UTC 


def generate_date_list(start_date, end_date):
    """ Generate a list of dates given start and 
    and end dates.

    :params start_date: str, date in YYYY-MM-DD
    :params end_date: str, date in YYYY-MM-DD
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_range = []

    for _ in range((end-start).days):
        date_range.append((start+timedelta(_)).strftime('%Y-%m-%d'))

    return date_range


def handle_response(response, start_date=None, end_date=None, names=None):
    """ This takes a list of Twitter Analytics responses and transforms them
    a usable list of dictionaries to input into a database. 

    :params response: list, Twitter Analytics responses
    :params start_date: str, YYYY-MM-DD
    :params end_date: str, YYYY-MM-DD
    :params names: dict, a lookup to associate id values with name values 
    """
    parsed = []

    if start_date and end_date:
        date_range = generate_date_list(start_date, end_date)
    else:
        # see _standard_params in resource.py
        end = datetime.utcnow()
        start = (end-timedelta(seconds=604800)).strftime('%Y-%m-%d')
        date_range = generate_date_list(start, end.strftime('%Y-%m-%d'))

    for record in response:
        
        id_data = record.get('id_data')
        entity_id = record.get('id')
        stats = flatten_record(id_data[0].get('metrics'))

        for idx, day in enumerate(date_range):
            row = {'date':day,'id':entity_id}
            if names:
                row.update(name=names[entity_id])
            for metric in stats:
                if str(stats[metric]) != 'None':
                    row.update({metric:stats[metric][idx]})
                else:
                    row.update({metric:0})
            parsed.append(row)

    return parsed


def flatten_record(row):
    """ Remove nested dictionaries from
    a request.

    :params row: dict
    """
    store = dict()

    for key in row.keys():
        if not isinstance(row[key], dict):
            store.update({key:row[key]})
        else:
            nested = row[key]
            for _key in nested.keys():
                name = '{}_{}'.format(key,_key)
                store.update({name:nested[_key]})
            
    return store


def line_item_generator(ids):
    """ Generator that yields sets of 20 line item ids.
    
    :params ids: list, list of line item ids
    """
    for step in range(0, len(ids), 20):
        if step < len(ids):
            yield ids[step:step+20]
        else:
            yield ids[step:len(ids)]
























