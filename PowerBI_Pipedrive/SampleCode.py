
sample_parameters ={
   "resource": "https://analysis.windows.net/powerbi/api",
   "tenant" : "",
   "authorityHostUrl" : "https://login.windows.net/common/oauth2/authorize",
   "clientId" : "04ebd110-445f-4c1d-89c3-0f91bdf074f8",
   "clientSecret" : "ckrsUnF1KejRq8tzZxPYa/brUNqRdN/vY0OzXnrGeWA="
                    }

authority_url = (sample_parameters['authorityHostUrl'] + '/' +
                 sample_parameters['tenant'])
RESOURCE =sample_parameters['resource']



#uncomment for verbose log
#turn_on_logging()

context = adal.AuthenticationContext(
    authority_url, validate_authority=sample_parameters['tenant'] != 'adfs',
    api_version=None)

token = context.acquire_token_with_client_credentials(
    RESOURCE,
    sample_parameters['clientId'],
    sample_parameters['clientSecret'])

print('Here is the token:')
print(json.dumps(token, indent=2))


