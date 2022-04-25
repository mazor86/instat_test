import sys

sys.path.append('..')
import moduleA


def main():
    instance = moduleA.ModuleA()
    instance.greeting()


if __name__ == '__main__':
    main()
