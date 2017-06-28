import requests
import json
import datetime
from dateutil.parser import parse

def is_date(x):
    if x is None:
        return False
    if type(x) is bool:
        return False
    if len(x)<9:
        return False
    try:
        parse(x)
        return True
    except:
        return False


json_deal = requests.get('https://skylarkdrones.pipedrive.com/v1/deals?api_token=d4d19d807af6c5e9861b0fa81d1cf403ea88e402')
intermediate = json_deal.text
buffer = json.loads(intermediate)
deal_table = buffer['data']
# row = deal_table[0]
list_of_columns = list(deal_table[0].keys( ))

print(str(len(list_of_columns))+' number of keys have been found.')
json_deal_fields = requests.get('https://skylarkdrones.pipedrive.com/v1/dealFields?api_token=d4d19d807af6c5e9861b0fa81d1cf403ea88e402')
deal_fields = json.loads(json_deal_fields.text)
fields = deal_fields['data']

column_name = {}
for x in fields:
    for i in range(0,len(list_of_columns)):
        if x['key'] == list_of_columns[i] :
            column_name[list_of_columns[i]] = x['name']

for column in list_of_columns:
    flag = False
    for key in column_name:
        if key == column:
            flag = True
    if flag == False:
        column_name[column] = column

final_list_of_columns = []
for x in list_of_columns:
    final_list_of_columns.append({'name':column_name[x], 'dataType':'string'})

for j in range(0,len(deal_table)):
    for x in list_of_columns:
        for key in deal_table[j]:
            if deal_table[j][key] is None:
                continue
            elif type(deal_table[j][key]) == int:
                for i in range(0,len(final_list_of_columns)):
                    if final_list_of_columns[i]['name'] == column_name[key]:
                        final_list_of_columns[i]['dataType'] = 'int64'
            elif is_date(deal_table[j][key]):
                for i in range(0,len(final_list_of_columns)):
                    if final_list_of_columns[i]['name'] == column_name[key]:
                        final_list_of_columns[i]['dataType'] = 'dateTime'
                        buf=parse(deal_table[j][key])
                        deal_table[j][key]=buf.strftime("%m/%d/%Y")
            elif type(deal_table[j][key]) == bool:
                for i in range(0,len(final_list_of_columns)):
                    if final_list_of_columns[i]['name'] == column_name[key]:
                        final_list_of_columns[i]['dataType'] = 'boolean'
            elif deal_table[j][key]!=None:
                deal_table[j][key] = str(deal_table[j][key])


json_table_1 = {'name':'deals', 'columns':final_list_of_columns}
json_tables = [json_table_1]
json_data_set = {'name':'Practice_1', 'tables':json_tables}
json_string_dataset = json.dumps(json_data_set)

with open('DataSet','w') as file:
    json.dump(json_data_set,file)

final_list_of_rows =[]
for row in deal_table:
    row1={}
    for key in row:
        row1[column_name[key]]=row[key]
    final_list_of_rows.append(row1)

row_final ={'rows':final_list_of_rows}
with open('rows','w') as r:
    json.dump(row_final,r)

with open('see_row_final','w') as file:
    json.dump(row_final,file,indent=4)
