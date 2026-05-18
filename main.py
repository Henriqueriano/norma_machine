from norma import Norma
from norma_utils import (
        allocate_in_norma,
        update_register
        )

def main():
    machine : Norma = Norma()
    
    choice: int = int(input('> number of registrars (base 8): '))
    machine = allocate_in_norma(machine, choice)

    needs_add : str = input('> do u needs add value into register (y/n)? ')
    if (needs_add.lower().strip() == 'y'):
        update_register(machine)

    file_name: str = input('> file name: ')  
    file_content: list[dict] = load_file(f'./{file_name}')

    print(machine.registers)

if __name__ == '__main__':
    while True: # main loop
        try:
            main()
        except Exception as err:
            print(err)
        except KeyboardInterrupt:
            print('\n> ending program . . .')
            break

