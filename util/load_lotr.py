from pathlib import Path

def lotr_chapters():
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    file_path = project_dir / "lotr.txt"

    with open(file_path, "r") as file:
        text = file.read()

    chapters = text.split("\n\n")
    return chapters