order={
    'size':'venti',
    'notes':'no whip',
    'drink':'mocha latte',
    'serve':'for here'
}

match order:
    case {'size':'tall',
          'serve':'for here',
          'drink':drink }:
        print(f"Filling ceramic mug with {drink}.")
    case {'size':'grande',
          'serve':'to go',
          'drink':drink }:
        print(f"Filling large paper cup with {drink}.")
    case {'size':'venti',
          'serve':'for here',
          'drink':drink }:
        print(f"Filling extra large tumbler with {drink}.")

        print (drink)

        
