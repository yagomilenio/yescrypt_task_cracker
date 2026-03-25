import struct
import os

"""
">"  →  big-endian (el byte más significativo va primero)
"Q"  →  unsigned long long = entero de 8 bytes (offset, máx 18 petabytes)
"I"  →  unsigned int       = entero de 4 bytes (length, máx 4 GB por registro)

de este modo me deja 12 bytes es decir 12 caracteres
"""

def max_offset_from_file(filepath: str) -> int: #retorna el valor en bytes
    size = os.path.getsize(filepath)
    return size-1

def leer_y_dividir_fichero(ruta_fichero, delimitador="\n"):
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        contenido = f.read()
    
    return contenido.split(delimitador)


def calcular_offsets(lista, delimitador='\n'):
    resultado = []
    offset = 0
    
    for elemento in lista:
        longitud = len(elemento)
        resultado.append((offset, longitud))
        offset += longitud + len(delimitador)
    
    return resultado


def bytes_necesarios_offsets(lista_offsets):
    max_offset = 0
    max_len = 0
    
    for offset, longitud in lista_offsets:
        if offset > max_offset:
            max_offset = offset
        if longitud > max_len:
            max_len = longitud
    
    def bytes_necesarios(n):
        if n == 0:
            return 1
        return (n.bit_length() + 7) // 8
    
    return (bytes_necesarios(max_offset), bytes_necesarios(max_len))


def ancho_fijo_por_caracter(lista_offsets):
    max_offset = max(offset for offset, _ in lista_offsets)
    max_len = max(length for _, length in lista_offsets)
    ancho_offset = len(str(max_offset))
    ancho_len = len(str(max_len))
    return ancho_offset, ancho_len


def escribir_offsets_texto(ruta_fichero, lista_offsets, ancho_offset, ancho_len, separador=" "):
    with open(ruta_fichero, "w", encoding="utf-8") as f:
        for offset, longitud in lista_offsets:
            line = f"{offset:0{ancho_offset}d} {longitud:0{ancho_len}d}\n"
            f.write(line)
    print(f"Bytes por cada entrada en fichero de indices: {len(line)}")




if __name__ == "__main__":

    FILEPATH = "rockyou_1k.txt"
    
    items = leer_y_dividir_fichero(FILEPATH)
    offsets = calcular_offsets(items)
    o, l = ancho_fijo_por_caracter(offsets)
    escribir_offsets_texto(f"{FILEPATH}.idx", offsets, o, l)

