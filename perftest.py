from time import perf_counter
import os, nilslib
from sys import stdout

out = ""

t = perf_counter()
print("Hello World my name is Nils")
out += f"{nilslib.clampDecimalPlace(9, perf_counter() - t)} "

t = perf_counter()
stdout.write("Hello World my name is Nils")
out += f"{nilslib.clampDecimalPlace(9, perf_counter() - t)} "

t = perf_counter()
os.system("echo Hello World my name is Nils")
out += f"{nilslib.clampDecimalPlace(9, perf_counter() - t)} "

print("\n\n\n")
os.system("cls")

print(out)