import os
import itertools

ban = '''
                                                    '''

print('''\033[91m

     ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
     ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
     ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   
     ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   
     ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   
      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                               		 
                     \033[91m
''')

scale = input('\033[36m[!] provide a size scale [eg: "4 to 8" = 4:8] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
    first_name = str(input("\n\033[36m[*] First Name: "))
    last_name = str(input("\n\033[36m[*] Last Name: "))
    birthday = str(input("\n\033[36m[*] Birthday: "))
    month = str(input("\n\033[36m[*] Month: "))
    year = str(input("\n\033[36m[*] Year: "))
    chrs = first_name + last_name + birthday + month + year
else:
    chrs = 'abcdefghijklmnopqrstuvwxyz'
    pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

total_combinations = sum(len(chrs) ** i for i in range(start, final + 1))
generated_combinations = 0

directory = input('\n\033[36m[!] Specify directory path or leave blank for current directory: ')
if directory:
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)

file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
file_name = os.path.join(directory, file_name + '.txt')

arq = open(file_name, 'w')

if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
    chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
    chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
    chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final + 1):
    for j in itertools.product(chrs, repeat=i):
        temp = ''.join(j)
        arq.write(temp + '\n')
        generated_combinations += 1

        # Calculate and display the percentage
        percentage = (generated_combinations / total_combinations) * 100
        print(f"Completion: {percentage:.2f}%\r", end='', flush=True)

# Ensure the completion reaches 100%
print("Completion: 100.00%")

arq.close()
