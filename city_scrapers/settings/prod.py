from .base import *

USER_AGENT = "City Scrapers [production mode]. Learn more and say hello at https://citybureau.org/city-scrapers"

# Configure item pipelines
ITEM_PIPELINES = {
    "city_scrapers_core.pipelines.DefaultValuesPipeline": 100,
    "city_scrapers_core.pipelines.MeetingPipeline": 200,
    "city_scrapers_core.pipelines.JSCalendarPipeline": 300,
}

# Uncomment one of the StatusExtension classes to write an SVG badge of each scraper's status to
# Azure or S3 after each time it's run.

# By default, this will write to the same bucket or container as the feed export, but this can be
# configured by adding a value in the CITY_SCRAPERS_STATUS_BUCKET or CITY_SCRAPERS_STATUS_CONTAINER
# for S3 and Azure respectively.

EXTENSIONS = {
    # "city_scrapers_core.extensions.AzureBlobStatusExtension": 100,
    # "city_scrapers_core.extensions.S3StatusExtension": 100,
    "scrapy_sentry.extensions.Errors": 10,
    "scrapy.extensions.closespider.CloseSpider": None,
}

FEED_EXPORTERS = {
    "json": "scrapy.exporters.JsonItemExporter",
    "jsonlines": "scrapy.exporters.JsonLinesItemExporter",
}

FEED_FORMAT = "jsonlines"

# Uncomment one of the following to enable a diff middleware class that will deduplicate JSCalendar
# UIDs based on City Scrapers IDs and list any meetings in the future which no longer appear in
# scraped results as cancelled.

SPIDER_MIDDLEWARES = {
    # "city_scrapers_core.middleware.S3DiffMiddleware": 100,
    # "city_scrapers_core.middleware.AzureDiffMiddleware": 100,
}


# Uncomment S3 or Azure to write scraper results to static file storage as newline-delimited JSON
# files made up of JSCalendar events following the meeting schema.

FEED_STORAGES = {
    # "s3": "scrapy.extensions.feedexport.S3FeedStorage",
    # "azure": "city_scrapers_core.extensions.AzureBlobFeedStorage",
}

# Uncomment credentials for whichever provider you're using

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
# AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
# AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")

# Uncomment the FEED_URI for whichever provider you're using

# FEED_URI = "s3://{bucket}/%(year)s/%(month)s/%(day)s/%(hour_min)s/%(name)s.json".format(
#     bucket=CITY_SCRAPERS_STATUS_BUCKET
# )

# FEED_URI = (
#     "azure://{account_name}:{account_key}@{container}"
#     "/%(year)s/%(month)s/%(day)s/%(hour_min)s/%(name)s.json"
# ).format(
#     account_name=AZURE_ACCOUNT_NAME,
#     account_key=AZURE_ACCOUNT_KEY,
#     container=AZURE_CONTAINER,
# )