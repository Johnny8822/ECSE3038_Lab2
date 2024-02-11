from fastapi import FastAPI 

app = FastAPI()

data = [] 

@app.post("/person") 
async def create_person(person):
    if not person.get("occupation") or not person.get("name") or not person.get("address"):
        result = {"error_message": "invalid request"}    
        print(result)
        return result
    else:
        data.append(person)
        result = "success" 
        print(data)
        return result
        

@app.get("/person")
def get_person():
    return data
