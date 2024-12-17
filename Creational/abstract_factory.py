from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def paint(self):
        return "Rendering a Windows button"

class MacButton(Button):
    def paint(self):
        return "Rendering a Mac button"

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Rendering a Windows checkbox"

class MacCheckbox(Checkbox):
    def paint(self):
        return "Rendering a Mac checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()

# Client code
def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button.paint(), checkbox.paint()

def main():
    windows_factory = WindowsFactory()
    mac_factory = MacFactory()
    
    print("Windows GUI:", create_gui(windows_factory))
    print("Mac GUI:", create_gui(mac_factory))

if __name__ == "__main__":
    main() 