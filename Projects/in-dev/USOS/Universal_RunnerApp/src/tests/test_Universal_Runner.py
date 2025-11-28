# test <Version=>0.0.1> Fallback <Verison=>0.0.2>

import sys
import os
import asyncio
import threading
import time
from pathlib import Path
from typing import Callable, Optional, TypeVar, Type, Any, List, Dict, Union
import logging
import traceback
from enum import Enum
import importlib


script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir.parent.parent))

import pydantic

# Import actual classes that exist
from src.monitoring.logger import LoggerManager,log_info, log_event, setup_logging, log_error, log_critical, log_warning, log_debug, log_metric
from src.dependency_injection.container import DependencyContainer, UniversalRunnerError
from src.exceptions._execution_exceptions import ExecutionError
from src.utils.path_utils import ensure_dir_exists, get_project_root

# Import placeholder classes from test_config

from src.tests.test_config import AuditLogManager, ConfigManager, DataLifecycleManager, DatabaseManager, DecoderX, ExecutorDispatcher, Formatter, LLMService, Linter, ModelLoader, PolicyEngine, SecurityBridge, SubprocessGuard, UniversalRunnerInitializationError, NetworkMonitor, ContentService, ContentMetadata, MonitorManager

T = TypeVar('T')

class ComponentName(Enum):
    CONFIG_MANAGER = "config_manager"
    DB_MANAGER = "db_manager"
    AUDIT_LOG_MANAGER = "audit_log_manager"
    SUBPROCESS_GUARD = "subprocess_guard"
    EXECUTOR_DISPATCHER = "executor_dispatcher"
    FORMATTER = "formatter"
    LINTER = "linter"
    MODEL_LOADER = "model_loader"
    LLM_SERVICE = "llm_service"
    SECURITY_BRIDGE = "security_bridge"
    POLICY_ENGINE = "policy_engine"
    DATA_LIFECYCLE_MANAGER = "data_lifecycle_manager"
    DECODER_X = "decoder_x"
    NETWORK_MONITOR = "network_monitor"
    CONTENT_SERVICE = "content_service"
    CONTENT_METADATA = "content_metadata"
    MONITOR_MANAGER = "monitor_manager"

