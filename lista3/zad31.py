x = input()
samogłoski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'ó', 'y', 'A', 'Ą', 'E', 'Ę', 'I', 'O', 'U', 'Ó', 'Y']
spółgłoski = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','R','T','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

if x in samogłoski:
    print("Samogłoska")
else:
    if x in spółgłoski:
        print("Spółgłoska")
    else:
            print("To nie jest litera!")
