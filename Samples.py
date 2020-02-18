import chart_studio.plotly as py
import cufflinks as cf
import pandas as pd
import numpy as np

py.sign_in('lyuboychuk', 'E6WUCFztzEEavxFgUJ1b')


df = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B']).cumsum()
df.iplot(filename='line-example')
