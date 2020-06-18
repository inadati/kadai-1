# python version 3.7 anaconda3-2019.10
import glob


def main():
    files = glob.glob("./src/**/*", recursive=True)

    for file in files:
        print(file.replace("./src/", ""))


if __name__ == '__main__':
    main()