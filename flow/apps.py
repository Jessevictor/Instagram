from django.apps import AppConfig


class FlowConfig(AppConfig):
    name = 'flow'

def ready(self):
    import flow.signals