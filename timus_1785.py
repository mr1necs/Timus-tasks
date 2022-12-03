def get_temp(temp):
    return {
        1 <= temp <= 4: 'few',
        5 <= temp <= 9: 'several',
        10 <= temp <= 19: 'pack',
        20 <= temp <= 49: 'lots',
        50 <= temp <= 99: 'horde',
        100 <= temp <= 249: 'throng',
        250 <= temp <= 499: 'swarm',
        500 <= temp <= 999: 'zounds',
        temp >= 1000: 'legion'
    }[True]


x = int(input())
print(get_temp(x))
