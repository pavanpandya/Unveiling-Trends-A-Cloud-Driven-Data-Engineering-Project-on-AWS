# To copy all JSON Reference data to same location:
aws s3 cp . s3://de-youtube-raw-us-east-2/youtube/raw_data/ --recursive --exclude "*" --include "*.json"


# To copy all data files to its own location, following Hive-style patterns:
aws s3 cp CAvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=ca/
aws s3 cp DEvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=de/
aws s3 cp FRvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=fr/
aws s3 cp GBvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=gb/
aws s3 cp INvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=in/
aws s3 cp JPvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=jp/
aws s3 cp KRvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=kr/
aws s3 cp MXvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=mx/
aws s3 cp RUvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=ru/
aws s3 cp USvideos.csv s3://de-youtube-raw-us-east-2/youtube/raw_data/region=us/