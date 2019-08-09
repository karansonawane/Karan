

import pandas as pd


physics_score = [15,12,8,8,7,7,7,6,5,3]
history_score = [10,25,17,11,13,17,20,13,9,15]

x = pd.Series(physics_score)
y = pd.Series(history_score)
r = x.cov(y)/(x.std()*y.std())

print("%.3f" %r)