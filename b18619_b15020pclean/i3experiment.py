import re, collections
import pandas as pd 
from termcolor import colored, cprint

from common import get_words, probability_model, valid_telephone_number
from i2bayes import correct_word, correct_words




orginal_txt = ''
df = pd.read_csv("datasets/hospital_dirty.csv")

print('1 -----------------------------')
original = 'surgery patients who were taking heart drugs caxxed beta \
bxockers before coming to the hospitax who were kept on the beta bxockers \
during the period just before and after their surgery'
after_check = correct_words(original)
print('Long sentence test(start):', "="*10)

text = colored('auto_correct test:', 'red', attrs=['reverse', 'blink'])
print(text)
if original != after_check:
	print(original)
	print('\n')
	print(after_check)
	print('-'*20)

original = 'surge patien who were taking heart drugs caxxed beta \
bxockers before coming to the hospitax who were kept on the beta bxockers \
during the period just before and after their sur'
after_check = correct_words(original)
print('Long sentence test(start):', "="*10)
text = colored('auto_completion test:', 'green', attrs=['reverse', 'blink'])
print(text)

if original != after_check:
	print(original)
	print('\n')
	print(after_check)
	print('-'*20)

print('Long sentence test(end):', "="*10)

print('2 -----------------------------')
print('Words test:')

i = 0.0

length = 1000
for index, row in df[0:length].iterrows():
    # orginal_txt += ' ' + row['HospitalName']
    # orginal_txt += ' ' + row['Address1']
    # orginal_txt += ' ' + row['MeasureName']
    original = row['HospitalName']

    # print(original)
    after_check = correct_words(original)
    if original != after_check:
    	print(original)
    	print(after_check)
    	l = colored('-'*20, 'yellow', attrs=['reverse', 'blink'])
    	print(l)
    	i += 1

ratio = i* 100/ length
print('dirty datasets have wrong HospitalName radio:', ratio, '%')

print('3 -----------------------------')
r_phone_number = '2053258100'
w_phone_number = '000111111100'
check = valid_telephone_number(r_phone_number)
print(check)
print('%s phone-number check results %s' %(r_phone_number, check))
check = valid_telephone_number(w_phone_number)
print(check)
print('%s phone-number check results %s' %(r_phone_number, check))

