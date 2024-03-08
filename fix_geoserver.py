import os
import time
from dotenv import load_dotenv
from geo.Geoserver import Geoserver

load_dotenv()

host=os.getenv('GEOSERVER_HOST')
user=os.getenv('GEOSERVER_USER')
passwd=os.getenv('GEOSERVER_PASSWORD')

geo = Geoserver(host, username=user, password=passwd)

# set workspace and datastores to delete
ws='ActionTracker'
datastores_to_delete=['MongoDB_AT','AT_Postgres']

for ds in datastores_to_delete:
    print(f'Borrando datastore: {ds} from workspace: {ws}  ')
    # delete feature store
    geo.delete_featurestore(featurestore_name=ds, workspace=ws)
    time.sleep(20)
print('END')