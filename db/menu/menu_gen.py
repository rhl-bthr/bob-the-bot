import json

month = '09'

for i in range(1,31+1):
    fname = f'{str(i).zfill(2)}-{month}-2018.json'
    content = {'breakfast': [f'{str(i).zfill(2)}-{month}'],
               'lunch': [f'{str(i).zfill(2)}-{month}'],
               'dinner': [f'{str(i).zfill(2)}-{month}']
              }
    with open(fname,'w') as f:
        json.dump(content,f)
