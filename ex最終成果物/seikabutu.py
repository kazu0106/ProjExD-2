import pygame as pg
import sys
from random import randint
import random
import os
from pygame.locals import *
import time
import tkinter as tk

WIDTH = 1600
HEIGHT = 900
BLOCK_LOCAT1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

BLOCK_LOCAT2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



class Screen:    #画面のクラス

    def __init__(self,title,wh,file):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:     #プレイヤーのクラス
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,file,size,location):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.rct.center = location

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, self.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Block:    #ブロック追加
    def __init__(self):
        self.sfc = pg.image.load("fig/block.jpg")
        self.sfc = pg.transform.scale(self.sfc,(50,50))
        self.rct = self.sfc.get_rect()
        

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,x,y,scr:Screen):
        self.rct.center = 25+50*x, 25+50*y
        self.blit(scr)


class Bomb:     #爆弾のクラス

    def __init__(self,color,radius,vxy,scr:Screen):
        self.sfc = pg.Surface((radius*20, radius*20)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius*10, radius*10), radius*10) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr:Screen,bcr:Block):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        y, t = check(self.rct, bcr.rct)
        self.vx *= yoko*y
        self.vy *= tate*t
        self.blit(scr)


class Change:  #新クラス　キー入力

    def __init__(self):
        self.num = random.randint(0,9) #こうかとん画像　ランダム
        self.size = random.randint(2,8)  #爆弾サイズ　ランダム
        self.file_lst = ["海.jpg","砂漠.jpg","チェス.jpg","金魚.jpg","森.jpg"]  #背景画像ランダム　　#修正 #17
        
    def kimg(self):
        file = f"fig/{self.num}.png"  #追加機能　画像ランダム選出
        main(kokaton=file)

    def bomb(self):    #追加機能　爆弾サイズ変更
        main(size=self.size)

    def bgimg(self):    #追加機能　背景画像変更
        bg_file = f"fig/{random.choice(self.file_lst)}"
        main(bg=bg_file) 

    def ranbro(self):
        ls_bro = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        for i in range(18):
            for j in range(32):
                ls_bro[i].append(random.randint(0,1))
        main(ls = ls_bro,mana = 1)


def check_bound(obj_rct, scr_rct):     #移動
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def check(obj_rct,scr_rct):   #ブロックと爆弾衝突の判定
    yoko, tate = 1, 1
    if obj_rct.left+20 == scr_rct.left or scr_rct.right == obj_rct.right+1550:
        yoko = -1
    if obj_rct.top+20 == scr_rct.top or scr_rct.bottom == obj_rct.bottom+850:   #修正　担当：C0B21171
        tate = -1
    return yoko,tate

main_dir = os.path.split(os.path.abspath(__file__))[0]
def load_sound(file):    #音声の追加
    """because pygame can be be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def main(kokaton="fig/6.png",size=5,bg="fig/海.jpg",count = 0,ls = [],mana = 0):
    scr = Screen("逃げろ！こうかとん",(WIDTH, HEIGHT),bg)
    kkt = Bird(kokaton,2.0,(900, 400))    
    bkd = Bomb((255, 0, 0),size,(+1,+1),scr)
    chg = Change()
    bcr = Block()
    
    boom_sound = load_sound("boom.wav")   #被弾時の効果音
    if pg.mixer:  #BGMの追加
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    clock = pg.time.Clock()

    bad = 0
    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F1:  #リセットボタン ゲームを初期化する
                main(count=8000)
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F2:    #追加機能　画像ランダム選出
                chg.kimg()
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F3: #追加機能　爆弾サイズ変更
                chg.bomb()
                return
            if event.type == pg.KEYDOWN and event.key ==pg.K_F4: #追加機能　背景画像変更
                chg.bgimg()  
                return     
            if event.type == pg.KEYDOWN and event.key ==pg.K_F5:
                chg.ranbro()
                return

        kkt.update(scr)
        bkd.update(scr,bcr)

        count += 1


        if count >= 4000:
            bkd.update(scr,bcr)
        if count >= 8000:
            bkd.update(scr,bcr)


        if count >= 2000:
            for i,bl in enumerate(BLOCK_LOCAT1):
                for j in range(32):   #ブロック追加
                    if bl[j] == 1:
                            bcr.update(j,i,scr)
                            
        if count >= 6000:
            for i,bl in enumerate(BLOCK_LOCAT2):
                for j in range(32):   #ブロック追加
                    if bl[j] == 1:
                            bcr.update(j,i,scr)

        if mana == 1:
            for i,bl in enumerate(ls):
                    for j in range(32):   #ブロック追加
                        if bl[j] == 1:
                                bcr.update(j,i,scr)
        
        if count >= 10000:
            root = tk.Tk()
            root.title("game")
            root.geometry("1000x400")
            root.resizable(True,True)
            if bad == 0:
                label = tk.Label(root,text="Clear",font=("",50))
            else:
                label = tk.Label(root,text=f"you lose",font=("",50))
            label.pack()
            root.mainloop()
            return

        if kkt.rct.colliderect(bkd.rct): 
            boom_sound.play()   #被弾時に効果音
            fonto = pg.font.Font(None,400)
            txt = fonto.render("Explosion",True,(0,0,0))
            scr.sfc.blit(txt,(100,200))
            bad += 1
            
        pg.display.update() 
        clock.tick(1000)

    

if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
