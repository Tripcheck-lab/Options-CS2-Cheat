import pymem.process

pm = pymem.Pymem("cs2.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll")

dwLocalPlayerPawn = pm.read_longlong(client.lpBaseOfDll + 0x1824A18)
# https://github.com/sezzyaep/CS2-OFFSETS/blob/main/offsets.hpp dwLocalPlayerPawn
pm.write_float(dwLocalPlayerPawn + 0x1358, 0.0)
# https://github.com/sezzyaep/CS2-OFFSETS/blob/main/client.dll.cs m_flFlashMaxAlpha
