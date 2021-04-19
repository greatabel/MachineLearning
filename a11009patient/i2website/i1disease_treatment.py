import pandas as pd
import csv
from datetime import date, datetime
import jellyfish
import traceback

mydict = {}
mysymptom_dict = {}
p_year = {}

def calculate_age(born):
    today = date.today()
    return today.year - born.year

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
				if row["PrescrptInfo"] not in new_list:
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
		# 为了比较效率
		if index < 2000:
			if row["Symptom"] != '' and row["PrescrptInfo"] != '':
				print(row["Symptom"], '#'*10, row["PrescrptInfo"])
				if row["Symptom"] not in mysymptom_dict:
					mysymptom_dict[row["Symptom"]] = [row["PrescrptInfo"]]
				else:
					new_list = mysymptom_dict[row["Symptom"]]
					if row["PrescrptInfo"] not in new_list:
						new_list.append(row["PrescrptInfo"])
					mysymptom_dict[row["Symptom"]] = new_list

	print(mysymptom_dict)
	return mysymptom_dict


def process_age():
	# read csv file
	origianl_df = pd.read_csv("../processed_data/ClinicPatient_20210412.csv", encoding = 'utf-8', 
		nrows=8000,  error_bad_lines=False, warn_bad_lines=False)

	# print(origianl_df.head())

	df = origianl_df.dropna(subset=['GlobalKey', 'Birthday'])
	  
	# concatenate the string
	# df['branch'] = df.groupby(['DiseName'])['PrescrptInfo'].transform(lambda x : ' '.join(x))
	# drop duplicate data
	df = df.drop_duplicates()   
	# show the dataframe
	print('-'*30)
	for index, row in df.iterrows():
		# 为了比较效率
		# if index < 100:
		if row["GlobalKey"] != '' and row["Birthday"] != '':
			print(row["GlobalKey"], '#'*10, row["Birthday"])
			if row["GlobalKey"] not in mysymptom_dict:
				try:
					date_of_birth = datetime.strptime(row["Birthday"], '%d/%m/%Y %H:%M:%S')
					y = calculate_age(date_of_birth)
					print(date_of_birth, '@'*20, y)
					p_year[row["GlobalKey"]] = y
				except Exception:
					traceback.print_exc()


	# print(p_year)
	return p_year


def process_drugday_age(input_PrescrptInfo):
	xs, ys = [], []

	p_year = process_age()
	# read csv file
	origianl_df = pd.read_csv("../processed_data/GlobalSickinfo_20210412.csv", encoding = 'utf-8', 
		nrows=8000,  error_bad_lines=False, warn_bad_lines=False)

	# print(origianl_df.head())

	df = origianl_df.dropna(subset=['DrugDay', 'PrescrptInfo'])
	  
	# concatenate the string
	# df['branch'] = df.groupby(['DiseName'])['PrescrptInfo'].transform(lambda x : ' '.join(x))
	# drop duplicate data
	df = df.drop_duplicates()   
	# show the dataframe
	print('-'*30)
	for index, row in df.iterrows():
		# 为了比较效率
		if index < 3000:
			if  row["PrescrptInfo"] != '' and row['DrugDay'] != '' and row['PatientKey'] != '':
				sname = row["PrescrptInfo"]
				tname = input_PrescrptInfo
				c1 = jellyfish.jaro_distance(sname, tname)
				if c1 > 0.6 or (tname in sname):
					print('*'*20)
					ys.append(row['DrugDay'])
					year = p_year[row['PatientKey']]
					print(row['PatientKey'], ' year->', p_year[row['PatientKey']])
					xs.append(year)

	print(xs, ys)
	return xs, ys

if __name__ == "__main__":
	# process()
	process_drugday_age()
	# process_symptom()