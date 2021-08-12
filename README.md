# Meteor Challenge

antes de tudo é necessário instalar o opencv para realizar as operações necessárias

`pip install opencv-python`

Neste desafio utilizei o python com a biblioteca OpenCV para analisar a imagem.

![image](meteor.png)

O que eu imaginei para a solução foi, como a imagem é uma matriz com 3 camadas, sendo elas, Red, Green e Blue, ou seja cada coordenada ou pixel, é um conjunto desses 3 elementos. Por exemplo, usando o OpenCV é possível descobrir o código em RGB dele.




```python
import cv2
 
image = cv2.imread('meteor.png')
print(image[0, 0])
```

executando este código é possível ver que o código RGB do primeiro pixel da imagem é [189 119   2].
Diante disso imaginei uma solução que percorre a matriz da imagem e testando a cor de cada pixel, para fazer um somatório de estrelas e meteoros. 

```python
import cv2
 
image = cv2.imread('meteor.png')
 
stars = meteors = 0
 
white = [255, 255, 255]
red = [0, 0, 255]
 
 
for y in range(0, image.shape[0]): 
    for x in range(0, image.shape[1]):       
        
        if (list(image[y, x]) == white):
            stars += 1
        elif (list(image[y, x]) == red):
            meteors += 1
 
print(f'Estrelas: {stars}')
print(f'Meteoros: {meteors}')
```

Assim criei 2 variáveis, para guardar a quantidade de estrelas e meteoros, 2 para guarda uma lista com os códigos RGB da cor branca (estrela e vermelha (meteoro), depois fiz um for duplo para percorrer ponto a ponto da imagem e testando em cada ponto se a cor era branca ou vermelha e somando em cada contador, caso fosse.
Para solucionar se o meteoro iria cair na água, oque imaginei foi, como ele deve cair em linha reta, é só analisar se em cada coluna mais abaixo possui água.

```python
import cv2
 
 
def search(list, element):
    for i in list:
        if i[1] == element:
            return True
            
    return False
 
image = cv2.imread('meteor.png')
 
print('largura em pixels: ', image.shape[1])
print('altura em pixels: ', image.shape[0])
print('quantidade de canais: ', image.shape[2])
 
stars = meteors = meteors_water  = 0
 
aux = 0
water = list()
 
white = [255, 255, 255]
red = [0, 0, 255]
blue = [255, 0, 0]
 
for y in range(0, image.shape[0]): 
    for x in range(0, image.shape[1]): 
        
        if (list(image[y, x]) == blue):
            water.append([y, x])
            a = 10
    
    if  aux == 10:
        break
 
for y in range(0, image.shape[0]): 
    for x in range(0, image.shape[1]):       
        
        if (list(image[y, x]) == white):
            stars += 1
        elif (list(image[y, x]) == red):
            meteors += 1
            if (search(water, x)):
                meteors_water += 1
  
print(f'Meteoros que caem na água: {meteors_water}')
```

Assim fiz um for duplo para guardar as posições onde está a água, mas como só é necessário a altura 512, percorrendo a linha inteira (que é altura onde começa a agua que encontrei em meus testes), depois de encontrar essas posições foi necessário outro for duplo para testar se em cada ponto vermelho na mesma coluna mais abaixo tem algum ponto azul, para isso criei uma função busca na matriz que guarda informações de onde tem água se possui o ponto na mesma coluna.
Depois de todos os testes foi possível ver que possuem:

Number of Stars | Number of Meteors | Meteors falling on the Water
:---: | :---: | :---:
315 | 328 | 105
