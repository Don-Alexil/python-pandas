import pandas as pd

medals = {'bronze' : 25, 'gold' : 15, 'silver': 20 }

for medal_type in medals:
    print(medal_type + ' medal  was won ' + str(medals[medal_type]))
