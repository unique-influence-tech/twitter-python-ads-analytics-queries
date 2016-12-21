"""
TODO: module docstrings
"""

class TwitterAnalyticsResponse:
    """A list-like class with a few more 
    methods to help with aggregated Twitter Ads
    responses.

    :params records: list, a list of dict objects
    """
    def __init__(self, entity, records):
        super(TwitterAnalyticsResponse, self).__init__()
        self._records = records
        self.__copy = records.copy()
        self._type = entity

    def __setitem__(self, key, value):
        self._records[key] = value

    def __getitem__(self, key):
        return self._records[key]

    def __add__(self, response_obj):
        if isinstance(response_obj, TwitterAnalyticsResponse):
            self._records.extend(response_obj.records)

    def __len__(self):
        return len(self._records)

    def include_only(self, *args):
        """ This is an include only filter. 
        
        :params args: str, fields associated with metric groups
        """
        comp = set(args)
        comp.update(('date','id','name'))

        filtered = list()
        for obj in self._records:
            record = dict()
            for key in obj.keys():
                if str(key) in comp:
                    record.update({key:obj[key]})
            filtered.append(record)
        self._records = filtered

    def reset(self):
        """Resets data back to original data."""
        self._records = self.__copy

    @property
    def records(self):
        return self._records

    def __repr__(self):
        return ("<[{type} TwitterAnalyticsResponse]" 
               " located at mem_addr=[{id}]>"
               ).format(type=self._type, id=id(self))
