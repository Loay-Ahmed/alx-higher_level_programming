#!/usr/bin/python3
if __name__ == "__main__":
    with open("hidden_4.pyc", "r") as f:
        for line in f:
            if line[0] != "__":
                print(line)
