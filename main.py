from moviePlatform.wsgi import application
app = application
from sqlalchemy import create_engine

def hello():
    engine_tcp = create_engine('mysql+pymysql://root:123@127.0.0.1:3305')
    existing_databases_tcp = engine_tcp.execute("SHOW DATABASES;")
    con_tcp ="Connecting from APP Engine Standard to Cloud SQL using TCP: databases =>" + str([d[0] for d in existing_databases_tcp]).strip('[]') +"\
"
    engine_unix_socket = create_engine('mysql+pymysql://root:123@/movies?unix_socket=/cloudsql/ca675-2-298418:europe-west2:movies')
    existing_databases_unix_socket = engine_unix_socket.execute("SHOW DATABASES;")
    con_unix_socket ="Connecting from APP Engine Standard to Cloud SQL using Unix Sockets: tables in sys database:  =>" + str([d[0] for d in existing_databases_unix_socket]).strip('[]') +"\
"
    return con_tcp + con_unix_socket