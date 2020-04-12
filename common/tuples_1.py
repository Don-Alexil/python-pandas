girl_names = ['JADA', 'Emily', 'Ava', 'SERENITY', 'Claire', 'SOPHIA', 'Sarah', 'ASHLEY', 'CHAYA', 'ABIGAIL', 'Zoe', 'LEAH',  'HAILEY' ]
boy_names = ['JOSIAH', 'ETHAN', 'David', 'Jayden', 'MASON', 'RYAN', 'CHRISTIAN', 'ISAIAH', 'JAYDEN', 'Michael', 'NOAH', 'SAMUEL', 'SEBASTIAN' ]

# Pair up the boy and girl names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))