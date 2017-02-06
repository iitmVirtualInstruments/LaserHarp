import ctypes
from ctypes import wintypes
import time
import serial
from statistics import mode

user32 = ctypes.WinDLL('user32', use_last_error=True)
VK_TAB  = 0x09
VK_MENU = 0x12
VK_CONTROL = 0X11
VK_UP = 0X26
VK_DOWN = 0X28
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_Q = 0x51
VK_W = 0x57
VK_E = 0x45
VK_R = 0x52
VK_T = 0x54
VK_Y = 0x59
VK_U = 0x55
VK_I = 0x49
VK_KEY_2 = 0x32 
VK_KEY_3 = 0x33
VK_KEY_5 = 0x35
VK_KEY_6 = 0x36
VK_KEY_7 = 0x37
#dict={'a':0x32,'c':0x33,'e':0x52,'f':0x35,'h':0x36,'j':0x37,'l':0x49,'z':0x41}
ser = serial.Serial('COM8',9600)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

#msdn.microsoft.com/en-us/library/dd375731

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def Upkey():
	
	PressKey(VK_UP)
	time.sleep(2)
	ReleaseKey(VK_UP)

def Downkey():
	
	PressKey(VK_DOWN)
	time.sleep(2)
	ReleaseKey(VK_UP)

def akey():
	
	PressKey(VK_A)
	time.sleep(2)
	ReleaseKey(VK_A)

def bkey():
	
	PressKey(VK_B)
	#time.sleep(1)
	ReleaseKey(VK_B)
def ckey():
	
	PressKey(VK_C)
	#time.sleep(1)
	ReleaseKey(VK_C)
def bckey():
	
	PressKey(VK_B)
	PressKey(VK_C)
	time.sleep(2)
	ReleaseKey(VK_B)
	ReleaseKey(VK_C)
def qkey():
	
	PressKey(VK_Q)
	#time.sleep(1)
	ReleaseKey(VK_Q)
def wkey():
	
	PressKey(VK_W)
	#time.sleep(1)
	ReleaseKey(VK_W)
def ekey():
	
	PressKey(VK_E)
	#time.sleep(1)
	ReleaseKey(VK_E)
def rkey():
	
	PressKey(VK_R)
	#time.sleep(1)
	ReleaseKey(VK_R)
def tkey():
	
	PressKey(VK_T)
	#time.sleep(1)
	ReleaseKey(VK_T)
def ykey():
	
	PressKey(VK_Y)
	#time.sleep(1)
	ReleaseKey(VK_Y)
def ukey():
	
	PressKey(VK_U)
	#time.sleep(1)
	ReleaseKey(VK_U)
def ikey():
	
	PressKey(VK_I)
	#time.sleep(1)
	ReleaseKey(VK_I)
def key2():
	
	PressKey(VK_2)
	#time.sleep(1)
	ReleaseKey(VK_2)
def key3():
	
	PressKey(VK_3)
	#time.sleep(1)
	ReleaseKey(VK_3)
def key5():
	
	PressKey(VK_5)
	#time.sleep(1)
	ReleaseKey(VK_5)
def key6():
	
	PressKey(VK_6)
	#time.sleep(1)
	ReleaseKey(VK_6)
def key7():
	
	PressKey(VK_7)
	#time.sleep(1)
	ReleaseKey(VK_7)

pvalue='z'
phex=0x41
datahex=0x41
PressKey(VK_A)
if __name__ == "__main__":
	while True:
		data3=ser.read(5)
		data2=data3.split()
		try:
			data=mode(data2)
		except:
			data=pvalue
		print(data)
		#print(data)
		print('pvalue=',pvalue)
		'''pvalue=data
        if (data!=pvalue):
        	ReleaseKey(int(dict(pvalue.decode('ascii')),16))

        	PressKey(int(dict(data.decode('ascii')),16))
        	PressKey(VK_I)
        	time.sleep(1)
        	ReleaseKey(VK_I)
        	print('world')
        else:	
        	print('Hello')
        rvalue=data
        print('rvalue=',rvalue)'''
		ser.flushInput()
		
#dict={'a':0x32,'c':0x33,'e':0x52,'f':0x35,'h':0x36,'j':0x37,'l':0x49,'z':0x41}
		
		if data.decode('ascii') == 'a':
			PressKey(0x51) #i
			#time.sleep(0.1)
			datahex=0x51
		if data.decode('ascii') == 'b':
			PressKey(0x32) #9
			#time.sleep(0.1)
			datahex=0x32
		if data.decode('ascii') == 'c':
			PressKey(0x57) #o
			#time.sleep(0.1)
			datahex=0x57
		if data.decode('ascii') == 'd':
			PressKey(0x33) #0
			#time.sleep(0.1)
			datahex=0x33
		if data.decode('ascii') == 'e':
			PressKey(0x45) #p
			#time.sleep(0.1)
			datahex=0x45
		if data.decode('ascii') == 'f':
			PressKey(0x52) #[
			#time.sleep(0.1)
			datahex=0x52
		if data.decode('ascii') == 'g':
			PressKey(0x35) #=
			#time.sleep(0.1)
			datahex=0x35
		if data.decode('ascii') == 'h':
			PressKey(0x42) #b
			#time.sleep(0.1)
			datahex=0x42	
		
						
		if data.decode('ascii') == 'z':
		    PressKey(0x41) #i
		    datahex=0x41	
		if data!=pvalue:
			ReleaseKey(phex)
		pvalue=data
		phex=datahex

        
