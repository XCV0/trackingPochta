from pack_mgr import get_status
from db_control import db



all_parcels = db.get_all_parcels()
print(all_parcels)
