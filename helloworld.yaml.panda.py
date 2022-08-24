import pandas as pd
df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
df.to_json('df-example-out')
