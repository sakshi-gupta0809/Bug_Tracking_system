
import os

def create_file(filepath, content=""):
    with open(filepath, 'w') as f:
        f.write(content)

def setup_bug_tracking_system(base_path='BugTrackingSystem'):
    # Define folders
    folders = [
        'data',
        'src',
        'docs',
        'tests'
    ]

    # Define files with optional initial content
    files = {
        'data/bugs.json': '[]',  # Start with empty JSON list

        'src/__init__.py': '',
        'src/main.py': '# Entry point for the Bug Tracking System\n\nfrom menu import menu\n\nif __name__ == "__main__":\n    menu()',
        'src/menu.py': '# Menu logic will go here\n',
        'src/bug_operations.py': '# Bug operations functions (add, update, delete, view) will go here\n',
        'src/data_handler.py': '# Functions to load and save data will go here\n',

        'docs/README.md': '# Bug Tracking System\n\nA simple bug tracking CLI application using Python and JSON storage.',
        'tests/test_bug_operations.py': '# Unit tests for bug operations will go here\n',

        'requirements.txt': '# List your required packages here, e.g. Flask if needed\n',
        '.gitignore': '__pycache__/\n*.pyc\n.env\n',
        'LICENSE': 'MIT License\n\nYour license text here.'
    }

    # Create base directory
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Create folders
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)

    # Create files
    for filepath, content in files.items():
        full_path = os.path.join(base_path, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        create_file(full_path, content)

    print(f"✅ Bug Tracking System project structure created successfully at '{base_path}/'")

# Run the setup function
if __name__ == "__main__":
    setup_bug_tracking_system()
