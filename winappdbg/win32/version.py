#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009-2011, Mario Vilas
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Detect the current architecture and operating system.
"""

__revision__ = "$Id$"

from defines import *

#--- OSVERSIONINFO and OSVERSIONINFOEX structures and constants ---------------

VER_PLATFORM_WIN32s                 = 0
VER_PLATFORM_WIN32_WINDOWS          = 1
VER_PLATFORM_WIN32_NT               = 2

VER_SUITE_BACKOFFICE                = 0x00000004
VER_SUITE_BLADE                     = 0x00000400
VER_SUITE_COMPUTE_SERVER            = 0x00004000
VER_SUITE_DATACENTER                = 0x00000080
VER_SUITE_ENTERPRISE                = 0x00000002
VER_SUITE_EMBEDDEDNT                = 0x00000040
VER_SUITE_PERSONAL                  = 0x00000200
VER_SUITE_SINGLEUSERTS              = 0x00000100
VER_SUITE_SMALLBUSINESS             = 0x00000001
VER_SUITE_SMALLBUSINESS_RESTRICTED  = 0x00000020
VER_SUITE_STORAGE_SERVER            = 0x00002000
VER_SUITE_TERMINAL                  = 0x00000010
VER_SUITE_WH_SERVER                 = 0x00008000

VER_NT_DOMAIN_CONTROLLER            = 0x0000002
VER_NT_SERVER                       = 0x0000003
VER_NT_WORKSTATION                  = 0x0000001

VER_BUILDNUMBER                     = 0x0000004
VER_MAJORVERSION                    = 0x0000002
VER_MINORVERSION                    = 0x0000001
VER_PLATFORMID                      = 0x0000008
VER_PRODUCT_TYPE                    = 0x0000080
VER_SERVICEPACKMAJOR                = 0x0000020
VER_SERVICEPACKMINOR                = 0x0000010
VER_SUITENAME                       = 0x0000040

VER_EQUAL                           = 1
VER_GREATER                         = 2
VER_GREATER_EQUAL                   = 3
VER_LESS                            = 4
VER_LESS_EQUAL                      = 5
VER_AND                             = 6
VER_OR                              = 7

# typedef struct _OSVERSIONINFO {
#   DWORD dwOSVersionInfoSize;
#   DWORD dwMajorVersion;
#   DWORD dwMinorVersion;
#   DWORD dwBuildNumber;
#   DWORD dwPlatformId;
#   TCHAR szCSDVersion[128];
# }OSVERSIONINFO;
class OSVERSIONINFOA(Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", DWORD),
        ("dwMajorVersion",      DWORD),
        ("dwMinorVersion",      DWORD),
        ("dwBuildNumber",       DWORD),
        ("dwPlatformId",        DWORD),
        ("szCSDVersion",        CHAR * 128),
    ]
class OSVERSIONINFOW(Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", DWORD),
        ("dwMajorVersion",      DWORD),
        ("dwMinorVersion",      DWORD),
        ("dwBuildNumber",       DWORD),
        ("dwPlatformId",        DWORD),
        ("szCSDVersion",        WCHAR * 128),
    ]

# typedef struct _OSVERSIONINFOEX {
#   DWORD dwOSVersionInfoSize;
#   DWORD dwMajorVersion;
#   DWORD dwMinorVersion;
#   DWORD dwBuildNumber;
#   DWORD dwPlatformId;
#   TCHAR szCSDVersion[128];
#   WORD  wServicePackMajor;
#   WORD  wServicePackMinor;
#   WORD  wSuiteMask;
#   BYTE  wProductType;
#   BYTE  wReserved;
# }OSVERSIONINFOEX, *POSVERSIONINFOEX, *LPOSVERSIONINFOEX;
class OSVERSIONINFOEXA(Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", DWORD),
        ("dwMajorVersion",      DWORD),
        ("dwMinorVersion",      DWORD),
        ("dwBuildNumber",       DWORD),
        ("dwPlatformId",        DWORD),
        ("szCSDVersion",        CHAR * 128),
        ("wServicePackMajor",   WORD),
        ("wServicePackMinor",   WORD),
        ("wSuiteMask",          WORD),
        ("wProductType",        BYTE),
        ("wReserved",           BYTE),
    ]
class OSVERSIONINFOEXW(Structure):
    _fields_ = [
        ("dwOSVersionInfoSize", DWORD),
        ("dwMajorVersion",      DWORD),
        ("dwMinorVersion",      DWORD),
        ("dwBuildNumber",       DWORD),
        ("dwPlatformId",        DWORD),
        ("szCSDVersion",        WCHAR * 128),
        ("wServicePackMajor",   WORD),
        ("wServicePackMinor",   WORD),
        ("wSuiteMask",          WORD),
        ("wProductType",        BYTE),
        ("wReserved",           BYTE),
    ]

LPOSVERSIONINFOA    = POINTER(OSVERSIONINFOA)
LPOSVERSIONINFOW    = POINTER(OSVERSIONINFOW)
LPOSVERSIONINFOEXA  = POINTER(OSVERSIONINFOEXA)
LPOSVERSIONINFOEXW  = POINTER(OSVERSIONINFOEXW)
POSVERSIONINFOA     = LPOSVERSIONINFOA
POSVERSIONINFOW     = LPOSVERSIONINFOW
POSVERSIONINFOEXA   = LPOSVERSIONINFOEXA
POSVERSIONINFOEXW   = LPOSVERSIONINFOA

#--- GetSystemMetrics constants -----------------------------------------------

SM_CXSCREEN             = 0
SM_CYSCREEN             = 1
SM_CXVSCROLL            = 2
SM_CYHSCROLL            = 3
SM_CYCAPTION            = 4
SM_CXBORDER             = 5
SM_CYBORDER             = 6
SM_CXDLGFRAME           = 7
SM_CYDLGFRAME           = 8
SM_CYVTHUMB             = 9
SM_CXHTHUMB             = 10
SM_CXICON               = 11
SM_CYICON               = 12
SM_CXCURSOR             = 13
SM_CYCURSOR             = 14
SM_CYMENU               = 15
SM_CXFULLSCREEN         = 16
SM_CYFULLSCREEN         = 17
SM_CYKANJIWINDOW        = 18
SM_MOUSEPRESENT         = 19
SM_CYVSCROLL            = 20
SM_CXHSCROLL            = 21
SM_DEBUG                = 22
SM_SWAPBUTTON           = 23
SM_RESERVED1            = 24
SM_RESERVED2            = 25
SM_RESERVED3            = 26
SM_RESERVED4            = 27
SM_CXMIN                = 28
SM_CYMIN                = 29
SM_CXSIZE               = 30
SM_CYSIZE               = 31
SM_CXFRAME              = 32
SM_CYFRAME              = 33
SM_CXMINTRACK           = 34
SM_CYMINTRACK           = 35
SM_CXDOUBLECLK          = 36
SM_CYDOUBLECLK          = 37
SM_CXICONSPACING        = 38
SM_CYICONSPACING        = 39
SM_MENUDROPALIGNMENT    = 40
SM_PENWINDOWS           = 41
SM_DBCSENABLED          = 42
SM_CMOUSEBUTTONS        = 43

SM_CXFIXEDFRAME         = SM_CXDLGFRAME     # ;win40 name change
SM_CYFIXEDFRAME         = SM_CYDLGFRAME     # ;win40 name change
SM_CXSIZEFRAME          = SM_CXFRAME        # ;win40 name change
SM_CYSIZEFRAME          = SM_CYFRAME        # ;win40 name change

SM_SECURE               = 44
SM_CXEDGE               = 45
SM_CYEDGE               = 46
SM_CXMINSPACING         = 47
SM_CYMINSPACING         = 48
SM_CXSMICON             = 49
SM_CYSMICON             = 50
SM_CYSMCAPTION          = 51
SM_CXSMSIZE             = 52
SM_CYSMSIZE             = 53
SM_CXMENUSIZE           = 54
SM_CYMENUSIZE           = 55
SM_ARRANGE              = 56
SM_CXMINIMIZED          = 57
SM_CYMINIMIZED          = 58
SM_CXMAXTRACK           = 59
SM_CYMAXTRACK           = 60
SM_CXMAXIMIZED          = 61
SM_CYMAXIMIZED          = 62
SM_NETWORK              = 63
SM_CLEANBOOT            = 67
SM_CXDRAG               = 68
SM_CYDRAG               = 69
SM_SHOWSOUNDS           = 70
SM_CXMENUCHECK          = 71  # Use instead of GetMenuCheckMarkDimensions()!
SM_CYMENUCHECK          = 72
SM_SLOWMACHINE          = 73
SM_MIDEASTENABLED       = 74
SM_MOUSEWHEELPRESENT    = 75
SM_XVIRTUALSCREEN       = 76
SM_YVIRTUALSCREEN       = 77
SM_CXVIRTUALSCREEN      = 78
SM_CYVIRTUALSCREEN      = 79
SM_CMONITORS            = 80
SM_SAMEDISPLAYFORMAT    = 81
SM_IMMENABLED           = 82
SM_CXFOCUSBORDER        = 83
SM_CYFOCUSBORDER        = 84
SM_TABLETPC             = 86
SM_MEDIACENTER          = 87
SM_STARTER              = 88
SM_SERVERR2             = 89
SM_MOUSEHORIZONTALWHEELPRESENT = 91
SM_CXPADDEDBORDER       = 92

SM_CMETRICS             = 93

SM_REMOTESESSION        = 0x1000
SM_SHUTTINGDOWN         = 0x2000
SM_REMOTECONTROL        = 0x2001
SM_CARETBLINKINGENABLED = 0x2002

#--- SYSTEM_INFO structure, GetSystemInfo() and GetNativeSystemInfo() ---------

# Values used by Wine
# Documented values at MSDN are marked with an asterisk
PROCESSOR_ARCHITECTURE_UNKNOWN        = 0xFFFF; # Unknown architecture.
PROCESSOR_ARCHITECTURE_INTEL          = 0       # x86 (AMD or Intel) *
PROCESSOR_ARCHITECTURE_MIPS           = 1       # MIPS
PROCESSOR_ARCHITECTURE_ALPHA          = 2       # Alpha
PROCESSOR_ARCHITECTURE_PPC            = 3       # Power PC
PROCESSOR_ARCHITECTURE_SHX            = 4       # SHX
PROCESSOR_ARCHITECTURE_ARM            = 5       # ARM
PROCESSOR_ARCHITECTURE_IA64           = 6       # Intel Itanium *
PROCESSOR_ARCHITECTURE_ALPHA64        = 7       # Alpha64
PROCESSOR_ARCHITECTURE_MSIL           = 8       # MSIL
PROCESSOR_ARCHITECTURE_AMD64          = 9       # x64 (AMD or Intel) *
PROCESSOR_ARCHITECTURE_IA32_ON_WIN64  = 10      # IA32 on Win64
PROCESSOR_ARCHITECTURE_SPARC          = 20      # Sparc (Wine)

# Values used by Wine
# PROCESSOR_OPTIL value found at http://code.google.com/p/ddab-lib/
# Documented values at MSDN are marked with an asterisk
PROCESSOR_INTEL_386     = 386    # Intel i386 *
PROCESSOR_INTEL_486     = 486    # Intel i486 *
PROCESSOR_INTEL_PENTIUM = 586    # Intel Pentium *
PROCESSOR_INTEL_IA64    = 2200   # Intel IA64 (Itanium) *
PROCESSOR_AMD_X8664     = 8664   # AMD X86 64 *
PROCESSOR_MIPS_R4000    = 4000   # MIPS R4000, R4101, R3910
PROCESSOR_ALPHA_21064   = 21064  # Alpha 210 64
PROCESSOR_PPC_601       = 601    # PPC 601
PROCESSOR_PPC_603       = 603    # PPC 603
PROCESSOR_PPC_604       = 604    # PPC 604
PROCESSOR_PPC_620       = 620    # PPC 620
PROCESSOR_HITACHI_SH3   = 10003  # Hitachi SH3 (Windows CE)
PROCESSOR_HITACHI_SH3E  = 10004  # Hitachi SH3E (Windows CE)
PROCESSOR_HITACHI_SH4   = 10005  # Hitachi SH4 (Windows CE)
PROCESSOR_MOTOROLA_821  = 821    # Motorola 821 (Windows CE)
PROCESSOR_SHx_SH3       = 103    # SHx SH3 (Windows CE)
PROCESSOR_SHx_SH4       = 104    # SHx SH4 (Windows CE)
PROCESSOR_STRONGARM     = 2577   # StrongARM (Windows CE)
PROCESSOR_ARM720        = 1824   # ARM 720 (Windows CE)
PROCESSOR_ARM820        = 2080   # ARM 820 (Windows CE)
PROCESSOR_ARM920        = 2336   # ARM 920 (Windows CE)
PROCESSOR_ARM_7TDMI     = 70001  # ARM 7TDMI (Windows CE)
PROCESSOR_OPTIL         = 0x494F # MSIL

# typedef struct _SYSTEM_INFO {
#   union {
#     DWORD dwOemId;
#     struct {
#       WORD wProcessorArchitecture;
#       WORD wReserved;
#     } ;
#   }     ;
#   DWORD     dwPageSize;
#   LPVOID    lpMinimumApplicationAddress;
#   LPVOID    lpMaximumApplicationAddress;
#   DWORD_PTR dwActiveProcessorMask;
#   DWORD     dwNumberOfProcessors;
#   DWORD     dwProcessorType;
#   DWORD     dwAllocationGranularity;
#   WORD      wProcessorLevel;
#   WORD      wProcessorRevision;
# } SYSTEM_INFO;

class _SYSTEM_INFO_OEM_ID_STRUCT(Structure):
    _fields_ = [
        ("wProcessorArchitecture",  WORD),
        ("wReserved",               WORD),
]

class _SYSTEM_INFO_OEM_ID(Union):
    _fields_ = [
        ("dwOemId",  DWORD),
        ("w",        _SYSTEM_INFO_OEM_ID_STRUCT),
]

class SYSTEM_INFO(Structure):
    _fields_ = [
        ("id",                              _SYSTEM_INFO_OEM_ID),
        ("dwPageSize",                      DWORD),
        ("lpMinimumApplicationAddress",     LPVOID),
        ("lpMaximumApplicationAddress",     LPVOID),
        ("dwActiveProcessorMask",           DWORD_PTR),
        ("dwNumberOfProcessors",            DWORD),
        ("dwProcessorType",                 DWORD),
        ("dwAllocationGranularity",         DWORD),
        ("wProcessorLevel",                 WORD),
        ("wProcessorRevision",              WORD),
    ]

    def __get_dwOemId(self):
        return self.id.dwOemId
    def __set_dwOemId(self, value):
        self.id.dwOemId = value
    dwOemId = property(__get_dwOemId, __set_dwOemId)

    def __get_wProcessorArchitecture(self):
        return self.id.w.wProcessorArchitecture
    def __set_wProcessorArchitecture(self, value):
        self.id.w.wProcessorArchitecture = value
    wProcessorArchitecture = property(__get_wProcessorArchitecture, __set_wProcessorArchitecture)

LPSYSTEM_INFO = ctypes.POINTER(SYSTEM_INFO)

# void WINAPI GetSystemInfo(
#   __out  LPSYSTEM_INFO lpSystemInfo
# );
def GetSystemInfo():
    _GetSystemInfo = windll.kernel32.GetSystemInfo
    _GetSystemInfo.argtypes = [LPSYSTEM_INFO]
    _GetSystemInfo.restype  = None

    sysinfo = SYSTEM_INFO()
    _GetSystemInfo(ctypes.byref(sysinfo))
    return sysinfo

# void WINAPI GetNativeSystemInfo(
#   __out  LPSYSTEM_INFO lpSystemInfo
# );
def GetNativeSystemInfo():
    _GetNativeSystemInfo = windll.kernel32.GetNativeSystemInfo
    _GetNativeSystemInfo.argtypes = [LPSYSTEM_INFO]
    _GetNativeSystemInfo.restype  = None

    sysinfo = SYSTEM_INFO()
    _GetNativeSystemInfo(ctypes.byref(sysinfo))
    return sysinfo

# int WINAPI GetSystemMetrics(
#   __in  int nIndex
# );
def GetSystemMetrics(nIndex):
    _GetSystemMetrics = windll.user32.GetSystemMetrics
    _GetSystemMetrics.argtypes = [ctypes.c_int]
    _GetSystemMetrics.restype  = ctypes.c_int
    return _GetSystemMetrics(nIndex)

# HANDLE WINAPI GetCurrentProcess(void);
def GetCurrentProcess():
##    return 0xFFFFFFFFFFFFFFFFL
    _GetCurrentProcess = windll.kernel32.GetCurrentProcess
    _GetCurrentProcess.argtypes = []
    _GetCurrentProcess.restype  = HANDLE
    return _GetCurrentProcess()

# HANDLE WINAPI GetCurrentThread(void);
def GetCurrentThread():
##    return 0xFFFFFFFFFFFFFFFEL
    _GetCurrentThread = windll.kernel32.GetCurrentThread
    _GetCurrentThread.argtypes = []
    _GetCurrentThread.restype  = HANDLE
    return _GetCurrentThread()

# BOOL WINAPI IsWow64Process(
#   __in   HANDLE hProcess,
#   __out  PBOOL Wow64Process
# );
def IsWow64Process(hProcess):
    _IsWow64Process = windll.kernel32.IsWow64Process
    _IsWow64Process.argtypes = [HANDLE, PBOOL]
    _IsWow64Process.restype  = bool
    _IsWow64Process.errcheck = RaiseIfZero

    Wow64Process = BOOL(FALSE)
    _IsWow64Process(hProcess, ctypes.byref(Wow64Process))
    return bool(Wow64Process)

# DWORD WINAPI GetVersion(void);
def GetVersion():
    _GetVersion = windll.kernel32.GetVersion
    _GetVersion.argtypes = []
    _GetVersion.restype  = DWORD
    _GetVersion.errcheck = RaiseIfZero

    # See the example code here:
    # http://msdn.microsoft.com/en-us/library/ms724439(VS.85).aspx

    dwVersion       = _GetVersion()
    dwMajorVersion  = dwVersion & 0x000000FF
    dwMinorVersion  = (dwVersion & 0x0000FF00) >> 8
    if (dwVersion & 0x80000000) == 0:
        dwBuild     = (dwVersion & 0x7FFF0000) >> 16
    else:
        dwBuild     = None
    return int(dwMajorVersion), int(dwMinorVersion), int(dwBuild)

# BOOL WINAPI GetVersionEx(
#   __inout  LPOSVERSIONINFO lpVersionInfo
# );
def GetVersionExA():
    _GetVersionExA = windll.kernel32.GetVersionExA
    _GetVersionExA.argtypes = [LPVOID]
    _GetVersionExA.restype  = bool
    _GetVersionExA.errcheck = RaiseIfZero

    osi = OSVERSIONINFOEXA()
    osi.dwOSVersionInfoSize = sizeof(osi)
    try:
        _GetVersionExA(ctypes.byref(osi))
    except WindowsError:
        osi = OSVERSIONINFOA()
        osi.dwOSVersionInfoSize = sizeof(osi)
        _GetVersionExA(ctypes.byref(osi))
    return osi

def GetVersionExW():
    _GetVersionExW = windll.kernel32.GetVersionExW
    _GetVersionExW.argtypes = [LPVOID]
    _GetVersionExW.restype  = bool
    _GetVersionExW.errcheck = RaiseIfZero

    osi = OSVERSIONINFOEXW()
    osi.dwOSVersionInfoSize = sizeof(osi)
    try:
        _GetVersionExW(ctypes.byref(osi))
    except WindowsError:
        osi = OSVERSIONINFOW()
        osi.dwOSVersionInfoSize = sizeof(osi)
        _GetVersionExW(ctypes.byref(osi))
    return osi

GetVersionEx = GuessStringType(GetVersionExA, GetVersionExW)

# BOOL WINAPI GetProductInfo(
#   __in   DWORD dwOSMajorVersion,
#   __in   DWORD dwOSMinorVersion,
#   __in   DWORD dwSpMajorVersion,
#   __in   DWORD dwSpMinorVersion,
#   __out  PDWORD pdwReturnedProductType
# );
def GetProductInfo(dwOSMajorVersion, dwOSMinorVersion, dwSpMajorVersion, dwSpMinorVersion):
    _GetProductInfo = windll.kernel32.GetProductInfo
    _GetProductInfo.argtypes = [DWORD, DWORD, DWORD, DWORD, PDWORD]
    _GetProductInfo.restype  = BOOL
    _GetProductInfo.errcheck = RaiseIfZero

    dwReturnedProductType = DWORD(0)
    _GetProductInfo(dwOSMajorVersion, dwOSMinorVersion, dwSpMajorVersion, dwSpMinorVersion, byref(dwReturnedProductType))
    return dwReturnedProductType.value

# BOOL WINAPI VerifyVersionInfo(
#   __in  LPOSVERSIONINFOEX lpVersionInfo,
#   __in  DWORD dwTypeMask,
#   __in  DWORDLONG dwlConditionMask
# );
def VerifyVersionInfo(lpVersionInfo, dwTypeMask, dwlConditionMask):
    if isinstance(lpVersionInfo, OSVERSIONINFOEXA):
        return VerifyVersionInfoA(lpVersionInfo, dwTypeMask, dwlConditionMask)
    if isinstance(lpVersionInfo, OSVERSIONINFOEXW):
        return VerifyVersionInfoW(lpVersionInfo, dwTypeMask, dwlConditionMask)
    raise TypeError("Bad OSVERSIONINFOEX structure")

def VerifyVersionInfoA(lpVersionInfo, dwTypeMask, dwlConditionMask):
    _VerifyVersionInfoA = windll.kernel32.VerifyVersionInfoA
    _VerifyVersionInfoA.argtypes = [LPOSVERSIONINFOEXA, DWORD, DWORDLONG]
    _VerifyVersionInfoA.restype  = bool
    return _VerifyVersionInfoA(ctypes.byref(lpVersionInfo), dwTypeMask, dwlConditionMask)

def VerifyVersionInfoW(lpVersionInfo, dwTypeMask, dwlConditionMask):
    _VerifyVersionInfoW = windll.kernel32.VerifyVersionInfoW
    _VerifyVersionInfoW.argtypes = [LPOSVERSIONINFOEXW, DWORD, DWORDLONG]
    _VerifyVersionInfoW.restype  = bool
    return _VerifyVersionInfoW(ctypes.byref(lpVersionInfo), dwTypeMask, dwlConditionMask)

# ULONGLONG WINAPI VerSetConditionMask(
#   __in  ULONGLONG dwlConditionMask,
#   __in  DWORD dwTypeBitMask,
#   __in  BYTE dwConditionMask
# );
def VerSetConditionMask(dwlConditionMask, dwTypeBitMask, dwConditionMask):
    _VerSetConditionMask = windll.kernel32.VerSetConditionMask
    _VerSetConditionMask.argtypes = [ULONGLONG, DWORD, BYTE]
    _VerSetConditionMask.restype  = ULONGLONG
    return _VerSetConditionMask(dwlConditionMask, dwTypeBitMask, dwConditionMask)

#--- get_bits, get_arch and get_os --------------------------------------------

ARCH_UNKNOWN = "unknown"
ARCH_I386    = "i386"
ARCH_AMD64   = "amd64"
ARCH_IA64    = "ia64"

ARCH_IA32 = ARCH_I386
ARCH_X86  = ARCH_I386
ARCH_X64  = ARCH_AMD64

OS_UNKNOWN   = "Unknown"
OS_NT        = "Windows NT"
OS_W2K       = "Windows 2000"
OS_XP        = "Windows XP"
OS_XP_64     = "Windows XP (64 bits)"
OS_W2K3      = "Windows 2003"
OS_W2K3_64   = "Windows 2003 (64 bits)"
OS_W2K3R2    = "Windows 2003 R2"
OS_W2K3R2_64 = "Windows 2003 R2 (64 bits)"
OS_W2K8      = "Windows 2008"
OS_W2K8_64   = "Windows 2008 (64 bits)"
OS_W2K8R2    = "Windows 2008 R2"
OS_W2K8R2_64 = "Windows 2008 R2 (64 bits)"
OS_VISTA     = "Windows Vista"
OS_VISTA_64  = "Windows Vista (64 bits)"
OS_W7        = "Windows 7"
OS_W7_64     = "Windows 7 (64 bits)"

OS_SEVEN    = OS_W7
OS_SEVEN_64 = OS_W7_64

OS_WINDOWS_NT         = OS_NT
OS_WINDOWS_2000       = OS_W2K
OS_WINDOWS_XP         = OS_XP
OS_WINDOWS_XP_64      = OS_XP_64
OS_WINDOWS_2003       = OS_W2K3
OS_WINDOWS_2003_64    = OS_W2K3_64
OS_WINDOWS_2003_R2    = OS_W2K3R2
OS_WINDOWS_2003_R2_64 = OS_W2K3R2_64
OS_WINDOWS_2008       = OS_W2K8
OS_WINDOWS_2008_64    = OS_W2K8_64
OS_WINDOWS_2008_R2    = OS_W2K8R2
OS_WINDOWS_2008_R2_64 = OS_W2K8R2_64
OS_WINDOWS_VISTA      = OS_VISTA
OS_WINDOWS_VISTA_64   = OS_VISTA_64
OS_WINDOWS_SEVEN      = OS_W7
OS_WINDOWS_SEVEN_64   = OS_W7_64

def _get_bits():
    """
    Determines the current integer size in bits.

    This is useful to know if we're running in a 32 bits or a 64 bits machine.

    @rtype: int
    @return: Returns the size of L{SIZE_T} in bits.
    """
    return sizeof(SIZE_T) * 8

# Current integer size in bits. See L{_get_bits} for more details.
bits = _get_bits()

def _get_arch():
    """
    Determines the current processor architecture.

    @rtype: str
    @return:
        One of the following values:
         - L{ARCH_UNKNOWN} (C{"unknown"})
         - L{ARCH_I386} (C{"i386"}) for Intel 32-bit x86 processor or compatible.
         - L{ARCH_AMD64} (C{"amd64"}) for Intel 64-bit x86_64 processor or compatible.
         - L{ARCH_IA64} (C{"ia64"}) for Intel Itanium processor or compatible.
    """
    try:
        si = GetNativeSystemInfo()
    except Exception:
        si = GetSystemInfo()
    wProcessorArchitecture = si.id.w.wProcessorArchitecture
    if wProcessorArchitecture == PROCESSOR_ARCHITECTURE_INTEL:
        return ARCH_I386
    if wProcessorArchitecture == PROCESSOR_ARCHITECTURE_AMD64:
        return ARCH_AMD64
    if wProcessorArchitecture == PROCESSOR_ARCHITECTURE_IA64:
        return ARCH_IA64
    return ARCH_UNKNOWN

# Current processor architecture. See L{_get_arch} for more details.
arch = _get_arch()

def _get_wow64():
    """
    Determines if the current process is running in Windows-On-Windows 64 bits.

    @rtype:  bool
    @return: C{True} of the current process is a 32 bit program running in a
        64 bit version of Windows, C{False} if it's either a 32 bit program
        in a 32 bit Windows or a 64 bit program in a 64 bit Windows.
    """
    # Try to determine if the debugger itself is running on WOW64.
    # On error assume False.
    if bits == 64:
        wow64 = False
    else:
        try:
            wow64 = IsWow64Process( GetCurrentProcess() )
        except Exception:
            wow64 = False
    return wow64

# Set to C{True} if the current process is running in WOW64. See L{_get_wow64} for more details.
wow64 = _get_wow64()

def _get_os():
    """
    Determines the current operating system.

    This function allows you to quickly tell apart major OS differences.
    For more detailed information call L{kernel32.GetVersionEx} instead.

    @note:
        Wine reports itself as Windows XP 32 bits (even if the Linux host is 64 bits).
        ReactOS reports itself as Windows 2000.

    @rtype: str
    @return:
        One of the following values:
         - L{OS_UNKNOWN} (C{"Unknown"})
         - L{OS_NT} (C{"Windows NT"})
         - L{OS_W2K} (C{"Windows 2000"})
         - L{OS_XP} (C{"Windows XP"})
         - L{OS_XP_64} (C{"Windows XP (64 bits)"})
         - L{OS_W2K3} (C{"Windows 2003"})
         - L{OS_W2K3_64} (C{"Windows 2003 (64 bits)"})
         - L{OS_W2K3R2} (C{"Windows 2003 R2"})
         - L{OS_W2K3R2_64} (C{"Windows 2003 R2 (64 bits)"})
         - L{OS_W2K8} (C{"Windows 2008"})
         - L{OS_W2K8_64} (C{"Windows 2008 (64 bits)"})
         - L{OS_W2K8R2} (C{"Windows 2008 R2"})
         - L{OS_W2K8R2_64} (C{"Windows 2008 R2 (64 bits)"})
         - L{OS_VISTA} (C{"Windows Vista"})
         - L{OS_VISTA_64} (C{"Windows Vista (64 bits)"})
         - L{OS_W7} (C{"Windows 7"})
         - L{OS_W7_64} (C{"Windows 7 (64 bits)"})
    """
    # rough port of http://msdn.microsoft.com/en-us/library/ms724429%28VS.85%29.aspx
    osvi = GetVersionEx()
    if osvi.dwPlatformId == VER_PLATFORM_WIN32_NT and osvi.dwMajorVersion > 4:
        if osvi.dwMajorVersion == 6:
            if osvi.dwMinorVersion == 0:
                if osvi.wProductType == VER_NT_WORKSTATION:
                    if bits == 64 or wow64:
                        return 'Windows Vista (64 bits)'
                    return 'Windows Vista'
                else:
                    if bits == 64 or wow64:
                        return 'Windows 2008 (64 bits)'
                    return 'Windows 2008'
            if osvi.dwMinorVersion == 1:
                if osvi.wProductType == VER_NT_WORKSTATION:
                    if bits == 64 or wow64:
                        return 'Windows 7 (64 bits)'
                    return 'Windows 7'
                else:
                    if bits == 64 or wow64:
                        return 'Windows 2008 R2 (64 bits)'
                    return 'Windows 2008 R2'
        if osvi.dwMajorVersion == 5:
            if osvi.dwMinorVersion == 2:
                if GetSystemMetrics(SM_SERVERR2):
                    if bits == 64 or wow64:
                        return 'Windows 2003 R2 (64 bits)'
                    return 'Windows 2003 R2'
                if osvi.wSuiteMask in (VER_SUITE_STORAGE_SERVER, VER_SUITE_WH_SERVER):
                    if bits == 64 or wow64:
                        return 'Windows 2003 (64 bits)'
                    return 'Windows 2003'
                try:
                    si = GetNativeSystemInfo()
                except Exception:
                    si = GetSystemInfo()
                if osvi.wProductType == VER_NT_WORKSTATION and si.wProcessorArchitecture == PROCESSOR_ARCHITECTURE_AMD64:
                    return 'Windows XP (64 bits)'
                else:
                    if bits == 64 or wow64:
                        return 'Windows 2003 (64 bits)'
                    return 'Windows 2003'
            if osvi.dwMinorVersion == 1:
                return 'Windows XP'
            if osvi.dwMinorVersion == 0:
                return 'Windows 2000'
        if osvi.dwMajorVersion == 4:
            return 'Windows NT'
    return 'Unknown'

# Current operating system. See L{_get_os} for more details.
os = _get_os()
