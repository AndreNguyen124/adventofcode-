def openFile():
    inputFile = open('text.txt', 'r')
    depths = list(map(int, inputFile.read().splitlines()))
    return depths


def solution(list):
    increased = 0
    for i in range(len(list)):
        counter = i - 1
        if list[i] > list[counter]:
            increased += 1
    print(increased)


if __name__ == '__main__':
    pass
    # print(openFile())
    list = openFile()
    solution(list)
