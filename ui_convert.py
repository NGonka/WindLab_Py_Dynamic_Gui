# http://www.swharden.com/wp/2016-07-30-live-data-in-pyqt4-with-matplotlibwidget/

from PyQt4 import uic
import glob
for fname in glob.glob("*.ui"):
    print("converting",fname)
    fin = open(fname,'r')
    fout = open(fname.replace(".ui",".py"),'w')
    uic.compileUi(fin,fout,execute=False)
    fin.close()
    fout.close()
