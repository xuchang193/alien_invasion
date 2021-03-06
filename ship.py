import pygame

class Ship():

    def __init__(self,ai_settings,screen):#初始化飞船并设置其初始位置
        self.screen=screen
        self.ai_settings=ai_settings

        #加载飞船图像并且获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #确定将每艘新船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        #在飞船属性center中存储小数值
        self.center=float(self.rect.centerx)

        #移动标志
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志调整飞船的位置,并且限制在屏幕范围内"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor

        #根据self.cener更新rext对象
        self.rect.centerx=self.center

    def blitme(self):
        """在指定位置绘制新船"""
        self.screen.blit(self.image,self.rect)
