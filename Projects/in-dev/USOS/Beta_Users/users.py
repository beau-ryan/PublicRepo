# Beta users module
# User file for beta Version purposes.
# Add user-specific configurations or functions here.
import os
from datetime import datetime
from pathlib import Path
import sys

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) )))
current_script_dir = Path(__file__).resolve().parent
usos_root_dir = current_script_dir.parent 
project_root_with_src = usos_root_dir 

# 4. Insert this path into Python's search list to enable absolute imports.
if str(project_root_with_src) not in sys.path:
    # Using insert(0) prioritizes this path
    sys.path.insert(0, str(project_root_with_src))

from Universal_RunnerApp.src.monitoring.logger import log_to_file
from .feedback import FeedbackRequest

features_enabled = [
    "run_main_app",
    "feedback_service"
]

my_modules = [
    "USOS\n",
    "Universal_RunnerApp",
    "ai_backend",
    "models",
    "services",
    "decoderX",
    "more to come"
]

def get_user_info(user_id=None, username: str = "guest"):
    """Retrieve user information for beta version.

    Args:
        user_id: Optional user ID.
        username: Username of the beta user.
    Returns:
        A dictionary containing user information.
    """
    allowed_users = [ "Admin", "username", "guest" ]
    if username not in allowed_users:
        raise ValueError(f"Username '{username}' is not allowed in beta version.")
    user_info = {
        "user_id": user_id if user_id is not None else "N/A",
        "username": username,
        "access_level": "beta",
        "login_time": datetime.now().isoformat()
    }
    return {
        "user_id": username,
        "username": username,
        "is_admin": username == "Admin",
        "is_user1": username == "User",
        "is_user2": username == "guest",
        "is_user3": username == "username",
        "beta_tester": username == "beta_tester",
        "role": "beta_tester",
        "features_enabled": features_enabled,
        "modules": my_modules
    }

def get_my_modules():
    """Retrieve the list of modules available to beta users.

    Returns:
        A list of module names.
    """
    try:
        package_dir = os.path.join(os.path.dirname(__file__), '..', 'Universal_RunnerApp')
        modules = [f[:-3] for f in os.listdir(package_dir) if f.endswith('.py') and f != '__init__.py']
        return modules
    except Exception as e:
        print(f"Error retrieving modules: {e}")
        return []

def wait_for_user_input(prompt):
    return input(prompt)

def write_feedback(user_id, feedback_text, priority="normal", tags=None, metadata=None):
    user_info = get_user_info(user_id)
    feedback = FeedbackRequest(
        user_id=user_id,
        feedback_text=feedback_text,
        priority=priority,
        tags=tags,
        metadata=metadata
    )
    print(f"Feedback submitted: {feedback}")
    return feedback

def get_feedback_summary(feedback: FeedbackRequest):
    try:
        summary = feedback.summary()
        return summary
    except Exception as e:
        print(f"Error generating feedback summary: {e}")
        return None

def get_featured_modules():
    return [
        "USOS", 
        "Universal_RunnerApp", 
        "ai_backend"
    ]   

def main():
    user_info = get_user_info()
    print(f"User Info: {user_info}")
    user_feedback = input("Your Feedback: ")
    feedback_request = write_feedback(user_id=user_info['username'], feedback_text=user_feedback)
    get_my_modules_list = get_my_modules()
    print(f"My Modules: {get_my_modules_list}")
    features_enabled = user_info.get("features_enabled", [])
    print(f"Enabled Features: {features_enabled}")
    
    # Generate and display feedback summary
    summary = get_feedback_summary(feedback_request)
    if summary:
        print(f"Feedback Summary: {summary}")
    
    print("My Modules:", get_my_modules_list)
    wait_for_user_input("Press Enter at your own Risk...")
    print("Exiting Beta User Module.")


def menu():
    username = input("Enter your username (Admin/User1/User2/User3): ").strip()
    try:
        user_info = get_user_info(username)
    except ValueError as e:
        print(e)
        return

    while True:
        print("\n1. View User Info")
        print("2. Submit Feedback")
        print("3. View My Modules & Featured Modules")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            print(f"User Info: {user_info}")
        elif choice == '2':
            user_feedback = input("Your Feedback: ")
            priority = input("Priority (low/normal/high): ").strip() or "normal"
            tags = input("Tags (comma-separated, optional): ").strip()
            tags_list = [tag.strip() for tag in tags.split(",") if tag.strip()] if tags else []
            write_feedback(
                user_id=username,
                feedback_text=user_feedback,
                priority=priority,
                tags=tags_list
            )
            log_to_file(user_id=username,
                feedback_text=user_feedback,
                priority=priority,
                tags=tags_list
            )
        elif choice == '3':
            features_enabled = user_info.get("features_enabled", [])
            print(f"Enabled Features: {features_enabled}")
            get_my_modules_list = get_my_modules()
            print(f"My Modules: {get_my_modules_list}")
        elif choice == '4':
            print("Exiting...")
            break
        continue_prompt = input("Continue? (y/n): ")
        if continue_prompt.lower() != 'y':
            break

if __name__ == "__main__":
    menu()