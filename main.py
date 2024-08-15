from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

from data_loader import (
    get_opportunity_data,
)


app = FastAPI()


class Opportunity(BaseModel):
    country: Optional[str] = None
    browser: Optional[str] = None
    platform: Optional[str] = None
    vertical: Optional[str] = None


@app.get("/opportunities")
def get_opportunities(
    country: str = None, browser: str = None, platform: str = None, vertical: str = None
):
    return {
        "query": {
            "country": country,
            "browser": browser,
            "platform": platform,
            "vertical": vertical,
        },
        "opportunities": get_opportunity_data(
            country,
            browser,
            platform,
            vertical,
        ),
    }
