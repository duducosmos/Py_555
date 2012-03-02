from distutils.core import setup
import py2exe
excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list",
            "Tkconstants","Tkinter","tcl"
            ]

setup(windows=['Py555.py'])
