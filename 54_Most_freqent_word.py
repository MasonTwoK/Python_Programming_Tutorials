from collections import Counter

text = " Ayy, I remember syrup sandwiches and crime allowances " \
       "Finesse a nigga with some counterfeits, but now I’m countin' this" \
       "Parmesan where my accountant lives; in fact, I'm downin’ this " \
       "D'USSÉ with my boo bae tastes like Kool-Aid for the analysts" \
       "Girl, I can buy yo' ass the world with my paystub" \
       "Ooh, that pussy good, won't you sit it on my taste bloods?" \
       "I get way too petty once you let me do the extras" \
       "Pull up on your block, then break it down: we playin' Tetris" \
       "A.M. to the P.M., P.M. to the A.M., funk" \
       "Piss out your per diem, you just gotta hate 'em, funk" \
       "If I quit your BM, I still ride Mercedes, funk" \
       "If I quit this season, I still be the greatest, funk" \
       "My left stroke just went viral" \
       "Right stroke put lil' baby in a spiral" \
       "Soprano C, we like to keep it on a high note" \
       "It's levels to it, you and I know " \



words = text.split()

counter = Counter(text)
top_tree = counter.most_common(3)

print(top_tree)