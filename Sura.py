import pandas as pd
import glob
for filename in glob.glob('dataset/tex*ALL.csv'):
	data = pd.read_csv(filename)
	print(filename, data['tex*ALL.csv'].min())