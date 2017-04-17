
from pyh import *
page = PyH('This is PyH page')
page << h1(cl='center', 'My')
table1 = page << table(border='1',id='mytable1')
headtr = table1 << tr(id='headline')
headtr << td('Head1') << td('Head2')
tr1 = table1 << tr(id='line1')
tr1 << td('r1,c1') <<td('r1,c2')
tr2 = table1 << tr(id='line2')
tr2 << td('r2,c1') <<td('r2,c2')
page.printOut()