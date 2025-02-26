import sys


def generateFours(target: int):
    ops = ['+', '-', '/', '*']
    solutions = {}
    flag = False
    
    for i in ops:
        if flag:
            break
        for j in ops:
            if flag:
                break
            for k in ops:
                eq = '4 ' + i + ' 4 ' + j + ' 4 ' + k + ' 4'
                val = eval(eq.replace('/', '//'))
                if val == target:
                    print(eq + ' = ' + str(target))
                    flag = True
    
    if not flag:
        print("no solution")

def main():
    n = input()
    for line in sys.stdin:
        line = line[:-1]
        generateFours(int(line))

if __name__ == "__main__":
    main()