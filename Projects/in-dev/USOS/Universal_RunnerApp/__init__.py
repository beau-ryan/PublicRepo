from .Universal_Runner import UniversalRunnerApp
from .run_main_app import main_menu


__all__ = ["UniversalRunnerApp", "app_core_instance", "shutdown_event", "initialize_app", "main_menu"]
app_core_instance = None
shutdown_event = None
def initialize_app():
    global app_core_instance, shutdown_event
    app_core_instance, shutdown_event = UniversalRunnerApp.initialize_app()
    return app_core_instance, shutdown_event
main_menu = main_menu