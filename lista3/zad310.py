for l in range(100, 401):
    lista = ['200', '202', '204', '206', '208', '220', '222', '224', '226', '228', '240', '242', '244', '246', '248',
             '260', '262', '264', '266', '268', '280', '282', '284', '286', '288', '400']

    # Każda z wyżej wymienionych liczb spełnia wymagania i są to wszystkie liczby spełniające te wymaganie,
    # jeśli wszystkie zostaną usuniete z listy, znaczy to że program znalazł wszystkie rozwiązania,
    # i wtedy zostanie wydrukowany zapis powyższej listy.

    z = lista
    r = list(str(l))
    k = [2, 4, 6, 8, 0]
    if r[0] == str(k[0]):
        if r[1] == str(k[0]):
            if r[2] == str(k[0]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
                print(lista)
            if r[2] == str(k[1]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[2]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[3]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[4]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
        if r[1] == str(k[1]):
            if r[2] == str(k[0]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[1]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[2]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[3]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[4]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
        if r[1] == str(k[2]):
            if r[2] == str(k[0]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[1]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[2]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[3]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[4]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
        if r[1] == str(k[3]):
            if r[2] == str(k[0]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[1]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[2]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[3]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[4]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
        if r[1] == str(k[4]):
            if r[2] == str(k[0]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[1]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[2]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[3]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
            if r[2] == str(k[4]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
    if r[0] == str(k[1]):
        if r[1] == str(k[4]):
            if r[1] == str(k[4]):
                lista.remove(''.join(r))
                if lista == []:
                    print(z)
