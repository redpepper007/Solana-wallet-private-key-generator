import base58
from solders.keypair import Keypair #type: ignore
from solders.pubkey import Pubkey  # type: ignore
import time
import os
import sys
import datetime
os.system('color'); green = '\033[32m'; red = '\033[31m'; yellow = '\033[33m'; reset = '\033[0m'
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "keyfinder.txt")
script_filename = os.path.basename(__file__)

total = 0

print(f'\n{green}Script will eventually generate the PRIVATE KEY for any SOL wallet of your choice\nUse only for educational purposes, positive result will take some time (maybe too much){reset}\n{yellow}Terminate with [ CTRL+C ] for a summary{reset}\n')
wallet = str(input('> Enter wallet address: '))

if len(wallet) != 44:
    print(f"{red}The {wallet} is not a valid SOL address, check and try again{reset}")
    time.sleep(5)
    sys.exit()

print(f'\nWorking, please wait...\n')
start_time = datetime.datetime.now()

while True:
    try:
        account = Keypair()
        privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
        walletAddress = account.pubkey()

        if walletAddress == wallet:
            print('\n')
            print(f'{red}Wallet address: {walletAddress}\nPrivate key: {privateKey}{reset}\n')
            with open(desktop_path, 'a') as file:
                file.write(f"{walletAddress} - {privateKey}\n")
            print(f"Wallet data saved to your Desktop: keyfinder.txt")
            time.sleep(99999)
        total += 1

        if total % 100000 == 0:
            print(f"{total} private keys checked for {wallet}")

    except KeyboardInterrupt:
        now_time = datetime.datetime.now() - start_time
        passed_seconds = now_time.total_seconds()
        speed = total/passed_seconds
        print(f'\n{yellow}Total checked {total} private keys in {now_time}\nSpeed was {speed:.0f} wal/sec{reset}\n')
        time.sleep(999)
        break
