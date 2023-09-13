import os

from dz_alchemy.database import DATABASE_NAME, Session
import create_data as db_creator

from dz_alchemy.client import Client
from dz_alchemy.firm import Firm

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
