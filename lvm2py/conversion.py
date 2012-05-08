#This file is part of lvm2py.

#reparted is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#reparted is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with reparted.  If not, see <http://www.gnu.org/licenses/>.

from ctypes.util import find_library
from ctypes import *

lib = find_library("lvm2app")

if not lib:
    raise Exception("Parted library not found.")

lvm = CDLL(lib)

version = lvm.lvm_library_get_version
version.argtypes = [c_void_p]
version.restype = c_char_p