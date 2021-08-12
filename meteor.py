'''
Antes de tudo é necessário instalar o opencv para realizar as operações necessárias

pip install opencv-python
'''

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
   


print(f'Número de estrelas: {stars}')
print(f'Número de meteoros: {meteors}')
print(f'Meteoros que caem na água: {meteors_water}')
