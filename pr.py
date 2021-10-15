import matplotlib.pyplot as plt
import math

tt = 0.0001
V0 = 662
g = 9.8
p0 = 0.029
k = 0.05
fg = 55
f = fg/57.3
VX = V0*math.cos(f)
VY = V0*math.sin(f)
x, y = 0, 60
m = 6.3
ks = k*p0/(2*m)
mass_x, mass_y = [0], [60]
for i in range(5000000):
    VX -= ks*abs(VX)*VX*tt
    VY -= (g + ks*abs(VY)*VY)*tt
    x += VX*tt
    y += VY*tt
    if y <= 0:
        break
    else:
        mass_x.append(x)
        mass_y.append(y)
print(mass_x[-1], mass_y[-1], tt*i-1)
plt.plot(mass_x, mass_y)
plt.plot([0, mass_x[-1]], [0, 0])
plt.show()

