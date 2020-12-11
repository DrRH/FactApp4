from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import basedatos as bd

app= FastAPI()

#Petición a una ruta
@app.get("/clientes/lista")

#Asincrona, la función no se ejecuta constantemente con las demas funciones 
async def enlistar_clientes():
    #Devuelve el codigo http 200
    return  bd.lista_clientes()

<<<<<<< HEAD
@app.post("/clientes/agregar/")

async def agregar_cliente(cliente: bd.Cliente):
    operacion_exitosa = bd.ingresar_cliente(cliente)
    if operacion_exitosa:
        return {"mensaje":"Cliente creado"}

    else:
        raise HTTPException(status_code=400, detail="Cliente existente") 
    
=======
#@app.post("/clientes/agregar/")

#async def agregar_cliente(cliente: Cliente):
>>>>>>> b71293a8726eaf60a090d3c715b5118d62d90bfd
