import re
import pandas as pd

spis_num = []

with open(r'Path#1', 'r') as lines:
    for line in lines:
        number = re.findall(r'^([0-9]*).([0-9]*)', line)
        pref, num = number[0]
        if num == '':
            continue
        else:
            mob_number = '7' + pref + num
            spis_num.append(mob_number)

df = pd.DataFrame(spis_num,columns=['Numbers'])

df.to_csv(r'C:\Users\My workstation\Desktop\Работа\Git_Repo\docs\1channel_Avtoobzvonshik\numbers.csv', index=False)