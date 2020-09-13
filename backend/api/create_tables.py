from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select, DateTime
from sqlalchemy import create_engine
from helpers import get_engine

def main():

    metadata = MetaData()

    videos = Table('videos', metadata,
        Column('id', Integer, primary_key=True),
        Column('channel_id', ForeignKey('channels.id')),
        Column('view_count', Integer),
        Column('upload_date', DateTime),
        Column('title', String),
        Column('description', String),
        Column('manifest_url', String),
        Column('thumbnail_url', String)
    )

    channels = Table('channels', metadata,
        Column('id', Integer, primary_key=True),
        Column('channel_url', String),
        Column('channel_icon_url', String),
        Column('name', String),
        Column('subscriber_count', Integer)
    )

    engine = get_engine()

    metadata.drop_all(engine)
    metadata.create_all(engine)

if __name__ == '__main__':
    main()