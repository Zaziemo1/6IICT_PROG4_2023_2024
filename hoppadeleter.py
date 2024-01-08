import os


directory = "/path/to/your/directory"

for i in range(1, 3000):
    filename = f"hoppa{i}"
    filepath = os.path.join(directory, filename)

    try:
        os.remove(filepath)
        print(f"Deleted: {filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error deleting {filename}: {e}")