import settings
import pymysql

conn = pymysql.connect(host=settings.DB_HOST,
                       user=settings.DB_USER,
                       password=settings.DB_PASSWORD,
                       db=settings.DB_NAME,
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

