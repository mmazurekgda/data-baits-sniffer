from time import sleep
import kfp

if __name__ == "__main__":
    print("Welcome to the Data-Baits-Sniffer!")
    while True:
        print("Checking for new experiments...")
        print(kfp.Client().list_experiments())
        sleep(secs=60)
