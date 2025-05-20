import os

script_template = {
    "posix": "python3 dist/testRunner.py config.json",
    "nt": "python dist\\testRunner.py config.json",
}

script = script_template.get(os.name)
if script is None:
    raise ValueError("Unsupported OS")

os.system(script)

input("Press Enter to exit...")
