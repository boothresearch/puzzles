def main():
    data = input('Enter a phrase: ')
    data = [i[0] for i in data.upper().split(' ')]
    print(''.join(data))

if __name__ == '__main__':
    main()

