'''
Kommandozeilenargumente
z.B. Kommandozeilenargumente.py -v -o meineDatei.txt

'''
import sys
import getopt

#print(sys.argv) # gibt alle Argumente aus

opts, rest = getopt.getopt(sys.argv[1:], "vbo:h")
# Erklärung: erste Eintrag ignorieren wir (wäre Pfad mit Dateiname)
# v entspricht '-v' als Argumnt
# b -> '-b'
# o: Doppelpunkt bedeutet, dass hinter '-o' noch ein weiterer Parameter erwartet wird (hier: Name der Output-Datei)
# h -> '-h'

def print_help():
    print('#'*20)
    print('Hilfe zum Kommandoargumente-Tool:')
    print('#'*20)

for opt, arg in opts:
    if opt == '-v':
        verb = True

    # Kommandozeilenargumente.py -o meineDatei.txt
    if opt == '-o':
        output = arg
        print(f"output: {output}")

    if opt == '-h':
        print_help()

    #print(opt, arg)


