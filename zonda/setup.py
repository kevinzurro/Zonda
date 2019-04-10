# Copyright (c) 2019, Eduardo Di Loreto <efdiloreto@gmail.com>

# This file is part of Zonda.

# Zonda is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Zonda is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Zonda.  If not, see <https://www.gnu.org/licenses/>.

import sys
import os
from cx_Freeze import setup, Executable
from gui import __about__, CARPETA_ICONOS, LICENCIA


build_exe_opciones = dict(
    packages=[
        'numpy.core._methods', 'numpy.lib.format', 'asyncio', 'jinja2'
    ],
    excludes=[
        'tkinter', 'PyQt5.QtBluetooth', 'PyQt5.QtNetwork', 'PyQt5.QtNfc',
        'PyQt5.QtWebChannel', 'PyQt5.QtWebSockets', 'PyQt5.QtWebEngineCore'
        'PyQt5.QtSql', 'PyQt5.QtNetwork', 'PyQt5.QtScript'
    ],
    include_files=[LICENCIA],
    optimize=2,
)

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

target = Executable(
    script='main.py',
    base=base,
    targetName='Zonda.exe',
    icon=os.path.join(CARPETA_ICONOS, 'zonda.ico'),
    copyright=__about__.__autor__
)

setup(
    name='Zonda',
    version=__about__.__version__,
    author=__about__.__autor__,
    description='Cálculo de carga de viento de acuerdo a CIRSOC 102-2005',
    options={'build_exe': build_exe_opciones},
    executables=[target]
)