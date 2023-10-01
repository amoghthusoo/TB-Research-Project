import hashlib as hl
import os

class Remove_Duplicates:

    def __init__(self, path : str) -> None:
        self.path = path

    def run(self) -> None:

        list_of_files = os.walk(self.path)

        hash_dict : dict = dict()

        for root, folders, files in list_of_files:

            for file in files:
                
                file_hash : str = hl.md5(open(file, "rb").read()).hexdigest()

                if (file_hash not in hash_dict):
                    hash_dict[file_hash] = file
                else:
                    os.remove(file)

def main() -> None:
    path : str = r"C:\Users\Dell\Desktop\Automation\Removing_Duplicates"
    obj = Remove_Duplicates(path)
    obj.run()

if __name__ == "__main__":
    main()
    