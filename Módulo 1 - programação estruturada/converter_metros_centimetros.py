






def converter_metros_centimetros(metros:float):
    return metros*100


def receber_metros():
    metros = float(input('Digite a medida em metros: '))
    return metros

def main():
    metros = receber_metros()
    centimetros = converter_metros_centimetros(metros)
    print(f'{metros} m = {centimetros} cm')


if __name__ == '__main__':
    main()
