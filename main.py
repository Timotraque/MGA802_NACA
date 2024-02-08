import matplotlib.pyplot as plt
import numpy as np

# Créer l'épaisseur du profil
t = int(input("Entrez le numéro de profil NACA00"))
t = t/100

# Créer une liste contenant les valeurs de 0 à la corde maximale
corde = int(input("Entrez la corde du profil en m : "))
nb_points = int(input("Entrez le nombre de points le long de la corde : "))
c = np.linspace(0, corde, nb_points)

choix = int(input("Distributions de points : \n1 - linéaire\n2 - non linéaire\nChoix : "))
if choix == 1 :
    x_c = np.linspace(0,corde,nb_points)
else :
    # Transformée de Glauert
    theta = np.linspace(0, np.pi, nb_points)
    x_c = 0.5 * (1 - np.cos(theta))

# Equation de la courbe
y_t = 5 * t * (0.2969 * np.sqrt(x_c) - 0.126 * x_c - 0.3516 * np.power(x_c, 2) + 0.2843 * np.power(x_c,3) - 0.1036 * np.power(x_c,4))

y_up = y_t * corde
y_down = -y_t * corde


# Affichage de la courbe
plt.rcParams['font.size'] = 14
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100
plt.plot(c, y_up*corde, label='extrados')
plt.plot(c, y_down*corde, label='intrados')
plt.xlabel('corde [m]')
plt.ylabel('épaisseur [m]')
plt.legend()
plt.grid()
plt.title('Profil NACA00' +str(int(t*100)))
plt.xlim(-0.1,corde+0.1)
plt.ylim(-0.3*corde,0.3*corde)      # Contraint l'affichage pour garder les proportions
plt.show()