class UniversalRunnerApp:
    """
    Singleton class for the Universal Runner application.

    Responsibilities:
    - Manages the initialization and lifecycle of all core components and services.
    - Ensures thread-safe, one-time initialization of the application.
    - Provides access to core services such as configuration, database, logging, execution, formatting, linting, model loading, security, policy, and monitoring.
    - Registers and manages dependencies using a dependency injection container.
    - Handles application startup, shutdown, and error reporting.

    Usage:
        app = UniversalRunnerApp.instance()
        app.run()
        ...
        app.shutdown()

    Core Components Managed:
        - ConfigManager
        - DatabaseManager
        - AuditLogManager
        - SubprocessGuard
        - ExecutorDispatcher
        - Formatter
        - Linter
        - ModelLoader
        - ContentService
        - ContentMetadata
        - ContentManagement
        - SecurityBridge
        - MonitorManager
        - NetworkMonitor
        - LLMService
        - SecurityBridge
        - PolicyEngine
        - DataLifecycleManager
        - DecoderX
        - MonitorManager

    Methods:
        - instance(): Returns the singleton instance.
        - run(): Starts the application and its monitors.
        - shutdown(): Cleans up resources and performs shutdown logic.
        - get_component(name): Retrieves a registered component by name.

    Raises:
        UniversalRunnerInitializationError: If initialization fails.
        ExecutionError: If an error occurs during application run.
    """
    _instance_shutdown = False
    _instance: Optional["UniversalRunnerApp"] = None
    config_manager: Optional[ConfigManager] = None
    db_manager: Optional[DatabaseManager] = None
    audit_log_manager: Optional[AuditLogManager] = None
    container: DependencyContainer
    _lock = threading.Lock()
    
    def __new__(cls, *args: Any, **kwargs: Any) -> "UniversalRunnerApp":
        """        Create a new instance of UniversalRunnerApp, ensuring singleton behavior.
        If an instance already exists, return it instead of creating a new one.
        Args:
            *args: Positional arguments for initialization.
            **kwargs: Keyword arguments for initialization.
        Returns:            UniversalRunnerApp: The singleton instance of the application.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(UniversalRunnerApp, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def instance(cls) -> 'UniversalRunnerApp':
        return cls()
    
    def _initialize_app(self):
            if getattr(self, "_initialized_flag", False):
                return
            log_info("UniversalRunnerApp: Initializing application...")
            log_event("APP_INIT_START")

            self.container = DependencyContainer()
            self._project_root = get_project_root()
            self.config_manager: Optional[ConfigManager] = None
            # self._logger.debug("UniversalRunnerApp: ConfigManager initialized.")  # <-- REMOVE THIS LINE
            if not self._project_root:
                raise UniversalRunnerInitializationError("Project root could not be determined.")

            try:
                self._setup_logging()
                # Now it's safe to use self._logger
                self._logger.debug("UniversalRunnerApp: Logging initialized.")
                self._initialize_components()
                log_info("UniversalRunnerApp: Initialization complete.")
                log_metric("app_init_duration", time.perf_counter())
                log_event("APP_INIT_SUCCESS")
                self._initialized_flag = True
            except UniversalRunnerInitializationError as e:
                log_critical(f"UniversalRunnerApp: Critical initialization failure: {e}", exc_info=True)
                log_event("APP_INIT_FAILURE", data={"error": str(e), "stage": "component_init"})
                raise
            except Exception as e:
                log_critical(f"UniversalRunnerApp: Unexpected error during initialization: {e}", exc_info=True)
                log_event("APP_INIT_FAILURE", data={"error": str(e), "stage": "unexpected", "traceback": traceback.format_exc()})
                raise UniversalRunnerInitializationError(f"Unexpected error during initialization: {e}") from e
            
    def _setup_logging(self):
        try:
            setup_logging()
            self._logger = LoggerManager().audit_logger
            self._logger.debug("Logging system initialized.")
        except Exception as e:
            raise UniversalRunnerInitializationError(f"Failed to setup: {e}") from e

    def _init_component(
        self,
        name: ComponentName,
        constructor: Callable[..., Any],
        *args: Any,
        **kwargs: Any
    ) -> Any:
        """Helper to initialize, register, and log a component."""
        try:
            component: Any = constructor(*args, **kwargs)
            self.container.register(name.value, component)
            log_info(f"{name.value} initialized and registered.")
            log_event("COMPONENT_INIT_SUCCESS", data={"component": name.value})
            return component
        except Exception as e:
            log_error(f"Failed to initialize {name.value}: {e}", exc_info=True)
            log_event("COMPONENT_INIT_FAILURE", data={"component": name.value, "error": str(e)})
            raise UniversalRunnerInitializationError(f"Failed to initialize {name.value}: {e}") from e

    def _initialize_components(self):
        """Initializes and registers core application components in dependency order."""
        log_info("Initializing core components...")
        log_event("COMPONENTS_INIT_START")

        self.config_manager = self._init_component(ComponentName.CONFIG_MANAGER, ConfigManager)
        self.db_manager = self._init_component(ComponentName.DB_MANAGER, DatabaseManager)
        self.audit_log_manager = self._init_component(ComponentName.AUDIT_LOG_MANAGER, AuditLogManager)
        self._logger.debug("ConfigManager, DatabaseManager, and AuditLogManager initialized.")

        # --- NOT INSTALLED: SubprocessGuard, ExecutorDispatcher, Formatter, Linter ---
    # Use the correct jsons directory inside Universal_RunnerApp/src/jsons
        data_dir = Path(__file__).parent / "src" / "jsons"
        ensure_dir_exists(data_dir)
        self.subprocess_guard = self._init_component(
            ComponentName.SUBPROCESS_GUARD, SubprocessGuard,
            temp_dir_base=data_dir,
            config_manager=self.config_manager,
            audit_log_manager=self.audit_log_manager
        )
        self.executor_dispatcher = self._init_component(
            ComponentName.EXECUTOR_DISPATCHER, ExecutorDispatcher,
            config_manager=self.config_manager,
            subprocess_guard=self.subprocess_guard
        )
        self.formatter = self._init_component(
            ComponentName.FORMATTER, Formatter,
            config_manager=self.config_manager,
            audit_log_manager=self.audit_log_manager,
            subprocess_guard=self.subprocess_guard
        )
        self.linter = self._init_component(
            ComponentName.LINTER,
            Linter
        )
        self._logger.debug("SubprocessGuard, ExecutorDispatcher, Formatter, and Linter initialized.")

        # --- ModelLoader ---
        model_dir = get_project_root() / "src" / "models"
        ensure_dir_exists(model_dir)
        self._logger.debug("Ensuring model directory exists at: %s", model_dir)
        self.model_loader = self._init_component(
            ComponentName.MODEL_LOADER, ModelLoader,
            config_manager=self.config_manager  # Use only the parameter that exists in test_config.py
        )

        #--- NOT INSTALLED: NetworkMonitor, LLMService, SecurityBridge, PolicyEngine, DataLifecycleManager, DecoderX ---
        self._network_monitor = self._init_component(
            ComponentName.NETWORK_MONITOR, NetworkMonitor,
            interval=10
        )
        self._logger.debug("NetworkMonitor initialized.")
        self.llm_service = self._init_component(
            ComponentName.LLM_SERVICE, LLMService,
            config_manager=self.config_manager,
            model_loader=self.model_loader,
            executor_dispatcher=self.executor_dispatcher
        )
        self.security_bridge = self._init_component(
            ComponentName.SECURITY_BRIDGE,
            SecurityBridge,
            project_root=self._project_root,
            config_manager=self.config_manager
        )
        self.policy_engine = self._init_component(
            ComponentName.POLICY_ENGINE, PolicyEngine
        )
        self.data_lifecycle_manager = self._init_component(
            ComponentName.DATA_LIFECYCLE_MANAGER, DataLifecycleManager
        )
        self.decoder_x = self._init_component(
            ComponentName.DECODER_X, DecoderX
        )

        # --- NOT INSTALLED: ContentService, ContentMetadata, MonitorManager registration for extra monitors ---
        self._content_service = self._init_component(
            ComponentName.CONTENT_SERVICE, ContentService,
            config_manager=self.config_manager,
            db_manager=self.db_manager,
            audit_log_manager=self.audit_log_manager
        )
        self._network_monitor = self._init_component(
            ComponentName.NETWORK_MONITOR, NetworkMonitor,
            config_manager=self.config_manager
        )
        self._logger.debug("ContentService initialized.")
        if not pydantic.BaseModel.__subclasscheck__(ContentMetadata):
            log_info("Registering ContentMetadata model in Pydantic...")
            pydantic.BaseModel.__subclasscheck__(ContentMetadata)
            self.container.register(
                ComponentName.CONTENT_SERVICE.value,
                self._content_service
            )
            self.container.register(
                ComponentName.CONTENT_METADATA.value,
                ContentMetadata
            )
            log_info("ContentMetadata model registered successfully.")

        # --- MonitorManager ---
        self.monitor_manager = MonitorManager()
        # Optionally start monitors here or in run()
        self.monitor_manager.register_monitor(NetworkMonitor(interval=10))  # Replace 10 with your desired interval in seconds
        self.monitor_manager.register_monitor(self._network_monitor)
        self.monitor_manager.register_monitor(self.security_bridge)
        self.monitor_manager.register_monitor(self.policy_engine)
        self.monitor_manager.register_monitor(self.data_lifecycle_manager)
        self.monitor_manager.register_monitor(self.decoder_x)
        self._logger.debug("NetworkMonitor, ModelLoader, LLMService, SecurityBridge, PolicyEngine, DataLifecycleManager, DecoderX initialized.")

        # --- Register only installed components ---
        self.container.register(ComponentName.CONFIG_MANAGER.value, self.config_manager)
        self.container.register(ComponentName.DB_MANAGER.value, self.db_manager)
        self.container.register(ComponentName.AUDIT_LOG_MANAGER.value, self.audit_log_manager)
        self.container.register(ComponentName.MODEL_LOADER.value, self.model_loader)
        self.container.register(ComponentName.SUBPROCESS_GUARD.value, self.subprocess_guard)
        self.container.register(ComponentName.EXECUTOR_DISPATCHER.value, self.executor_dispatcher)
        self.container.register(ComponentName.FORMATTER.value, self.formatter)
        self.container.register(ComponentName.LINTER.value, self.linter)
        self.container.register(ComponentName.NETWORK_MONITOR.value, self._network_monitor)
        self.container.register(ComponentName.LLM_SERVICE.value, self.llm_service)
        self.container.register(ComponentName.SECURITY_BRIDGE.value, self.security_bridge)
        self.container.register(ComponentName.POLICY_ENGINE.value, self.policy_engine)
        self.container.register(ComponentName.CONTENT_SERVICE.value, self._content_service)
        self.container.register(ComponentName.MONITOR_MANAGER.value, self.monitor_manager)
        self.container.register(ComponentName.DATA_LIFECYCLE_MANAGER.value, self.data_lifecycle_manager)
        self.container.register(ComponentName.DECODER_X.value, self.decoder_x)
        self.container.register("project_root", self._project_root)
        self.container.register("logger", self._logger)
        log_info("UniversalRunnerApp: All components initialized and registered.")
        print("UniversalRunnerApp initialized and running.")

    def get_component(self, name: ComponentName, expected_type: type) -> Any:
        """
        Retrieves a registered component by name and checks its type.
        Args:
            name (ComponentName): The enum value of the component to retrieve.
            expected_type (type): The expected type of the component.
        Returns:
            Any: The component instance if found and type matches, otherwise raises UniversalRunnerError.
        Raises:
            UniversalRunnerError: If the component is not found or type does not match.
        """
        if not self._initialized_flag:
            raise UniversalRunnerError("Application not initialized. Call instance() first.")
        return self.container.get(name.value, expected_type)
    
    def run(self) -> None:
        """
        Starts the application and its monitors.
        This method initializes all components and starts the monitoring services.
        """
        log_info("UniversalRunnerApp: Starting application...")
        log_event("APP_RUN_START")
        try:
            # if self.monitor_manager is not None:
            #     self.monitor_manager.start_all_monitors()
            log_info("UniversalRunnerApp: All monitors started successfully.") 
            log_info("UniversalRunnerApp: Application started successfully.")
            log_event("APP_RUN_SUCCESS")
        except Exception as e:
            log_error(f"UniversalRunnerApp: Error during application run: {e}", exc_info=True)
            log_event("APP_RUN_FAILURE", data={"error": str(e)})
            raise ExecutionError(f"Error during application run: {e}") from e
        finally:
            self._instance_shutdown = True
            self._logger.debug("UniversalRunnerApp: Application run completed.")
            log_info("UniversalRunnerApp: Informational log reached.")
            log_event("APP_RUN_COMPLETE")
            log_debug("UniversalRunnerApp: Application run method finished execution.")

    def shutdown(self) -> None:
        """Clean up resources and perform shutdown logic."""
        def _can_log():
            import sys
            return getattr(sys, 'meta_path', None) is not None

        if self._instance_shutdown:
            if _can_log():
                log_warning("UniversalRunnerApp: Shutdown called, but instance is already shutdown.")
            return

        if _can_log():
            log_info("UniversalRunnerApp: Shutting down application...")
            log_event("APP_SHUTDOWN_START")
        try:
            if hasattr(self, "monitor_manager") and self.monitor_manager:
                self.monitor_manager.stop_all_monitors()
                if _can_log():
                    log_info("UniversalRunnerApp: All monitors stopped successfully.")
            # Only shut down components that are registered
            for name in ComponentName:
                if self.container.has(name.value):
                    component: Any = self.container.resolve(name.value)
                    if component and hasattr(component, 'shutdown'):
                        if _can_log():
                            log_info(f"UniversalRunnerApp: Shutting down component {name.value}...")
                        component.shutdown()
                        if _can_log():
                            log_info(f"UniversalRunnerApp: Component {name.value} shutdown successfully.")
            if _can_log():
                log_info("UniversalRunnerApp: All components shut down successfully.")
                log_event("APP_SHUTDOWN_SUCCESS")
        except Exception as e:
            if _can_log():
                log_error(f"UniversalRunnerApp: Error during shutdown: {e}", exc_info=True)
                log_event("APP_SHUTDOWN_FAILURE", data={"error": str(e)})
            raise UniversalRunnerError(f"Error during shutdown: {e}") from e
        finally:
            self._instance_shutdown = True
            if _can_log():
                log_info("UniversalRunnerApp: Shutdown complete.")
                log_event("APP_SHUTDOWN_COMPLETE")
                if hasattr(self, "_logger"):
                    self._logger.debug("UniversalRunnerApp: Shutdown method finished execution.")
            UniversalRunnerApp._initialized_flag = False
    def __del__(self):
        """Destructor to ensure proper cleanup."""
        if not self._instance_shutdown:
            try:
                self.shutdown()
            except Exception:
                pass  # Avoid logging during interpreter shutdown
        else:
            if hasattr(self, "_logger"):
                self._logger.debug("UniversalRunnerApp: __del__ method executed.")
        UniversalRunnerApp._instance = None
        

if __name__ == "__main__":
    app = UniversalRunnerApp.instance()
    app._initialize_app()
    app.run()

# Logger test
log_info("Logger test: This should appear in I:/USOS/Universal_RunnerApp/data/logs/app.log")
log_error("Logger test: This should appear in I:/USOS/Universal_RunnerApp/data/logs/app_error.log")

# Example model training (using placeholder)
csv_path = "I:/USOS/data/your_data.csv"  # Your real data file
target_column = "target"  # Your target column name
model_path = "I:/USOS/Universal_RunnerApp/models/local_model.bin"

decoder = DecoderX()
decoder.train_and_save_real_model(csv_path, target_column, model_path)
    
# Example usage
async def main():
    try:
        app = UniversalRunnerApp.instance()
        app.run()
        
        # Example of using a component
        llm_service = app.get_component(ComponentName.LLM_SERVICE)
        response = await llm_service.generate_text("Explain the concept of dependency injection.")
        print(f"\n--- Application Usage Example ---\nResponse from LLM Service: {response}\n")
        
        formatter = app.get_component(ComponentName.FORMATTER)
        formatted_code = await formatter.format_code("def my_func():\n    pass", "python")
        print(f"Formatted code:\n{formatted_code}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'app' in locals():
            app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
   
