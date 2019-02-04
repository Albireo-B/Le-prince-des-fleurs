import pygame

corpsA=100
corpsB=10
distance=50

def forceAttractionCorps (corps1,corps2,distance):
    g = 6.67408*pow(10,-11)
    return g*((corps1*corps2)/distance)

print(forceAttractionCorps(corpsA,corpsB,distance))
