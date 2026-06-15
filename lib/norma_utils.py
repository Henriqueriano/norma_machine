from lib import norma

def allocate_in_norma(machine: norma.Norma, qt: int) -> norma.Norma:
    if qt < 8:
        print('> alocating 8 base registrars . . .')
    if qt > 8:
        print(f'> alocating {qt} registrars (8 base + {qt - 8} aux). . .')
        for i in range(73, 65 + qt):
            new: chr = chr(i)
            machine.push_register(new)
    return machine

def update_register(machine: norma.Norma, label: str, value: int) -> None:
        if label not in machine.registrars:
             print('> unknow register.')
             return
        machine.registrars[label] = value

def show_registers(machine: norma.Norma):
    for register in machine.registrars:
         print(f'{register} => {machine.registrars[register]}')

def show_opperations(machine: norma.Norma) -> None:
     print(machine.opperations)

def load_opperation_file(machine: norma.Norma, file_path: str) -> None:
    path : str = './assets/'+file_path+'/macro'
    bucket: dict[int, list[str]] = {}
    try:
        with open(path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                elif line.__contains__('&'): # KKKKKKKKKKKKKKKKKKKK here, I'm genius 
                     continue
                norm: list[str] = line.strip().split()
                bucket[int(norm[0])] = [norm[i] for i in range(1, len(norm))]
        machine.opperations = bucket
    except FileNotFoundError:
         print('> file not found on assets folder.')