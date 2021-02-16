
# incluir src en la ruta de acceso al modulo para testearlo desde pytets
# no incluir src en la ruta si se ejecuta el modulo en modo main desde CLI python 
# from loose_change_invariantes import COIN_KEYS, COIN_VALUES
from loose_change_invariantes import COIN_KEYS, COIN_VALUES

# Para desactivar las aserciones:
# python3 -O src/loose_change.py 

def loose_change(cents):

    # PRECONDICIONES
    assert not isinstance(cents, list)
    assert isinstance(COIN_KEYS, list)
    assert isinstance(COIN_VALUES, list)

    wallet = dict(zip(COIN_KEYS, COIN_VALUES))

    assert len(wallet) == len(COIN_KEYS)
    assert len(wallet) == len(COIN_VALUES)

    coins = list(sorted(wallet.values()))
    
    assert len(coins) == len(wallet)
    assert coins[0] == 1
    assert coins[3] == 25

    change = []
    i = len(coins) - 1
    while cents > 0 and i >= 0:
        if cents >= coins[i]:
            cents = cents - coins[i]
            change.append(coins[i])
        else:
            i -= 1

    change_dict = dict.fromkeys(COIN_KEYS, 0)
    assert 'Pennies' in change_dict
    assert change_dict['Pennies'] == 0

    for coin in change:
        for coin_keys in wallet:
            if wallet[coin_keys] == coin:
                change_dict[coin_keys] += 1

    # POSTCONDICION complicada
    assert len(change_dict) == len(COIN_KEYS)
    return change_dict

if __name__ == "__main__":

    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
