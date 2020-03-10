import pymongo

import time
from jianwei.pipelines import MongoPipeline

monitor = MongoPipeline('mongodb://localhost:27017', 'jianwei')
monitor_db = monitor.db
newest_name = max(monitor_db.list_collection_names())
mongo_clt = monitor.db[newest_name]
start_time = time.time()
while True:
    used_time = time.time() - start_time

    print('Time: %6.2f min, Documents stacked: %6d in collection %s'
          % (used_time/60, mongo_clt.count_documents({}), mongo_clt.name))
    time.sleep(5)

    '''After Main Procedure starts, then start it, for waiting reading the MongoDB'''

