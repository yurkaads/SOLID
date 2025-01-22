from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

# Клас, який реалізує лише друк
class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

# Клас, який реалізує функціонал сканування
class SimpleScanner(Scanner):
    def scan(self, document):
        print(f"Scanning: {document}")

# Клас, який реалізує і друк, і сканування
class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

# Використання
printer = SimplePrinter()
printer.print("Document1")

scanner = SimpleScanner()
scanner.scan("Document2")

multi_device = MultiFunctionDevice()
multi_device.print("Document3")
multi_device.scan("Document4")
