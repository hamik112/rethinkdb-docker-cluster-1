import rethinkdb as r

try:
    print("rethinkdb initialising")

    construct = [
        {'DB':'awesome', 'TABLE':'things', 'INDEXES':['stuff']}
    ]
    for struct in construct:
        DB      = struct['DB']
        TABLE   = struct['TABLE']
        INDEXES = struct['INDEXES']

        conn  = r.connect(host='127.0.0.1', port=28015, db=DB)

        # Create databses
        db_exists = r.db_list().contains(DB).run(conn)
        if not db_exists:
            r.db_create(DB).run(conn)

        # Create tables
        table_exists = r.db(DB) \
                        .table_list() \
                        .contains(TABLE) \
                        .run(conn)

        if not table_exists:
            result = r.db(DB) \
                      .table_create(TABLE) \
                      .run(conn)

        # Create indexes
        rtable = r.db(DB).table(TABLE)
        print('creating shards')
        rtable.reconfigure(shards=2, replicas=1).run(conn)

        current_indexes = rtable.index_list().run(conn)
        for index in INDEXES:
            if index not in current_indexes:
                print('adding index {0}'.format(index))
                rtable.index_create(index).run(conn)

    print("rethinkdb ready")

except Exception as e:
    print(e)
    print("rethinkdb failed to initialise")
    exit(1)
