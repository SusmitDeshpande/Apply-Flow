import os
import pandas as pd
from setup import setup

setup()
print("Setting up test file done...\nTest file path : ", os.path.abspath("../other/test.csv"))

print("\n*** WELCOME TO APPLYFLOW ***")

file_dir = input("Enter the File Directory : ")
df = pd.read_csv(file_dir)
# print(df)


