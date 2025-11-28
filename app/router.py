"""
Centralized router configuration.
All application routers are registered here and imported into main.py.
"""

from fastapi import FastAPI

from app.crawling.adapter.input.web.crawling_router import crawling_router
from app.data.adapter.input.web.data_router import data_router
from app.data.infrastructure.orm.data_orm import DataORM  # noqa: F401
from app.keywords.adapter.input.web.keyword_router import keyword_router
from app.keywords.infrastructure.orm.keyword_orm import KeywordORM  # noqa: F401
from app.post_analysis.adapter.input.web.document_analysis_router import (
    post_analysis_router,
)


def setup_routers(app: FastAPI) -> None:
    app.include_router(post_analysis_router, prefix="/post-analysis")
    app.include_router(data_router, prefix="/data")
    app.include_router(crawling_router, prefix="/crawling")
    app.include_router(keyword_router, prefix="/keywords")