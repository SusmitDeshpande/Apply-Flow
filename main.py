import os
import pandas as pd
from src.setup import setup
from src.emailService import send_email

setup()
print("Setting up test file done...\nTest file path : ", os.path.abspath("../other/test.csv"))

print("\n*** WELCOME TO APPLYFLOW ***")

file_dir = input("Enter the File Directory : ")
df = pd.read_csv(file_dir)
# print(df)
email = 'satejsdeshpande@gmail.com'
send_email(email)