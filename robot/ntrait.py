from PIL import Image
import time
PARASITE = 0.65
TAILLE = 60
T = 40
TOLERANCE = (T,T,T)
ROUGE = (150,40,40)
VERT = (40,80,50)
BLEU = (5,40,90)
JAUNE = (170,140,40)
NOIR = (0,0,0)
FILE = "./samples/image4.png"
TIME1 = 0
TIME2 = 0
TIME3 = 0
TIME4 = 0
START = 0
C = 2
#C= constante de diminution de resolution

class Analyse(object):
  
  #le tuple est code tel que (jaune, vert , rouge , bleu, aucun)  

  def __init__(self, image, taille):
    self.image = image
    width , height = image.size
    self.lar = (width)//C
    self.hau = (height - taille )//C
    self.tab = [[(0,0,0,0,0) for x in range(width//C)] for y in range(self.hau)] 
    self.tabs = [[(0,0,0,0,0) for x in range(width//C)] for y in range(self.hau)] 
    self.tabp = [[(0,0,0,0,0) for x in range(width//C)] for y in range(height//C)] 
    self.taille = taille //C

  def addtuple(self,x, y, signe = 1):
    z = []
    for i in range(len(x)):
        z.append(x[i]+(y[i]*signe))
    return tuple(z)
   

  def compris_tuple(self,t1,t2,signe):
    #compare deux tuple t1 et t2, si signe = 1 alors renvoie true si t1 plus grand que t2, false sinon
    #si signe = -1 renvoie au contraire true si t1 est plus petit que t2, false sinon
    for i in range(0,len(t1)):
      if(t1[i]*signe<t2[i]*signe):
        return False
    return True

  def compris_couleur(self, pixel, couleur, toler):
    #Cette fonction verifie si la couleur d'un pixel est compris
    #dans la limite de toler

    positive_difference = self.addtuple(couleur , toler)
    negative_difference = self.addtuple(couleur , toler,signe=-1)
    if((self.compris_tuple(pixel,positive_difference,-1)) and (self.compris_tuple(pixel,negative_difference,1))):
      return True
    
    return False
  
  def tuple_couleur(self, pixel):

    if(self.compris_couleur(pixel,VERT,TOLERANCE)):
      return (0,1,0,0,0)

    elif(self.compris_couleur(pixel,ROUGE,TOLERANCE)):
      return (0,0,1,0,0)

    elif(self.compris_couleur(pixel,BLEU,TOLERANCE)):
      return (0,0,0,1,0)

    elif(self.compris_couleur(pixel,JAUNE,TOLERANCE)):
      return (1,0,0,0,0)
     
    else:
      return (0,0,0,0,1)
 
  def definir_sous(self, x):

    tuple_couleur = (0,0,0,0,0)
    for i in range(0,self.taille):
      tuple_couleur = self.addtuple(self.tabp[i][x],tuple_couleur)
    self.tabs[0][x] = tuple_couleur;


    for j in range(1,self.hau):
      tuple_couleur = self.addtuple(tuple_couleur, self.tabp[j][x], signe = -1)
      tuple_couleur = self.addtuple(self.tabp[j+self.taille][x],tuple_couleur)
      self.tabs[j][x] = tuple_couleur
  
  def somme_ligne(self,x):
    s = (0,0,0,0,0)
    for i in range(0,self.taille):
      s = self.addtuple(s,self.tabs[x][i])

    self.tab[x][0] = s

    for j in range(1,self.lar-self.taille):
      s = self.addtuple(s,self.tabs[x][j-1],signe=-1)
      s = self.addtuple(s,self.tabs[x][j+self.taille-1])
      self.tab[x][j] = s
      
    

  def definir(self):
    global TIME1
    global TIME2
    global TIME3
    global START
   
    TIME1 = time.time() - START
    for k in range(0,self.lar):
      for l in range(0,self.hau+self.taille):
        self.tabp[l][k] = self.tuple_couleur(self.image.getpixel((k*2,l*2)))

    
    TIME2 = time.time() - START

    for i in range(0,self.lar):
      self.definir_sous(i)

    TIME3 = time.time() - START    

    for j in range(0,self.hau):
      self.somme_ligne(j)

  
  def sous_calcul(self,x,y):

    j = (self.tab[y][x])[0]
    v = (self.tab[y][x])[1]
    r = (self.tab[y][x])[2]
    b = (self.tab[y][x])[3]
    autre = (self.tab[y][x])[4]
    
    
    maximum = max(j,v,r,b)
    minimum = min(j,v,r,b)
    interval = maximum-minimum
    return interval , autre
  
  def calcul(self, parasite_ratio):

    minimum = self.taille*self.taille
    parasite = minimum*parasite_ratio 
    self.definir()
    x = y = -1
    indice_i = 0
    for i in range(0,self.lar-self.taille):
      for j in range(0,self.hau):        
        m , autre = self.sous_calcul(i,j)

        if((m<minimum) and (autre<parasite)):
          minimum = m
          x  = j
          y = i


    width , height = self.image.size
    
    return x*C , y*C

START = time.time()

image = Image.open(FILE).convert("RGB")
analyse = Analyse(image, TAILLE)
x, y = analyse.calcul(PARASITE) 
print("x = ",x,"y = ",y,"   \n")

print ("TIME1 = " , TIME1)
print ("TIME2 = " , TIME2)
print ("TIME3 = " , TIME3)

print ("duree = " , (time.time()-START))
