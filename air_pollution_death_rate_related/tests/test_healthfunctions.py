'''Tests the functions in healthdata_module.py, which are used to clean the health data'''
import pandas as pd
from ..scripts import healthdata_module
from ..scripts import healthdata_cleanup

#Test data
DF1 = pd.read_csv('air_pollution_death_rate_related/data/test_data_1.csv')
DF2 = pd.read_csv('air_pollution_death_rate_related/data/test_data_2.csv')

def test_func_changing_names():
    '''Testing the first function, renaming columns.'''
    df_renamed = healthdata_module.changing_col_name(DF1, 'Year', 'year')
    assert 'year' in list(df_renamed.columns)
    assert 'Year' not in list(df_renamed.columns)

def test_func_split_col():
    '''Testing the second function, splitting a column value into two strings.'''
    df_split = healthdata_module.split_column(DF2, 'County', 'County', 'State Abrev', ',')
    assert 'State Abrev' in list(df_split.columns)
    assert ' WA' in list(df_split['State Abrev'])
    assert 'King' in list(df_split['County'])

def test_func_choose_data():
    '''Testing the third function, choosing data by year.'''
    df_2015 = healthdata_module.choose_data_by_year(healthdata_cleanup.COUNTY_POP_MERGE, 2015)
    assert '2015' in list(df_2015['Year'])
    assert '2001' not in list(df_2015['Year'])

def test_func_concat():
    '''Testing the fourth function, which concatenates the functions vertically.'''
    df_concat = healthdata_module.concat_dfs_vertically(DF1, DF2)
    assert len(df_concat) == 4
