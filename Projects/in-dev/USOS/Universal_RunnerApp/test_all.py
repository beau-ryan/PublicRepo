# test module to run tests

from src.tests.test_Universal_Runner import UniversalRunnerApp
from src.tests.test_config import ConfigManager, AuditLogManager, DataLifecycleManager, DatabaseManager, DecoderX, ExecutorDispatcher, Formatter, LLMService, Linter, ModelLoader, PolicyEngine, SecurityBridge, SubprocessGuard, UniversalRunnerInitializationError, NetworkMonitor, ContentService, ContentMetadata, MonitorManager
from src.utils.path_utils import get_project_root




config_manager = ConfigManager()
app = UniversalRunnerApp.instance()
project_root = get_project_root()
audit_log_manager = AuditLogManager()
data_lifecycle_manager = DataLifecycleManager()

if __name__ == "__main__":
    print(f"APP_VERSION: {config_manager.get_setting('APP_VERSION')}")
    print(f"APP_INSTANCE: {app.instance()}")
    print(f"PATH_UTILS: {get_project_root}")