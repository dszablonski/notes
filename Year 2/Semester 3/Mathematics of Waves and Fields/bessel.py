import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

plt.matplotlib.rc('text', usetex = True)
plt.matplotlib.rc('grid', linestyle = 'dotted')
plt.matplotlib.rc('figure', figsize = (6.4,4.8)) # (width,height) inches
x = np.linspace(0, 15, 500)

for v in range(0, 6):
    plt.plot(x, sp.jv(v, x))

plt.xlim((0, 15))
plt.ylim((-0.5, 1.1))
plt.legend(('${J}_0(x)$', '${J}_1(x)$', '${J}_2(x)$','${J}_3(x)$', '${J}_4(x)$', '${J}_5(x)$'), loc = 0)
plt.xlabel('$x$')
plt.ylabel('${J}_n(x)$')

plt.grid(True)
plt.tight_layout()

plt.savefig('example-04-fig.pdf')
# save the data for later use by pgfplots
np.savetxt('example-04.txt',list(zip(x,sp.jv(0,x),sp.jv(1,x),sp.jv(2,x),sp.jv(3,x),sp.jv(4,x),sp.jv(5,x))),fmt="% .10e")