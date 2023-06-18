#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    f = dir(hidden_4)
    for line in f:
        if line[:2] != "__":
            print(line)
