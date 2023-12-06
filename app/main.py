from time import sleep
from datetime import datetime
import kfp

if __name__ == "__main__":
    print("Welcome to the Data-Baits-Sniffer!")
    while True:
        print("Checking for new experiments...")
        print(kfp.Client().list_experiments())
        print(kfp.Client().list_experiments(namespace="jb-admin"))
        print(f"Checked at: {datetime.now()}")
        sleep(60)
