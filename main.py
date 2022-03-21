from fastapi import FastAPI
import random
app = FastAPI()

Recommanded_Games = ["GTA 5","Red Dead Redemption 2","Assassins Creed Valhalla","Valorant","CS:GO","Sleeping Dogs","Need for Speed","Resident Evil"]
@app.get("/")
async def root():
    choice = random.randint(0,len(Recommanded_Games))
    #Yaha change kara hai
    return {"Try this game":Recommanded_Games[choice]}
