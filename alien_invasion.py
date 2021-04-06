
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Ship实例化
    ship=Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人编组
    aliens=Group()

    #创建外星人群
    gf.creat_fleet(ai_settings,screen,aliens)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)#这里为什么传入了4个参数？
        ship.update()
        gf.update_bullets(bullets)

        """更新屏幕上的图像，并切换到新屏幕"""
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()