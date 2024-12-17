from typing import Dict, Any

# Complex subsystem classes
class CPU:
    def __init__(self):
        self._position = 0
        self._registers = {}
    
    def freeze(self) -> None:
        print("CPU: Freezing processor.")
    
    def jump(self, position: int) -> None:
        self._position = position
        print(f"CPU: Jumping to position {position}.")
    
    def execute(self) -> None:
        print("CPU: Executing commands from current position.")

class Memory:
    def __init__(self):
        self._memory: Dict[int, Any] = {}
    
    def load(self, position: int, data: Any) -> None:
        self._memory[position] = data
        print(f"Memory: Loading data '{data}' to position {position}.")
    
    def free(self, position: int) -> None:
        if position in self._memory:
            del self._memory[position]
            print(f"Memory: Freeing position {position}.")

class HardDrive:
    def __init__(self):
        self._sectors: Dict[int, Any] = {}
    
    def read(self, sector: int, size: int) -> str:
        data = f"data from sector {sector} with size {size}"
        print(f"HardDrive: Reading {data}.")
        return data
    
    def write(self, sector: int, data: Any) -> None:
        self._sectors[sector] = data
        print(f"HardDrive: Writing '{data}' to sector {sector}.")

class PowerUnit:
    def __init__(self):
        self._power_on = False
    
    def power_on(self) -> None:
        self._power_on = True
        print("PowerUnit: Supplying power to all components.")
    
    def power_off(self) -> None:
        self._power_on = False
        print("PowerUnit: Cutting power to all components.")
    
    @property
    def is_powered(self) -> bool:
        return self._power_on

# Facade
class ComputerFacade:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hard_drive = HardDrive()
        self._power_unit = PowerUnit()
    
    def start(self) -> None:
        print("\nComputer is starting up...")
        self._power_unit.power_on()
        self._cpu.freeze()
        self._memory.load(0, "boot_sector")
        self._cpu.jump(0)
        self._cpu.execute()
    
    def shutdown(self) -> None:
        print("\nComputer is shutting down...")
        self._cpu.freeze()
        self._memory.free(0)
        self._power_unit.power_off()
    
    def process_file(self, sector: int) -> None:
        print(f"\nProcessing file from sector {sector}...")
        self._cpu.freeze()
        data = self._hard_drive.read(sector, 128)
        self._memory.load(0, data)
        self._cpu.jump(0)
        self._cpu.execute()
        self._memory.free(0)

# Client code
def main():
    # Create the facade
    computer = ComputerFacade()
    
    # Use the simplified interface
    computer.start()
    computer.process_file(5)
    computer.process_file(7)
    computer.shutdown()

if __name__ == "__main__":
    main() 