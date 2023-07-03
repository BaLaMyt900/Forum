from django.apps import AppConfig


class AnnounceConfig(AppConfig):
    name = 'announcement'

    def ready(self):
        import announcement.signals
