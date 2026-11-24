# Einrichtung OkapiAPIClient : https://gitlab.bib-bvb.de/folio-public/okapiclient/-/tree/0ba3be8ed9a0dd783b8ddb787a66ccc2c056b39f/ 

from OkapiAPIClient.ApiClient import ApiClient
# Okapi-Authentifizierung
helper = ApiClient(
    url = URL
    username = USER
    password = PASSWORD
    tenant = TENANT
    verbose = True
)

number_5_1 = helper.makeAPICall(
    path = f'/users?limit=0'
).json()

number_5_1["totalRecords"]
