import create_tables
import example_populate
import redis
import boto3

if __name__ == '__main__':
    create_tables.main()
    example_populate.main()

    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('video_id_counter', 0)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('youtube-clone-dev-storage')
    bucket.objects.filter(Prefix="video/").delete()