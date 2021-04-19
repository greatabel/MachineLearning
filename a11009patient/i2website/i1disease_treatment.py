import pandas as pd
import csv
  
mydict = {}
mysymptom_dict = {}

def process():
	# read csv file
	origianl_df = pd.read_csv("../processed_data/GlobalSickinfo_20210412.csv", encoding = 'utf-8', 
		nrows=8000,  error_bad_lines=False, warn_bad_lines=False)

	# print(origianl_df.head())

	df = origianl_df.dropna(subset=['DiseName', 'PrescrptInfo'])
	  
	# concatenate the string
	# df['branch'] = df.groupby(['DiseName'])['PrescrptInfo'].transform(lambda x : ' '.join(x))
	# drop duplicate data
	df = df.drop_duplicates()   
	# show the dataframe
	print('-'*30)
	for index, row in df.iterrows():
		# if index < 50:
		if row["DiseName"] != '' and row["PrescrptInfo"] != '':
			print(row["DiseName"], '#'*10, row["PrescrptInfo"])
			if row["DiseName"] not in mydict:
				mydict[row["DiseName"]] = [row["PrescrptInfo"]]
			else:
				new_list = mydict[row["DiseName"]]
				new_list.append(row["PrescrptInfo"])
				mydict[row["DiseName"]] = new_list

	print(mydict)
	return mydict


def process_symptom():
	# read csv file
	origianl_df = pd.read_csv("../processed_data/GlobalSickinfo_20210412.csv", encoding = 'utf-8', 
		nrows=8000,  error_bad_lines=False, warn_bad_lines=False)

	# print(origianl_df.head())

	df = origianl_df.dropna(subset=['Symptom', 'PrescrptInfo'])
	  
	# concatenate the string
	# df['branch'] = df.groupby(['DiseName'])['PrescrptInfo'].transform(lambda x : ' '.join(x))
	# drop duplicate data
	df = df.drop_duplicates()   
	# show the dataframe
	print('-'*30)
	for index, row in df.iterrows():
		# if index < 50:
		if row["Symptom"] != '' and row["PrescrptInfo"] != '':
			print(row["Symptom"], '#'*10, row["PrescrptInfo"])
			if row["Symptom"] not in mysymptom_dict:
				mysymptom_dict[row["Symptom"]] = [row["PrescrptInfo"]]
			else:
				new_list = mysymptom_dict[row["Symptom"]]
				new_list.append(row["PrescrptInfo"])
				mysymptom_dict[row["Symptom"]] = new_list

	print(mysymptom_dict)
	return mysymptom_dict

if __name__ == "__main__":
	process()
	# process_symptom()