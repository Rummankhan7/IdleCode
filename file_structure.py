from pathlib import Path

def generate_folder_structure(dir_path: str | Path, indent: str = "") -> None:
    path = Path(dir_path)
    
    
    if not path.exists():
        print(f"Error: The path '{dir_path}' does not exist.")
        return
    if not path.is_dir():
        print(f"Error: The path '{dir_path}' is not a directory.")
        return

    
    if indent == "":
        print(f"📁 {path.name}/")

    
    try:
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(f"{indent}└── [Permission Denied]")
        return

    
    for index, item in enumerate(items):
        is_last = (index == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        if item.is_dir():
            print(f"{indent}{connector}📁 {item.name}/")
            # Create a deeper indent for the next level
            next_indent = indent + ("    " if is_last else "│   ")
            generate_folder_structure(item, next_indent)
        else:
            print(f"{indent}{connector}📄 {item.name}")


if __name__ == "__main__":
    # Replace this with the path you want to scan
    target_directory = "D:\sih" 
    
    print(f"Generating structure for: {target_directory}\n")
    generate_folder_structure(target_directory)
