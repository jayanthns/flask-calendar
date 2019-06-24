import logging

from flask import Blueprint, request

from models.article import Article

from common.util.common_response import response

from apps.article.api.serializers import (
    articles_schema,
    article_schema,
    article_create_schema,
    article_update_schema,
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


article_api_blueprint = Blueprint(
    'article_api', __name__
)


@article_api_blueprint.route("/", methods=['GET', 'POST'], strict_slashes=False)
def articles():
    """view for get articles"""
    if request.method == "GET":
        articles = articles_schema.dump(Article.query.all())
        return response(
            message="Data fetched successfully.",
            data=articles.data,
            status=200
        )

    """View for Creating the article."""
    if request.method == 'POST':
        article_data = article_create_schema.load(request.get_json() or {})

        if article_data.errors:
            return response(
                message="Incorrect data were provided.",
                data={**article_data.errors},
                status=401
            )

        article = article_data.data
        article.save()
        article = article_schema.dump(article)
        return response(
            message="Article created successfully.",
            data=article.data,
            status=201
        )


@article_api_blueprint.route(
    "/<int:id>",
    methods=['GET', 'PUT', 'DELETE'],
    strict_slashes=False
)
def article_details(id):
    """Checking the article existence"""
    article = Article.query.get(id)
    if not article:
        return response(
            message="Article not found",
            status=404
        )

    """Detail of the article"""
    if request.method == 'GET':
        article = article_schema.dump(article)
        return response(
            message="Data fetched successfully.",
            data=article.data,
            status=200
        )

    """Updating the  article"""
    if request.method == "PUT":
        article_serializer = article_update_schema.load(
            request.get_json() or {},
            instance=article,
            partial=True
        )
        if article_serializer.errors:
            return response(
                message="Incorrect data were provided.",
                data={**article_serializer.errors},
                status=400
            )

        article = article_serializer.data
        article.save()
        article = article_schema.dump(article)
        return response(
            message=F"Article updated successfully.",
            data=article.data,
            status=200
        )

    if request.method == 'DELETE':
        article.delete()
        return response(
            message="Article deleted successfully.",
            status=200
        )
