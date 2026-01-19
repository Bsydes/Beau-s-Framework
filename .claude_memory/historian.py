import os
import sys
import datetime

MEMORY_ROOT = os.path.expanduser("~/.claude_memory")


def update_folder_index(folder_path):
    """
    Generates a _CONTENTS.md file for a specific folder.
    This acts as the 'Description Front Matter' for tree traversal.
    """
    items = os.listdir(folder_path)
    # Filter out hidden files and the index itself
    items = [i for i in items if not i.startswith('.') and i != '_CONTENTS.md']
    items.sort()

    index_path = os.path.join(folder_path, "_CONTENTS.md")

    with open(index_path, "w") as f:
        f.write(f"# Index of {os.path.basename(folder_path)}\n\n")
        f.write("## Sub-Directories (Categories)\n")
        has_dirs = False
        for item in items:
            if os.path.isdir(os.path.join(folder_path, item)):
                f.write(f"- 📂 {item}/\n")
                has_dirs = True
        if not has_dirs:
            f.write("(None)\n")

        f.write("\n## Memory Snapshots (Files)\n")
        has_files = False
        for item in items:
            if os.path.isfile(os.path.join(folder_path, item)):
                f.write(f"- 📄 {item}\n")
                has_files = True
        if not has_files:
            f.write("(None)\n")


def save_snapshot(path_structure, message, content=None):
    """
    Saves a file deep in the tree and updates indexes all the way up.
    path_structure: 'workflows/finance' (creates folders if missing)
    """
    # 1. Construct full path
    full_dir = os.path.join(MEMORY_ROOT, path_structure)
    if not os.path.exists(full_dir):
        os.makedirs(full_dir)

    # 2. Save the Snapshot
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_name = message.replace(" ", "_").replace("/", "-")[:40]
    filename = f"{timestamp}_{clean_name}.md"

    with open(os.path.join(full_dir, filename), "w") as f:
        f.write(f"# {message}\n\n{content or 'No content provided.'}")

    print(f"✅ Saved to: {path_structure}/{filename}")

    # 3. Recursive Re-Indexing (The 'Traversal' Enabler)
    # We update the index in the target folder, then its parent, then root.
    current = full_dir
    while True:
        update_folder_index(current)
        if os.path.abspath(current) == os.path.abspath(MEMORY_ROOT):
            break
        current = os.path.dirname(current)

    print("🔄 Tree Indexes Updated.")


def save_checkpoint(message, project_path="."):
    """
    Project-local checkpoints for plugin workflows.
    Unlike save_snapshot (global memory tree), this creates quick checkpoints
    in the current project's .claude_memory/checkpoints directory.

    Args:
        message: Description of the checkpoint
        project_path: Path to project root (defaults to current directory)

    Returns:
        Path to the created checkpoint file
    """
    checkpoint_dir = os.path.join(project_path, ".claude_memory", "checkpoints")
    os.makedirs(checkpoint_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{checkpoint_dir}/{timestamp}_snapshot.md"

    with open(filename, "w") as f:
        f.write(f"# Checkpoint: {timestamp}\n\n")
        f.write(f"## Context\n{message}\n\n")
        f.write(f"## Timestamp\n{datetime.datetime.now().isoformat()}\n")

    print(f"✅ Checkpoint: {filename}")
    return filename


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 historian.py 'folder/subfolder' 'Message' 'Optional Content'")
    else:
        path = sys.argv[1]
        msg = sys.argv[2]
        content = sys.argv[3] if len(sys.argv) > 3 else "Snapshot"
        save_snapshot(path, msg, content)
