import random

ibti = {
    "weapon": "sabre",
    "record": 0.9, 
    "score": 0, 
}

ibti["name"] = "Ibti"

rebecca = {
    "weapon": "sabre",
    "record": 0.5,
    "score": 0,
}
rebecca["name"] = "Rebecca"
# ibti["score"] = 3
# rebecca["score"] += 1
# can update values in dict by reassigning them

def bout(fencer1, fencer2):
    while fencer1["score"] < 5 and fencer2["score"] < 5:
        touch = random.choice((1, 2))
        if touch == 1:
            fencer1["score"] += 1
            print("Touch right")
        elif touch == 2:
            fencer2["score"] += 1
            print("Touch left")
    winner = fencer1 if fencer1["score"] > fencer2["score"] else fencer2
    print(f'{winner["name"]} has won the bout.')
    return

bout(ibti, rebecca)



