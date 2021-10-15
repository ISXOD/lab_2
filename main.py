import matplotlib.pyplot as plt
import math
V0, a_gr, h = 200, 46, 70
g, rad = 9.8, 57.3
a = a_gr/rad
t_end = (V0*math.sin(a) + math.sqrt(V0*V0*math.sin(a)*math.sin(a) + 2*g*h))/g
print(t_end)
S = V0*math.cos(a)*t_end
print(S)
y_mass = []
x_mass = []
j = int(t_end//0.0005)
for i in range(j +1):
    t = i/2000
    x = V0*math.cos(a)*t
    y = math.tan(a)*x - g*x*x/(2*V0*V0*math.cos(a)*math.cos(a))
    y_mass.append(y)
    x_mass.append(x)
    #print(str(i) + ')', t, round(x, 3), round(y, 3))

plt.plot(x_mass, y_mass)
plt.plot([0, S], [-70, -70])
plt.plot([0, S], [0, 0])
plt.show()