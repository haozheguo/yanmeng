from django.apps import AppConfig


class ScrapyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "scrapy"
    verbose_name = "爬虫文章管理"
