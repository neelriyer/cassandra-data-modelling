from create_tables import main as create_tables_main
from etl import main as etl_main
from process_events import main as process_events_main

if __name__ == '__main__':
    process_events_main()
    create_tables_main()
    etl_main()