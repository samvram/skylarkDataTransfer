import json
import adal
import requests
import requests_oauthlib
import oauthlib

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

clientID = '966aaaec-51fa-49c0-8e85-59a4cfd50091'
resource = 'https://analysis.windows.net/powerbi/api'
redirect = 'https://login.live.com/oauth20_desktop.srf'
auth_url = 'https://login.microsoftonline.com/common/oauth2/authorize'
scopes = []

from oauthlib.oauth2 import MobileApplicationClient
from requests_oauthlib import OAuth2Session

oauth = OAuth2Session(client=MobileApplicationClient(client_id=clientID), scope=scopes)
authorization_url, state = oauth.authorization_url(auth_url)

response = oauth.get(authorization_url)
# print(response.url)
oauth.parse_request_uri_response(response.uri)

# authorization_url = 'https://login.microsoftonline.com/common/oauth2/authorize?'+'client_id='+clientID+'&response_type=code'+'&redirect_uri='+'&resource='+resource

# authority = requests.get(authorization_url)
# print(authority)
# print(json.dumps(authority,indent=2))



#File Operations
# with open('Column','r') as file:
#     columns = file.read( )
#
# json_column = json.loads(columns)
# json_table_1 = {'name':'deals', 'columns':json_column}
# json_tables = [json_table_1]
# json_data_set = {'name':'Sample DataSet', 'tables':json_tables}
# json_string_dataset = json.dumps(json_data_set)
#
#
# with open('rows','r') as fp:
#     row = fp.read( )
# json_rows_string = {'rows':row}
#
# final_url = 'https://api.powerbi.com/v1.0/myorg/datasets'
# response = requests.post(final_url, data=json_string_dataset)
#
# read_response = json.loads(response.text)
# dataset_id = read_response['id']
#
# table_name = 'deals'
# requests.post('https://api.powerbi.com/v1.0/myorg/datasets/'+dataset_id+'/tables/'+table_name+'/rows',json_rows_string)