times = ('flamengo', 'internacional', 'sãopaulo', 'atletico', 'fluminense', 'palmeiras', 'gremio', 'santos', 'athletico-pr',
     'ceara sc', 'corinthians', 'bragantino', 'atletico-go', 'sport recif', 'bahia', 'fortaleza', 'vasco',
     'goias', 'coritiba', 'bostafogo')
print("Os cinco primeiros colocados são: {}".format(times[0:5]))
print("Os quatro ultimos colocados são: {}".format(times[-4]))
print("Em ordem alfabetica: ")
print(sorted(times))
print("O corinthians está na {}".format(times.index("corinthians")))