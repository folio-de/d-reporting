from ldlite import LDLite

# Configure LDLite using the connection parameters
ld = LDLite()
ld._verbose = True
ld.connect_folio(base_url, tenant, user, password)
_ = ld.connect_db("") # provide a filename to to persist data accross kernel restarts -> eg. `ld.connect_db(ldlite.duckdb)`

_ = ld.query(
    table="dbs_users", # table specifies the name the data get in the database
    path="users", # path specifies the api endpoint to pull the data from
)

_ = ld.query(
    table="patrongroups", # table specifies the name the data get in the database
    path="/groups", # path specifies the api endpoint to pull the data from
    #limit=5000 # limit specifies the maximum number of records to pull from the endpoint
)

value=ld.db.cursor().execute('''SELECT  COUNT(DISTINCT barcode)
                                FROM dbs_users__t 
                                LEFT JOIN patrongroups__t ON dbs_users__t.patron_group = patrongroups__t.id
                                WHERE patrongroups__t.group NOT IN ('Technik')''').pl()
print("5.1", value, sep=":  ")
