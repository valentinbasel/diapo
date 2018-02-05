# diapo

Diapo es un pequeño software para el diseño de presentaciones en formato
SVG, usanod el plugin SOZI de inkscape.

La idea principal es poder contar con un generador de presentaciones en
SVG usando un archivo de texto plano basado en RST (aunque no  es completamente RST).

# Como usar

para crear un archivo de presentación, hay que tener dos archivos, un
config.ini con los datos de configuración y un archivo .txt con las presentaciones en formato RST.

para probar un Demo se puede usar:

python diapo.py -c demo/config.ini -s demo/diapo.txt -f demo/presentacion.svg

donde:

-c : Configuracion de la presentación.
-s : Archivo RST con las presentaciones.
-f : El resultado final de la creación de la presentación.
