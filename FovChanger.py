import pymem.process

pm = pymem.Pymem("cs2.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll")

dwLocalPlayerController = pm.read_longlong(client.lpBaseOfDll + 0x1A0E9C8)
# https://github.com/sezzyaep/CS2-OFFSETS/blob/main/offsets.hpp dwLocalPlayerController

pm.write_int(dwLocalPlayerController + 0x6C4, 90)
# https://github.com/sezzyaep/CS2-OFFSETS/blob/main/client.dll.cs m_iDesiredFOV
