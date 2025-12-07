import pandas as pd

def setup():

    df = pd.DataFrame([['mail@email.com', 'xyz uvw', 'Data Science', 'Pune'],['mail2@email.com', 'abc def', 'AI', 'Pune']], columns=['email', 'name', 'position', 'location'])
    df.to_csv("../other/test.csv", index=False)