from lupa.lua54 import LuaRuntime
import PySimpleGUI as psg
lua = LuaRuntime(unpack_returned_tuples=True)
lua.eval('1+1')
g = lua.globals()
g.psg = psg
f = open("main.lua")
lua.execute(f.read())
f.close()