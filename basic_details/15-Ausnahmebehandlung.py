"""
try:
except:
"""
import sys

# Bsp 1: Int Zahlen prüfen
while True:
    try:
        zahl = input("Int Zahl eingeben: ")
        zahl = int(zahl)
        break
    except ValueError as e:
        print("Error: ", e)


# Bsp 2: Mehrere Exceptions
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as err:
    (errno, strerror) = err.args
    print("I/O error ({0}): {1}".format(errno, strerror))
except ValueError:
    print("No valid int value.")
except:
    (type, value, traceback) = sys.exc_info()
    print("Type: ", type)
    print("Value: ", value)
    print("traceback: ", traceback)

    #print("Unexpected error: ", sys.exc_info()[0])
    raise # führt gerade abgefangene Ausnahme nochmal aus
    # dadurch kann man diese Ausnahme an anderer Stelle wieder auffangen


# Final
try:
    x = float(input("Your number: "))
    inverse = 1.0/x
finally:
    print("Ich werde immer ausgegeben.")