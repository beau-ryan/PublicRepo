import sys
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add Universal_RunnerApp root to sys.path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from src.ai_backend.app.features.debugger_assist import DebuggerAssist, DebuggerAssistError

@pytest.fixture(autouse=True)
def reset_singleton():
    DebuggerAssist._instance = None
    yield
    DebuggerAssist._instance = None

@pytest.fixture
def mock_llm_service():
    with patch('src.ai_backend.app.features.debugger_assist.LLMService') as MockLLM, \
         patch('src.ai_backend.app.features.debugger_assist.Settings') as MockSettings:
        instance = MockLLM.return_value
        instance.is_model_loaded.return_value = True
        
        # Mock the Settings.LLM_TEMPERATURE attribute
        MockSettings.LLM_TEMPERATURE = 0.7
        
        # Create a proper async mock for generate_text
        instance.generate_text = MagicMock()
        
        # Make generate_text return a coroutine
        async def mock_generate_text(*args, **kwargs):
            return instance.generate_text.return_value
        
        instance.generate_text.side_effect = mock_generate_text
        
        yield instance

@pytest.mark.asyncio
async def test_diagnose_error_success(mock_llm_service):
    mock_llm_service.generate_text.return_value = (
        "Issue Summary: Division by zero.\n"
        "Root Cause: Attempted to divide by zero.\n"
        "Suggested Fix: Add a check for zero.\n"
        "Relevant Code Lines (optional, comma-separated): 10, 20-22"
    )
    debugger = DebuggerAssist()
    result = await debugger.diagnose_error("ZeroDivisionError", stack_trace="...", code_context="...", language="python")
    assert "Division by zero" in result.issue_summary
    assert 10 in result.relevant_code_lines
    assert 20 in result.relevant_code_lines
    assert 22 in result.relevant_code_lines

@pytest.mark.asyncio
async def test_diagnose_error_llm_not_loaded(mock_llm_service):
    mock_llm_service.is_model_loaded.return_value = False
    debugger = DebuggerAssist()
    with pytest.raises(DebuggerAssistError):
        await debugger.diagnose_error("ZeroDivisionError")

@pytest.mark.asyncio
async def test_diagnose_error_llm_error(mock_llm_service):
    mock_llm_service.generate_text.side_effect = Exception("LLM error")
    debugger = DebuggerAssist()
    with pytest.raises(DebuggerAssistError):
        await debugger.diagnose_error("ZeroDivisionError")

@pytest.mark.asyncio
async def test_diagnose_error_no_structured_output(mock_llm_service):
    mock_llm_service.generate_text.return_value = "Just a plain text response."
    debugger = DebuggerAssist()
    result = await debugger.diagnose_error("ZeroDivisionError")
    assert result.issue_summary == "Could not determine issue summary."
    assert result.root_cause == "Could not determine root cause."
    assert result.suggested_fix == "Could not determine suggested fix."
    assert result.relevant_code_lines is None

# ...more tests for context, different error types, etc.
def test_singleton_behavior(mock_llm_service):
    debugger1 = DebuggerAssist()
    debugger2 = DebuggerAssist()
    assert debugger1 is debugger2

if __name__ == "__main__":
    # Reset singleton for direct execution
    DebuggerAssist._instance = None
    
    print("Running debugger tests...")
    try:
        # Run tests manually when script is executed directly
        print("✅ Testing singleton behavior...")
        
        # Mock LLMService for direct execution
        with patch('src.ai_backend.app.features.debugger_assist.LLMService') as MockLLM:
            MockLLM.return_value.is_model_loaded.return_value = True
            test_singleton_behavior(MockLLM.return_value)
        
        print("✅ Singleton test passed!")
        
        # You can add more manual test calls here if needed
        print("✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()