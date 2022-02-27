import json

import requests

from main.api.schemas.common import Response
from main.utils import add_query_params

SCRAPY_URL = "http://0.0.0.0:7800/crawl.json"


class AmazonLocationService:
    """
    Service to extract data from ScrapyRT service.
    """

    @staticmethod
    def get_cookies(zip_code: str, country_code: str) -> Response:
        query_params = {
            "start_requests": "1",
            "spider_name": "amazon:location-session",
            "crawl_args": json.dumps(
                {"zip_code": zip_code, "country": country_code.lower()}
            ),
        }
        url = add_query_params(url=SCRAPY_URL, params=query_params)
        json_data = requests.get(url=url).json()
        cookies = json_data["items"]
        return Response(
            success=True,
            data={
                "zip_code": zip_code,
                "country_code": country_code,
                "cookies": cookies[0],
            },
        )