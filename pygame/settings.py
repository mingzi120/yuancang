# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:33:36 2020

@author: 张钧铭
"""

#settings.py

class Settings():
    """存储 外星人入侵 的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (6,35,102)
        
        
        #子弹设置
        
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = 237,136,73
        self.bullets_allowed = 3
        
        #外星人设置
        
        self.fleet_drop_speed = 10
        self.score_scale = 1.5
        
        #飞船设置
        
        self.ship_limit = 3
        
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 1
       
        #fleet_direction为1表示右移动，-1为向左移动
        self.fleet_direction = 1
        
        #计分
        self.alien_points = 50
        
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points*self.score_scale)
       