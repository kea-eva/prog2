# if løkke - at prøve indtil en betingelse er mødt

temp = 25
nat = 4
sol = 18
skyer = 12

if temp > sol:
    print("\n Meget varmt \n")
elif temp < sol and temp > skyer:
    print("\n Lidt varme \n")
elif temp < skyer and temp > nat:
    print("\n Lidt koldt \n")
else:
    print("\n meget kaldt \n")
