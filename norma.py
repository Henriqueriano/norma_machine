class Norma:
    def __init__(self):
        self.registers : list[dict] = [{'A': 0},{'B': 0},{'C': 0},
                                       {'D': 0},{'E': 0},{'F': 0},
                                       {'G': 0},{'H': 0},] 
    
    def push_register(self, label: str) -> None:
        self.registers.append(label)

    def pop_register(self, label: str) -> None:
        pass

    def add(self, register: str, jmp: int) -> None:
        pass

    def sub(self, register: str, jmp: int) -> None:
        pass

    def is_zero(self, register: str, true_jmp: int, false_jmp: int) -> bool:
        pass
 
