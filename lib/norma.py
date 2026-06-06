class Norma:
    def __init__(self):
        self.registrars : dict = {'A': 0,'B': 0,'C': 0,
                                'D': 0,'E': 0,'F': 0,
                                'G': 0,'H': 0} 
        self.opperations : dict[int,list[str]] 
    
    def push_register(self, label: str) -> None:
        self.registrars[label] = 0
        return

    def pop_register(self, label: str) -> None:
        if label in self.registrars:
            for index, register in enumerate(self.registrars):
                if register == label:
                   self.registrars.pop(index)
                   return
        print(f'> The register {label} is not in the machine.')
        return

    def add(self, label: str) -> None:
        self.registrars[label] += 1
        return

    def sub(self, label: str) -> None:
        self.registrars[label] -= 1
        return

    def is_zero(self, label: str) -> bool:
        return self.registrars[label] == 0

    def work(self) -> None:
        working: bool = True
        current_opper: int = 1 # Starts on fisrt.
        while working:
            if current_opper not in self.opperations:
                print('> steps outside the machine.')
                working = False

            for opperation in self.opperations:
                if opperation == current_opper:
                    opper: str = self.opperations[opperation][0]
                    register: str = self.opperations[opperation][1]

                    if opper == 'ADD':
                        self.add(register)
                        current_opper = int(self.opperations[opperation][2])
                        print('> add.')
                        continue

                    elif opper == 'SUB':
                        self.sub(register)
                        current_opper = int(self.opperations[opperation][2])
                        print('> sub.')
                        continue

                    current_opper = int(self.opperations[opperation][2]) if self.is_zero(register) else int(self.opperations[opperation][3])
                    print('> is zero.')
                    continue
        return