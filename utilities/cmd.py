import os

class color:
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magneta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    reset = '\u001b[0m'

class window:
    def clear():
        return os.system('CLS')
    
    def resize(x, y):
        return os.system(f'mode con cols={x} lines={y}')
    
    def title(name):
        return os.system(f'title {name}')

def main():
    import os

if __name__ == '__main__':
    main()
