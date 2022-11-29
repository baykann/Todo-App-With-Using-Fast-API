from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import connection
app = FastAPI()
statusList=["pending","rejected","in-progress","done"]  # Status durumuna göre girdileri ekrana yazdırabilmek için bir liste oluşturduk.

class Todo(BaseModel): # HTTP protokolüyle gelen JSON verisini alabilmek için bir sınıfı oluşturduk.

    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=200)
    date: str
    status: str = Field (min_lengt=1)

@app.get("/")      # Get komutu tanımladık ve SQL sorgusu ile ilişkilendirdik.
def get_all_todos():
    return connection.get_all()


@app.post("/")     # Post komutu tanımladık ve SQL sorgusu ile ilişkilendirdik.
def Create_todos(todo : Todo):
    if statusList.__contains__(todo.status.lower()): #Kullanıcılardan sadece listedeki status değerlerini girmeleri istendi.
        connection.add_item(name=todo.name,description=todo.description,status=todo.status.lower(),date=todo.date)

        return {"New work is added"}
    return {"Please input valid status.(pending , in-progress , rejected , done)"}


@app.put("/{checklist_id}")  # Put komutu tanımladık ve SQL sorgusu ile ilişkilendirdik.
def update(checklist_id : str , todo : Todo):
    if statusList.__contains__(todo.status.lower()):
        connection.update(checklist_id,todo.name,todo.description,todo.date,todo.status)

        return {"The update was succesful."};
    return"Please input valid status.(pending , in-progress , rejected , done)"

@app.delete("/{checklist_id}") # Delete komutu tanımladık ve SQL sorgusu ile ilişkilendirdik.
def delete(checklist_id : str ):
    connection.delete(checklist_id);
    return {"The delete was succesful."}


@app.get("/{status}")    # Status durumuna göre DB'den çağrılacak girdiler için GET komutu eklendi.
def get_todos_by_state(status):
    return connection.getTodosByState(status)
