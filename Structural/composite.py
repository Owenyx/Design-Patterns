from abc import ABC, abstractmethod
from typing import List

# Component interface
class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def display(self, indent: str = "") -> None:
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size
    
    def display(self, indent: str = "") -> None:
        print(f"{indent}File: {self.name} ({self._size}KB)")
    
    def get_size(self) -> int:
        return self._size

# Specialized Leaf classes
class ImageFile(File):
    def display(self, indent: str = "") -> None:
        print(f"{indent}Image File: {self.name} ({self._size}KB)")

class DocumentFile(File):
    def display(self, indent: str = "") -> None:
        print(f"{indent}Document File: {self.name} ({self._size}KB)")

class ExecutableFile(File):
    def display(self, indent: str = "") -> None:
        print(f"{indent}Executable File: {self.name} ({self._size}KB)")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)
    
    def display(self, indent: str = "") -> None:
        print(f"{indent}Directory: {self.name} ({self.get_size()}KB)")
        for child in self._children:
            child.display(indent + "  ")
    
    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

# Client code
def main():
    # Create root directory
    root = Directory("root")
    
    # Create and populate Documents directory
    docs = Directory("Documents")
    docs.add(DocumentFile("resume.pdf", 500))
    docs.add(ImageFile("photo.jpg", 2000))
    
    # Create and populate Project directory
    project = Directory("Project")
    project.add(ExecutableFile("main.exe", 10))
    project.add(DocumentFile("data.csv", 5000))
    
    # Add Project to Documents
    docs.add(project)
    
    # Add Documents to root
    root.add(docs)
    
    # Add some files directly to root
    root.add(DocumentFile("config.xml", 100))
    root.add(DocumentFile("readme.txt", 50))
    
    # Display the entire file system
    print("File System Structure:")
    root.display()
    
    print(f"\nTotal size: {root.get_size()}KB")

if __name__ == "__main__":
    main() 