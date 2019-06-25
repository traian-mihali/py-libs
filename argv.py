import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python3 sys-argv.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
