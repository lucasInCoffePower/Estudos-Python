def converter_seg_em_min(segundos: float):
    return segundos/60


def converter_MB_em_Mb(dado: int):
    return dado*8


def calcular_tempo_download(tam_arquivo:float, largura_de_banda:float ):
    return tam_arquivo/largura_de_banda


def receber_largura_internet():
    return int(input('Tamanho do link de internet(Mbps): '))


def receber_tamanho_arquivo():
    return int(input('Tamanho do arquivo em MB: '))


def main():
    tam_arquivo = converter_MB_em_Mb(receber_tamanho_arquivo())
    largura_de_banda = receber_largura_internet()
    minutos_download = converter_seg_em_min(calcular_tempo_download(tam_arquivo, largura_de_banda))
    print(f'Tempo estimado de download: {minutos_download:.2f}min')
    


if __name__ == '__main__':
    main()
