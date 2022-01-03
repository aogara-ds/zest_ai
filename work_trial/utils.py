import pandas as pd

"""
Functions to be used by notebooks in the pipeline. 

"""

def bad_rate_by_category(data, col_name, hist = False):
    """
    Provided the name of a categorical column and our merged dataset, returns
    a dataframe of default rates by category in the provided column. 
    
    """
    df = data.groupby(col_name).agg({'bad': ['sum', 'count']})
    df['bad_rate'] = df[('bad', 'sum')] / df[('bad', 'count')]
    df = df.sort_values('bad_rate')
    
    # TODO: Make this work? Or delete. 
    if hist == True:
        return df[['bad_rate']].hist()
    
    else:
        return df

def add_entry_to_dictionary(data, data_dict, variable: str, eda_category: str, categorical: bool):
    """
    Adds the provided variable to the data dictionary. 
    Inserts the provided eda_category and categorical flag. 
    Internally calculates and inserts var_dtype and coverage.  
    Returns the updated data dictionary. 
    
    Requirements:
        * New variable must exist in data beforehand
    
    """
    # Check for other entries under the same name
    duplicate = data_dict.loc[data_dict['variable']==variable].shape[0]
    if duplicate == True:
        # If row already exists, drop it and replace it
        data_dict = data_dict.loc[~data_dict['variable']==variable]
    
       
    # Generate new row for data dictionary
    new_row = {
        'variable': variable,
        'eda_category': eda_category,
        'categorical': categorical
    }
    
    # Append new row to data dictionary
    data_dict = data_dict.append(new_row, ignore_index=True)
    
    # Recalculate standard information about data dictionary
    # TODO: This doesn't work. Can't assume order of vars. Lambda please. 
    data_dict.loc[data_dict['variable']==variable, 
                  'var_dtype'] = data[variable].dtype
    data_dict.loc[data_dict['variable']==variable, 
                  'coverage'] = data[variable].count() / data.shape[0]
    
    return data_dict

def clean_name(x):
    # Check the name is a string
    if type(x) != str:
        return None
    
    # Establish which characters will be replaced
    name_cleaning_dict = {' ': '_',
                         '\s+': '_',
                         '\t': ' ',
                         '(': '',
                         ')': '',
                         '$': 'amt',
                         '#': 'num',
                         '%': 'percent',
                         ',': '',
                         '-': '_',
                         '/': '_',
                         '___': '_',
                         '__': '_'}
    
    # Replace characters according to dict
    for k, v in name_cleaning_dict.items():
        x = x.replace(k, v)
        
    # Lowercase, no whitespace
    x = x.lower()
    x = x.strip()
    
    return x    



