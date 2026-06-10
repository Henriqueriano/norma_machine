import os
import subprocess
from time import sleep
from lib.norma import Norma
from lib.norma_utils import (
        allocate_in_norma,
        update_register,
        load_opperation_file,
        show_registers,
        show_opperations,
        )

def main() -> None:
    # Setup some stuffs
    delay: int = 0

    # Allocating machine.
    machine : Norma = Norma()
    choice: int = int(input('> number of registrars (base 8): '))
    allocate_in_norma(machine, choice)
    show_registers(machine)

    # Updating register flux
    does_user_update_register: str = str(input('> do u want update some register value (y/n)?')).lower() \
    .strip()

    if does_user_update_register not in ['y', 'n']:
        raise ValueError('> value not inside the choice options.')

    updating: bool = True if does_user_update_register == 'y' else False
    while updating:
        label: str = str(input('> label of the register: ')).upper()
        value: int = int(input('> value of the register: '))
        update_register(machine=machine, label=label, value=value)

        again: str = str(input('> again (y/n)?')).lower() \
        .strip()
        if again == 'n':
            updating = False
            subprocess.run('cls' if os.name == 'nt' else 'clear',
                        shell=True)

    # Loading the file.
    file_path: str = str(input('> named folder in assets: '))
    load_opperation_file(machine = machine, file_path = file_path)

    print('> loaded opperations: ')
    show_opperations(machine=machine)

    print(f'> starting the machine after {delay}s!')
    sleep(delay)
    machine.work()

   
if __name__ == '__main__':
    subprocess.run('cls' if os.name == 'nt' else 'clear',
                    shell=True)
    working: bool = True
    while working: # main loop
        try:
            main()
            working = False

        except Exception as err:
            delay: int = 5
            print(f'> aborting execution because: {err}!')
            print(f'> restarting application loop in {delay}s!')
            sleep(delay)
            subprocess.run('cls' if os.name == 'nt' else 'clear',
                            shell=True)

        except KeyboardInterrupt:
            print('\n> ending program . . .')
            break