if __name__ == "__main__":
    print("Welcome to the Data-Baits-Sniffer!")
    import kfp

    print(kfp.Client().list_experiments())
