# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:39:19 2020

@author: 张钧铭
"""

#sun.py

import pygame

class Sun():
    def __init__(self,ai_settings,screen):
        
        self.ai_settings=ai_settings
        #加载太阳图像并获取其外接矩形
        self.image = pygame.image.load('images/sun.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕顶部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)