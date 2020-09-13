from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select, DateTime
from helpers import get_engine

def main():
    metadata = MetaData()
    engine = get_engine()

    videos = Table('videos', metadata, autoload=True, autoload_with=engine)
    channels = Table('channels', metadata, autoload=True, autoload_with=engine)

    ins = videos.insert().values(
        channel_id=0,
        view_count=1019478943,
        upload_date="2012-11-08 01:37:45",
        title="Lose Yourself - Music Video"
    )

    ins2 = videos.insert().values(
        channel_id=0,
        view_count=2019478943,
        upload_date="2013-11-08 01:37:45",
        title="Slim Shady - Music Video"
    )

    ins3 = channels.insert().values(
        id=0,
        channel_url='#',
        name='EminemVEVO',
        subscriber_count=11871298
    )

    conn = engine.connect()
    conn.execute(ins3)
    conn.execute(ins)
    conn.execute(ins2)

    conn.close()

if __name__ == '__main__':
    main()