from marshmallow import ValidationError, validate

from extensions import ma

from models.article import Article


def validate_required_string(field_value):
    if not len(field_value):
        raise ValidationError("This field value is required")


class ArticleSchema(ma.ModelSchema):
    # created_on = ma.Function(lambda obj: obj.created_on.strftime("%d-%m-%y"))
    # modified_on = ma.Function(lambda obj: obj.modified_on.strftime("%d-%m-%y"))

    class Meta:
        model = Article


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


class ArticleCreateSchema(ma.ModelSchema):

    class Meta:
        model = Article
        fields = ('name', 'author', 'description')


article_create_schema = ArticleCreateSchema()


class ArticleUpdateSchema(ma.ModelSchema):
    class Meta:
        model = Article
        fields = ('name', 'author', 'description')


article_update_schema = ArticleUpdateSchema()
