import requests
import json
import datetime



json_dl = requests.get('https://skylarkdrones.pipedrive.com/v1/deals?api_token=d4d19d807af6c5e9861b0fa81d1cf403ea88e402')
intermediate = json_dl.text
intermediate = intermediate.replace('4cb7188a28ebe6a85f349baf8d5408125f95d400','website')
intermediate = intermediate.replace('974c30ccc0759260072130b6a3fc318c4c66b531','leadsource')
intermediate = intermediate.replace('ed38a67023d58734f40c41cdc27b525755071b6a','designation')
buffer = json.loads(intermediate)
tables = buffer['data']

columns = []

full_list_of_columns = list(buffer['data'][0].keys( ))

print(str(len(full_list_of_columns))+' no of keys found')
list_of_refined_columns = []

rows=buffer['data']
for i in range(0,len(rows)):
    for key in rows[i]:
        if(type(rows[i][key])== dict):
            rows[i][key] = 'difficult'
        

for x in full_list_of_columns:
    if type(rows[0][x]) == int :
       list_of_refined_columns.append({'name':x,'dataType':'Int64' })
    # elif 'date' in x or 'time' in x:
    #     list_of_refined_columns.append({'name':x,'dataType':'Datetime' })
    # elif type(rows[0][x]) == str:
    else:
        list_of_refined_columns.append({'name':x,'dataType':'String' })
    
#    elif 'count' in x or 'id' in x:
#       list_of_refined_columns.append({'name':x,'dataType':'Int64' })
#    else:
#       list_of_refined_columns.append({'name':x,'dataType':'String' })
 
#for i in range(0,len(rows)):
#    for x in full_list_of_columns:
#        if x['dataType'] == 'Int64' and type(rows[i][x['name']]) != int:
#            rows[i][x['name']] = int(rows[i][x['name']])
#        if x['dataType'] == 'String' and type(rows[i][x['name']]) != str:
#            rows[i][x['name']] = str(rows[i][x['name']])

# for i in range(0,len(rows)):
#     for x in full_list_of_columns:
#         if 'date' in x or 'time' in x and rows[i][x] is None and type(rows[i][x])!=int:
#             rows[i][x] = ''
#          elif 'date' in x or 'time':
#             rows[i][x] = str(rows[i][x]).replace(' ','')
            # rows[i][x] =



row_final={'rows':rows}
with open('rows','w') as row:
    json.dump(row_final,row)

json_column_structure_edit = json.dumps(list_of_refined_columns,indent=4,sort_keys=False)
print(json_column_structure_edit)
# to_write_string = json.dumps(json_column_structure)
with open('Column','w') as file:
    file.write(json_column_structure_edit)

with open('Column','r') as file:
    columns = file.read( )

json_column = json.loads(columns)
json_table_1 = {'name':'deals', 'columns':json_column}
json_tables = [json_table_1]
json_data_set = {'name':'Skylark_Pipe_Drive_1', 'tables':json_tables}
json_string_dataset = json.dumps(json_data_set)

with open('DataSet','w') as file:
    json.dump(json_data_set,file)



# table1 = {'name' : 'Deals', 'columns':columns}
# tables = [table1]
#
# dataset = {'name' : 'Test deals', 'tables':tables }

