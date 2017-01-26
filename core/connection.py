import settings
import pymysql

conn = pymysql.connect(host=settings.host,
                       user=settings.user,
                       password=settings.password,
                       db=settings.db,
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
