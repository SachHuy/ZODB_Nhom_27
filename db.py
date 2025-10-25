from ZODB import DB, FileStorage
import transaction

DB_FILE = "contacts.fs"

# Kết nối database
storage = FileStorage.FileStorage(DB_FILE)
db = DB(storage)
connection = db.open()
root = connection.root()

# Khởi tạo dict lưu contacts nếu chưa có
if 'contacts' not in root:
    root['contacts'] = {}
    transaction.commit()

contacts = root['contacts']

def commit():
    transaction.commit()

def close():
    connection.close()
    db.close()
