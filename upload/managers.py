from django.db.models.query import QuerySet
from django_pandas.io import read_frame
from django.db import models



def to_dataframe(self, fieldnames=(), verbose=True, index=None,
                     coerce_float=False, datetime_index=False):
        """
        Returns a DataFrame from the queryset
        Paramaters
        -----------
        fieldnames:  The model field names(columns) to utilise in creating
                     the DataFrame. You can span a relationships in the usual
                     Django ORM way by using the foreign key field name
                     separated by double underscores and refer to a field
                     in a related model.
        index:  specify the field to use  for the index. If the index
                field is not in fieldnames it will be appended. This
                is mandatory for timeseries.
        verbose: If  this is ``True`` then populate the DataFrame with the
                 human readable versions for foreign key fields else
                 use the actual values set in the model
        coerce_float:   Attempt to convert values to non-string, non-numeric
                        objects (like decimal.Decimal) to floating point.
        datetime_index: specify whether index should be converted to a
                        DateTimeIndex.
        """

        return read_frame(self, fieldnames=fieldnames, verbose=verbose,
                          index_col=index, coerce_float=coerce_float,
                          datetime_index=datetime_index)

