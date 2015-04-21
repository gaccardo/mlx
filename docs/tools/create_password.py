from passlib.hash import md5_crypt
import sys

h = md5_crypt.encrypt(sys.argv[1])
print h
