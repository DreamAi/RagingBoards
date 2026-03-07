import time

from marketing.content_generator import generate_post
from marketing.fact_checker import validate
from marketing.quality_validator import check_quality
from marketing.seo_engine import add_seo
from marketing.social_publisher import publish

def run_campaign():

    post = generate_post()

    if not validate(post):

        print("Post rejected: fact check failed")
        return

    if not check_quality(post):

        print("Post rejected: quality check failed")
        return

    post = add_seo(post)

    publish(post)

while True:

    run_campaign()

    time.sleep(7200)
