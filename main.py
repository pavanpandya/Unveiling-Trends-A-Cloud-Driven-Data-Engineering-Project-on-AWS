# If you want to store the data in the local machine.
# import scrapper

# if __name__ == "__main__":
#     # Call the scrap function from scrapper.py
#     scrapper.scrap()


# If you want to store the data in the AWS S3 bucket.
import scrapper

if __name__ == "__main__":  
    # Call the scrap function from scrapper.py
    country_data = scrapper.scrap()
    # print(country_data)
    # Upload data to S3
    bucket_name = "de-youtube-raw-us-east-2"
    for country_code, data in country_data.items():
        scrapper.write_to_s3(country_code, data, bucket_name)
