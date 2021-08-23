# -*- coding: utf-8 -*-
"""
@author: GITAA
"""
# =============================================================================
# Difference between logical and bitwise
# =============================================================================

# 0-False 
# 1-True

#%%

# Comparing boolean values
# Transalates to comparing True or Flase (Truth Tables)
print(0 or 1)
print(0 | 1)

print(0 and 1)
print(0 & 1)

#%%

# Comparing 0 and 3
# Any non-zero number is also considered to be True

0 or 3
0 | 3

0 and 3
0 & 3

#%%
1 or 3
1 | 3

1 and 3
1 & 3

#%%

2 or 3
2 | 3

2 and 3
2 & 3


# =============================================================================
# How to use bitwise operators?
# =============================================================================

#%%

# Bitwise operators on pandas dataframe

import pandas as pd

# Reading data
df=pd.read_csv('flavors_of_cacao.csv')

# Gist of data
df.info()

# Bitwise and conditional operators together
# Subsetting data where Rating>=3 and Company Location is France

# No. of records where Rating>=3
counts1=len(df[(df['Rating'] >= 3)])

# No. of records where Company Location is France
counts2=df['Company Location'].value_counts()


# With '&' both these conditions should be obeyed
# Records that satisfy both these conditions are stored in df1
df1=df[(df['Rating'] >= 3) and (df['Company Location'] == 'France')]
df1=df[(df['Rating'] >= 3) & (df['Company Location'] == 'France')]


# With '|' it is enough if one of the two conditions should be obeyed
# Records that satisfy even one of the conditions are stored in df1
df2=df[(df['Rating'] >= 3) | (df['Company Location'] == 'France')]

'''
Note- Other bitwise operators have not been covered because we can achieve
the outputs that they give using a combination of conditional operators, 
bitwise &/| and buit is python functions like isin, notin etc.

While these operators can be performed in python they are not relevant 
from data science perspective
'''

#%%
import numpy as np

# Consider two arrays
a=np.array([[0, 4, 4, 2],[1, 3, 0, 2],[3, 2, 4, 4]])
b=np.array([[6, 9, 8, 6],[7, 7, 9, 6],[8, 6, 5, 7]])

a and b
a or b


'''
Why logical operator won't work?
Logical operators won't work because they are designed to work 
on operands with single value

Bitwise operators are designed to work on operands with 
single value and arrays
'''

# Bitwise operator as intersecion 
a & b 
# Bitwise operator as intersecion 
a | b

# Bitwise and conditional operators together
(a > 3) | (b > 8)


#%%
