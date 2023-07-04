import fastapi
import pandas as pd
#from fastapi import File, UploadFile, FastAPI
import uvicorn 

#from starlette.responses import RedirectResponse

app=fastapi(title='Consulta de FILMS')

@app.get("/")

def funcion():
  return "hola mundo"

def dayofweek(d, m, y):
    ''' funcion para hallar el numero de dia 0,1,2,3,4,5,6
    dic={1:'lunes',2:'martes',3:'miercoles',4:'jueves',5:'viernes',6:'sabado',0:'domingo'}'''
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)

