import sys
import os
from typing import Any

# Add Universal_RunnerApp root to sys.path
project_root: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

print("Current sys.path:")
for p in sys.path:
    print(" ", p)

# Test imports
try:
    print("Testing utils imports...")
    from src.utils import path_utils, diagnostics_utils, filesystem_utils, logging_utils, network_utils, secure_utils, voice_utils
    print("✅ Utils imported successfully!")
    
    print("Testing network imports...")
    from src.network import phone_client, phone_server, network_chain_runner, security, websocket_server, proxy_chain
    print("✅ Network imported successfully!")
    
    print("Testing monitoring imports...")
    from src.monitoring import audit_log_manager, error_handler, event, handlers, logger, performance_metrics, tools
    from src.monitoring import threat_intelligence  # Import separately to isolate the issue
    print("✅ Monitoring imported successfully!")
    
    print("Testing config imports...")
    from src.config import *
    print("✅ Config imported successfully!")
    
    print("Testing exceptions imports...")
    from src.exceptions import LLMServiceError, NetworkError, ConfigurationError
    print("✅ Exceptions imported successfully!")

    print("✅ All src submodules imported successfully!")

except ModuleNotFoundError as e:
    print(f"❌ Failed to import: {e}")
    
    # Let's test individual imports to find the specific issue
    print("\nTesting individual monitoring imports:")
    monitoring_modules = [
        "audit_log_manager", "error_handler", "event", "handlers", 
        "logger", "performance_metrics", "threat_intelligence", "tools"
    ]
    
    for module in monitoring_modules:
        try:
            exec(f"from src.monitoring import {module}")
            print(f"✅ {module} imported successfully")
        except ImportError as import_error:
            print(f"❌ {module} failed: {import_error}")
        except Exception as other_error:
            print(f"⚠️ {module} error: {other_error}")
    
    # Also try direct import
    print("\nTrying direct import:")
    try:
        import src.monitoring.threat_intelligence
        print("✅ Direct import of threat_intelligence worked")
    except Exception as e:
        print(f"❌ Direct import failed: {e}")

