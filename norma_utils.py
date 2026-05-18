from norma import Norma

def allocate_in_norma(machine: Norma, qt: int) -> Norma:
    if qt > 8:
        print('> alocating registrars . . .')
        for i in range(73, 65 + qt):
            new: chr = chr(i)
            machine.push_register({f'{new}': 0})
    return machine

def update_register(machine: Norma) -> None:
        specific_register: str = input('> register: ')  \
        .upper()                                        \
        .strip()
        new_value: int = int(input('> new value: '))
        machine.registers[specific_register] = new_value
 

