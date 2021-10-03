eventos = [
  ((2020, 1, 13), (11, 50), 'Renovar identidade'),
  ((2020, 1, 15), (16, 30), 'Fazer compras'),
  ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
  ((2020, 2, 29), (14, 15), 'Prestar concurso'),
  ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
  ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista')]


def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
    agenda = []

    for evento in eventos:
        data = evento[0]
        if(data[0]>=de_data[0] and data[0]<=ate_data[0]):
            if(data[1]>=de_data[1] and data[1]<=ate_data[1]):
                if((data[2]>=de_data[2] or (data[2]<de_data[2]and data[1]>de_data[1])) and (data[2]<=ate_data[2] or (data[2]>ate_data[2] and data[1]<ate_data[1]))):
                    agenda.append(evento)
    
    for evento in agenda:
        print('{} - {}: {}'.format(formatar_data(evento[0]), formatar_hora(evento[1]), evento[2]))

def formatar_data(data):
    meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
    
    dia=''
    if(len(str(data[2])) == 1):
        dia='0'+str(data[2])
    else:
        dia=str(data[2])

    mes = meses[data[1]-1]

    return '{}/{}/{}'.format(dia, mes, data[0])

def formatar_hora(hora):
    return '{}:{}'.format(hora[0], hora[1])

imprimir_eventos(eventos, ate_data=(2020, 3, 15))
print('\n')
imprimir_eventos(eventos, (2020, 1, 20))