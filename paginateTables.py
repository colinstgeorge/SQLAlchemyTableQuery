#!/usr/local/bin/python
from sqlalchemy import *
import getpass

password = getpass.getpass()
engine = create_engine("mysql+pymysql://root:" + password + "@localhost", pool_recycle=3600)
#dbToSearch = raw_input("DB To Search: ")
dbToSearch = 'labtech'
i = 0

try:
    connection = engine.connect()
    takeInput = True

    while(True):
        try:
            if( takeInput ):
                tablePrefix = raw_input("Table Prefix: ")
                limiter = raw_input("LIMIT By: ")
            sqlQuery = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '" + dbToSearch + "' AND TABLE_NAME LIKE '%" + tablePrefix  + "%' LIMIT " + str(i) + "," + limiter + ";"
            queryCount = "SELECT count(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '" + dbToSearch + "' AND TABLE_NAME LIKE '%" + tablePrefix  + "%';"

            count = connection.execute(text(queryCount)).first()
            result = connection.execute(text(sqlQuery))
            
            for row in result:
                print row
            i = i + int(limiter)
            if ( i <= count[0] ):
               if( raw_input("More? (y/n):") == 'n' ):
                   takeInput = True
                   continue
               else:
                   takeInput = False
                   pass
            else:
                takeInput = True
        except Exception, e:
            print e
            break
except Exception,e:
    print e
    connection.close()
