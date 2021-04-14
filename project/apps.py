from django.apps import AppConfig


class MtaaConfig(AppConfig):
    name = 'project'

    def ready(self):
        import project.signals