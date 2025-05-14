import os
import subprocess

from watchdog.events import FileSystemEventHandler

class PluginHandler(FileSystemEventHandler):
    """Watches for new plugins and installs dependencies automatically."""

    IGNORED_DIRS = [
        ".git",
        "__pycache__",
        ".venv",
        "venv",
        "env",
        ".env",
        ".idea",
        ".vscode",
        ".pytest_cache",
        ".mypy_cache",
    ]
    
    def on_created(self, event):
        if os.path.isdir(event.src_path) and not any(
            ignored_dir in event.src_path for ignored_dir in self.IGNORED_DIRS
        ):
            plugin_name = os.path.basename(event.src_path)
            print(f"New plugin detected: {plugin_name}")

            # Check for pyproject.toml (Poetry) or requirements.txt (pip)
            pyproject_path = os.path.join(event.src_path, "pyproject.toml")

            if os.path.exists(pyproject_path):
                print(f"Installing dependencies for {plugin_name} with Poetry...")
                subprocess.run(
                    ["poetry", "install"],
                    cwd=event.src_path,
                    check=True)
            
            # Restart server
            print("Restarting FastAPI server...")
            self.force_restart(event)
    
    def force_restart(self, event):
        trigger_file_path = f"{'/'.join(event.src_path.split('/')[0:-2])}/main.py"
        # os.utime(trigger_file_path, None)  # Try updating the timestamp

