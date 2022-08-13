from prisoner import Prison


def main(prisoner_num):
    print(f'rabok szama: {prisoner_num}')
    prison = Prison(prisoner_num)
    print(f'szabadulas napja: {prison.prison_break()}')


if __name__ == '__main__':
    main(20)
