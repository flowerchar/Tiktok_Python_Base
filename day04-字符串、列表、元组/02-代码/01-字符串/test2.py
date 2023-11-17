import os

def rename_files():
    current_path = os.getcwd()
    for filename in os.listdir(current_path):
        if filename.endswith(".py") and filename.startswith("hm_"):
            new_filename = filename.replace("hm_", "")
            os.rename(filename, new_filename)
            print(f"Renamed: {filename} to {new_filename}")

if __name__ == "__main__":
    rename_files()
