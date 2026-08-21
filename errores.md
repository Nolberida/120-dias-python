# Libreta de errores del reto
## Error 1 — ValueError
- Qué hice: int("hola")
- Qué dijo Python: ValueError: invalid literal for int() with base 10: 'hola'
- Por qué: int() solo convierte textos que parecen números


## Error 2 — ValueError (otra vez)
- Qué hice: escribí "mil novecientos noventa y cinco" cuando int(input()) esperaba un número
- Qué dijo Python: Traceback (most recent call last):
  File "/home/ruben/120-dias-python/bloque1_fundamentos/bloque1_fundamentos/dia02_fstrings.py", line 37, in <module>
    print(f"hola {nombre2} , tu edad es {2026-int(anio)} años")
                                              ^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'mil novecientos noventa y cinco'
- Por qué: input() siempre devuelve texto, e int() solo convierte textos que parecen números
- Se parece al Error 1 en: es el mismo ValueError; ayer lo provoqué yo con int("hola"), hoy lo provocó "el usuario" al escribir con letras