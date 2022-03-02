from csql_queries import create_table_queries, music_app_keyspace_create
from cassandra.cluster import Cluster


def create_tables(session):
    for query in create_table_queries:
        session.execute(query)
        # try:
        #     session.execute(query)
        # except Exception as e:
        #     print(e)


def create_keyspace(session):
    session.execute(music_app_keyspace_create)
    # try:
    #     session.execute(music_app_keyspace_create)
    # except Exception as e:
    #     print(e)


def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    create_keyspace(session)
    session.set_keyspace('music_app')

    create_tables(session)

    print('Tables created.')


if __name__ == '__main__':
    main()
