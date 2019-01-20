#开始部分
import pygame
import random
import os

#pygame的开始
pygame.init()

#定义各自的宽度，行列方向的格子数量
CRID_WIDTH=20
CRID_NUM_WIDTH=15
CRID_NUM_HEIGHT=25
#根据格子数量计算可视框的宽度和高度
WIDTH,HEIGHT = CRID_WIDTH * CRID_NUM_WIDTH*,CRID_WIDTH * GRID_NUM_HEIGHT
SIDE_WIDTH=200
SCREEN_WIDTH=WIDTH + SIDE_WIDTH
#定义常用颜色
WHITE=(0xff,0xff,0xff)
BLACK=(0,0,0)
LINE_COLOR=(0x33,0x33,0x33)
#定义颜色矩阵，主要用于生成不用颜色的俄罗斯方块
CUBE_COLORS=[
    (0xcc, 0x99, 0x99), (0xff, 0xff, 0x99), (0x66, 0x66, 0x99),
    (0x99, 0x00, 0x66), (0xff, 0xcc, 0x00), (0xcc, 0x00, 0x33),
    (0xff, 0x00, 0x33), (0x00, 0x66, 0x99), (0xff, 0xff, 0x33),
    (0x99, 0x00, 0x33), (0xcc, 0xff, 0x66), (0xff, 0x99, 0x00)

]

#设置可视窗的宽高
screen = pygame.display.set_mode(SCREEN_WIDTH,HEIGHT)
#设置标题
pygame.display.set_caption("俄罗斯方块")
#根据帧数限制游戏运行速度
clock = pygame.time.Clock()
#帧数
FPS = 30
#分数和等级
score = 0
level = 1
#储存每个格子状态，若未填充格子则为None，已填充的话会变成该方块的颜色值
screen_color_matrix = [[None] * CRID_NUM_WIDTH for i in range(CRID_NUM_HEIGHT)]
#设置游戏的根目录为当前文件夹
base_folder = os.path.dirname(__file__)
#封装一个函数方便显示文字
def show_text(surf,text,size,x,y,color=WHITE)
    font_name = os.path.join(base_folder,"font/font.ttc")
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)

#方块类
class CubeShape(object):
    #储存方块的名字的列表
    SHAPES=['I','J','L','O','S','T','Z']
    I = [[(0,-1),(0,0),(0,1),(0,2)],[(-1,0),(0,0),(1,0),(2,0)]]
    J = [[(-2, 0), (-1, 0), (0, 0), (0, -1)],
         [(-1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, 1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (1, 0)]]
    L = [[(-2, 0), (-1, 0), (0, 0), (0, 1)],
         [(1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, -1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (-1, 0)]]
    O = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    S = [[(-1, 0), (0, 0), (0, 1), (1, 1)],
         [(1, -1), (1, 0), (0, 0), (0, 1)]]
    T = [[(0, -1), (0, 0), (0, 1), (-1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, 1)],
         [(0, -1), (0, 0), (0, 1), (1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, -1)]]
    Z = [[(0, -1), (0, 0), (1, 0), (1, 1)],
         [(-1, 0), (0, 0), (0, -1), (1, -1)]]
    # 储存方块各种形态（各种变形）的对象
    SHAPES_WITH_DIR = {
        'I': I, 'J': J, 'L': L, 'O': O, 'S': S, 'T': T, 'Z': Z
    }

#初始化函数，设置形状（shape），中心点（center）,形态（dir）,颜色（color）为类的自身属性
def __init__(self):
    self.shape=self.SHAPES[random.randint(0,len(self.SHAPES)-1)]
    #骨牌所在的行列
    self.center=(2,CRID_NUM_WIDTH // 2)
    self.dir = random.randint(0,len(self.SHAPES_WITH_DIR[self.shape])-1)
    self.color=CUBE_COLORS[random.randint(0,len(CUBE_COLORS)-1)]



