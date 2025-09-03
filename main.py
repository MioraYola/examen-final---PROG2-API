from fastapi import FastAPI

app = FastAPI()

@app.get("/health", )
def health():
    return {"message": "ok"}
list_phones=[] 

     phone(BaseModels){
        identifier str,
        brand str,
        model str, 
        characteristics Characteristics {
           ram_memory int, 
           rom_memory int
        }
    }
@app.post("/phones")
def phone(): 
