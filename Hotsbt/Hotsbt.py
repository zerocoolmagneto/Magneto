from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import time
import _thread
from os import listdir
from os.path import isfile, join
import os



dt1 = 0.1
dt2 = 1
ft1 = .02
ft2 = .1
epoch_time = int(time.time())
debugging = 1
play_area_y = (120,750)
game_screen = None

tab_portrait_directory = os.path.dirname(os.path.realpath(__file__)) + '\\tab_portrait\\'
tab_portraits = [f for f in listdir(tab_portrait_directory) if isfile(join(tab_portrait_directory, f))]

def click_screen(pic, confid, offsetx, offsety):
    screen = pyautogui.locateOnScreen(pic, confidence=confid)
    if screen != None:
        win32api.SetCursorPos((screen.left+offsetx, screen.top+offsety))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        return True
def click_region(pic, confid, x, y, width, height, offsetx, offsety):
    region = pyautogui.locateOnScreen(pic, region=(x,y,width,height), confidence=confid)
    if region != None:
        win32api.SetCursorPos((region.left+offsetx, region.top+offsety))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        return True
def check_region(pic, confid, x, y, width, height, offsetx, offsety):
    region = pyautogui.locateOnScreen(pic, region=(x,y,width,height), confidence=confid)
    if region != None:
        return True
def debug(message):
    if debugging == 1:
        print(message)
def move_cursor(x,y,t1,t2):
    time.sleep(random.uniform(t1,t2))
    win32api.SetCursorPos((x,y))
def click(x,y,t1,t2):
    time.sleep(random.uniform(t1,t2))
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def right_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def left_click(t1,t2):
    time.sleep(random.uniform(t1,t2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def talent_picker():
    newtalent = pyautogui.locateOnScreen('newtalent.png', region=(35,1000,160,1060), confidence=0.9)
    if newtalent != None:
        debug('newtalent Found!')
        talent_open = pyautogui.locateOnScreen('talent_open.png', region=(10,790,50,840), confidence=0.9)
        if talent_open == None:
            click(newtalent.left, newtalent.top,dt1,dt2)
        talent_fav = pyautogui.locateOnScreen('talent_fav.png', region=(0,400,100,800), confidence=0.9)
        if talent_fav != None:
            click(talent_fav.left, talent_fav.top,dt1,dt2)
   
def rotation():
    if aim(25, 50):
        pyautogui.hotkey('q')
        left_click(dt1,dt2)
    if aim(25, 50):
        pyautogui.hotkey('w')
        left_click(dt1,dt2)
    if aim(25, 50):
        pyautogui.hotkey('e')
        left_click(dt1,dt2)
    if aim(25, 50):
        pyautogui.hotkey('r')
        left_click(dt1,dt2)

def hit_key(key,t1,t2):
    time.sleep(random.uniform(t1,t2))
    pyautogui.hotkey(key)
def attack_core(left, top):
    debug('redcore Found!')
    move_cursor(left+30, top+15,dt1,dt2)
    hit_key('a',dt1,dt2)
    hit_key(' ',dt1,dt2)
def hat():
    healthbar = pyautogui.locateOnScreen('healthbar.png', confidence=0.8)
    if healthbar != None:
        move_cursor(healthbar.left+75, healthbar.top+100,dt1,dt2)
        pyautogui.hotkey('q')
        #debug('healthbar found!')
def check_hotbar_ready(pic):
    hotbar = pyautogui.locateOnScreen(pic, region=(650,980,1919,1079), confidence=0.8)
    if hotbar != None:
        return True
def click_mini_map(pic, offsetx, offsety, confid, gscale):
    mini_map = pyautogui.locateOnScreen(pic, region=(1389,715,1919,1079), confidence=confid, grayscale=gscale)
    if mini_map != None:
        win32api.SetCursorPos((mini_map.left + offsetx, mini_map.top + offsety))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        return True
    else:
        return False
def attack_mini_map(pic, offsetx, offsety, confid, gscale):
    mini_map = pyautogui.locateOnScreen(pic, region=(1389,715,530,364), confidence=confid, grayscale=gscale)
    if mini_map != None:
        debug('Found Something to attack!')
        win32api.SetCursorPos((mini_map.left + offsetx, mini_map.top + offsety))
        pyautogui.hotkey('a')
        return True
    else:
        return False
def aim(offsetx, offsety):
    debug('Checking for Enemy!')
    time.sleep(random.uniform(0.05,0.1))
    enemy = pyautogui.locateOnScreen('enemy_health_bar.png', region=(500,150,1400,800), confidence=0.8)
    if enemy != None:
        debug('Enemy Found!')
        win32api.SetCursorPos((enemy.left + offsetx, enemy.top + offsety))
        return True
def check_gamemode():
    prim = pyautogui.locateOnScreen('prim.png', region=(40,870,175,920), confidence=0.9)
    if prim != None:
        debug('Portrait Found! Remaining in Gamemode 1')
        return 1
    else:
        if pyautogui.locateOnScreen('browse_all_heroes.png') != None:
            return 2
        else:
            return 0
def select_ban():
    #0,244,380,125 ban
    #0,366,466,125 ban 2
    #0,460,569,125 ban 3
    #1315,775 search
    #612,857 hero
    #715,820 hero2
    #800,820 hero3
    #915,820 hero4
    #950,975 lock in
    time.sleep(random.uniform(0.1,0.5))
    click(715,820)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(815,820)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(915,820)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
def select_hero():
    #time.sleep(random.uniform(0.1,0.5))
    click(612,857)
    #time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(715,820)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(815,820)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(915,820)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(950,975)
    time.sleep(random.uniform(0.1,0.5))
    click(1015,820)
    time.sleep(random.uniform(0.1,0.5))
    click(1150,975)
    time.sleep(random.uniform(0.1,0.5))
    click(1215,820)
    time.sleep(random.uniform(0.1,0.5))
    click(1350,975)
    time.sleep(random.uniform(0.1,0.5))
    click(1415,820)
    time.sleep(random.uniform(0.1,0.5))
    click(1550,975)
def check_hero():
    time.sleep(1)
    pyautogui.keyDown('f1')
    for tab_portrait in tab_portraits:
        debug('checking '+tab_portrait)
        full_tab_portrait = 'tab_portrait\\' + tab_portrait
        if pyautogui.locateOnScreen(full_tab_portrait, region=(390,240,120,55), confidence=0.8) != None:
            hero = tab_portrait.replace('tab_','').replace('.png','')
            debug('Hero Found')
            debug(hero)
            pyautogui.keyUp('f1')
            return hero
        else:
            debug('could not find '+tab_portrait+' in '+full_tab_portrait)
    debug('setting AI to default')
    pyautogui.keyUp('f1')
    return 'default'

class check_game():
    def __init__(self):
        self.blue_side = None
        self.red_core = pyautogui.locateOnScreen('redcore.png', region=(1389,715,1919,1079), confidence=0.8)
        self.blue_core = pyautogui.locateOnScreen('blue_core.png', region=(1389,715,1919,1079), confidence=0.8)
        if self.red_core != None: 
            if self.red_core[0] > 1700:
                debug('Detected Blue side is on Left')
                self.blue_side = 'left'
            else:
                self.blue_side = 'right'
                debug('Detected Blue side is on Right')
    def blue_hero_location(self):
        return pyautogui.locateAllOnScreen('ally_health_bar.png', confidence=0.8)
    def red_hero_location(self):
        return pyautogui.locateAllOnScreen('enemy_health_bar.png', confidence=0.8)
    def red_minion_location(self):
        return pyautogui.locateAllOnScreen('enemy_minion_bar.png', confidence=0.8)
    def red_structure_location(self):
        return pyautogui.locateAllOnScreen('enemy_structure_bar.png', confidence=0.8)
        
    def parsed_blue_hero_locations(self):
        #debug('parsed blue hero')
        return self.parse_locations(self.blue_hero_location())
    def parsed_red_hero_locations(self): 
        #debug('parsed red hero')
        return self.parse_locations(self.red_hero_location())
    def parsed_red_minion_locations(self): 
        return self.parse_locations(self.red_minion_location())
    def parsed_red_structure_locations(self): 
        return self.parse_locations(self.red_structure_location())
        
    def closest_red(self): 
        #debug('closest_red')
        return self.find_closest(self.parsed_red_hero_locations(), ((960,450)))
    def opposite_closest_red(self): 
        #debug('opposite_closest_red')
        return self.find_opposite_closest(self.closest_red())
   
   
    def read_ally_healthbars(self):
        x=0
        health_bar = []
        hero_locations = self.parsed_blue_hero_locations()
     
        if hero_locations == None:
            return None
        else:
            for xy in hero_locations:
                health = 0
                health_screen = pyautogui.screenshot(region=(xy[0],xy[1],128,6))
                for x in range(0,127,1):                  
                    r,g,b = health_screen.getpixel((x,5))
                    if b > 110:
                        health = health + 1
                    if r == 0 and g == 0 and b == 0:
                        health = health + 1

                health_bar.append((health, xy[0], xy[1])) 
                debug(('health_bar is ', health_bar))
            return health_bar
            

    def find_lowest_ally_healthbar(self):
        lowest_health = ((200, 0, 0))
        ally_healthbars = self.read_ally_healthbars()
        if ally_healthbars == None:
            return None
        else:
            for healthxy in ally_healthbars:
                if lowest_health[0] > healthxy[0]:
                    lowest_health = healthxy
            return lowest_health[1], lowest_health[2], lowest_health[0]

    def find_closest(self, location, location2):
        
        #debug('finding closest')
        closest = (0,0)
        if not location:
            return None
        else:
            for xy in location:
                if (abs(closest[0] - 960) + abs(closest[1] - 450)) > (abs(xy[0] - 960) + abs(xy[1] - 450)):
                    return xy

    def find_opposite_closest(self, xy):
        #debug('finding opposite_closest')
        if not xy:
            return None
        else:
            return ((960-xy[0])+960,(450-xy[1]+450))


    def read_green_healthbar(self):
        #debug('reading green healthbar')
        
        screen = pyautogui.screenshot(region=(0,0,1919,1079))
        
        health = 0
        x=0
        for x in range(0,200,2):
            r,g,b = screen.getpixel((x+206,1009))
            if g > 150 and b < 110:
                health = health + 1
        return health
        debug(hero_object_1.health)
    def parse_locations(self, locations):
        #debug('parsing locations')
        parsed_locations = []
        if not locations:
            return None
        else:
            for location in locations:
                if locations != None:
                    parsed_locations.append((location.left, location.top))
                    return parsed_locations



class hero_object:
    def __init__(self,
        name='', 
        type='', 
        q_target='',
        q_type='',
        w_target='',
        w_type='',
        e_target='',
        e_type='',
        r_target='',
        r_type='',
        d_target='',
        d_type=''):
        self.name = name
        self.type = type
        self.health = 0
        self.q_target = q_target
        self.q_type = q_type
        self.w_target = w_target
        self.w_type = w_type
        self.e_target = e_target
        self.e_type = e_type
        self.r_target = r_target
        self.r_type = r_type
        self.d_target = d_target
        self.d_type = d_type
        self.stick_team = 'on'
        self.heal_others = 'on'
        self.stay_alive = 'on'
        self.attack = 'on'
        self.hearth = 'off'
        self.wait = 'off'
        self.mount = 'off'
        self.found_target = None
        self.q_pic = None
        self.w_pic = None
        self.e_pic = None
        self.r_pic = None
        self.d_pic = None
        self.heal_other_threshold = 99
        self.find_ally_clock = clock_timer(15)
        if pyautogui.locateOnScreen('hotbar\\mount_hotbar.png', region=(660,1020,120,55)) != None:
            debug('Found Non Standard Mount')
            self.non_standard_mount = True
        else:
            debug('Found Standard Mount')
            self.non_standard_mount = False
    def prioritize(self):
        self.stick_team = 'off'
        self.heal_others = 'off'
        self.stay_alive = 'off'
        self.attack = 'off'
        self.hearth = 'off'
        self.mount = 'off'
        self.stick_screen_team = 'off'
        if self.type == 'healer':
            if self.health >= 66:
                #debug('reprioritizing Healing others and attacking
                
                self.stick_team = 'on'
                self.stick_screen_team = 'on'
                self.heal_others = 'on'
                self.attack = 'on'
            if self.health < 66:
                #debug('reprioritizing just trying to stay alive!')
                self.stick_screen_team = 'on'
                
                self.stick_team = 'on'
                #self.stay_alive = 'on'
            if self.health < 33:
                #debug('reprioritizing trying to stay alive and hearth back')
                self.stay_alive = 'on'
                self.hearth = 'on'
            return
        if self.type == 'default':
            if self.health >= 66:
                #debug('reprioritizing Healing others and attacking
                
                self.stick_team = 'on'
                self.stick_screen_team = 'on'
                self.attack = 'on'
            if self.health < 66:
                #debug('reprioritizing just trying to stay alive!')
                self.stick_screen_team = 'on'
                
                self.stick_team = 'on'
                #self.stay_alive = 'on'
            if self.health < 33:
                #debug('reprioritizing trying to stay alive and hearth back')
                self.stay_alive = 'on'
                self.hearth = 'on'
            return


    def debug_prioritize(self):
        self.stick_team = 'on'
        self.heal_others = 'off'
        self.stay_alive = 'off'
        self.attack = 'off'
        self.hearth = 'off'
        self.mount = 'off'
        self.stick_screen_team = 'off'
    def run_ai(self):
        self.health = game_screen.read_green_healthbar()
        debug(('hero health = ', self.health))
        self.prioritize()
        debug('Priorities:')
        debug(('stick team', self.stick_team))
        debug(('heal_others', self.heal_others))
        debug(('stay_alive', self.stay_alive))
        debug(('attack', self.attack))
        debug(('hearth', self.hearth))
        debug(('mount', self.mount))
        #self.debug_prioritize()
        self.run_action()
    def run_action(self):
        self.target=''
        if self.stick_team == 'on':   
            if game_screen.find_lowest_ally_healthbar() == None:
                #if self.find_ally_clock.check_timer():
                self.action_find_team()
        if self.stick_screen_team == 'on':
            self.action_stick_team_screen()
        if self.stay_alive == 'on':
            debug("running staying alive")
            self.action_self_heal()
            self.action_run_away()
        if self.hearth == 'on':
            self.action_hearth()
        if self.attack == 'on':
            debug('Attack')
            self.action_attack()
        if self.heal_others == 'on':
            debug('Trying to Heal Team')
            self.action_heal_others()
        if self.mount == 'on':
            debug('Mounting')
            self.action_mount()
    def action_heal_others(self):

        lowest = game_screen.find_lowest_ally_healthbar()
        debug('Looking Someone to Heal!')
        if lowest != None:
            if lowest[2] < self.heal_other_threshold:
                debug('Found Someone To Heal!')
                self.target = 'allies'
                if self.q_type == 'heal':
                    debug('Healing with Q')
                    if self.q_target == 'unit':
                        self.action_hotbar('q','allies')
                    if self.q_target == 'allies none':
                        self.action_hotbar('q','allies none') #no reason not to just pass variable q_target >.<
                if self.w_type == 'heal':
                    if self.w_target == 'unit':
                        self.action_hotbar('w','allies')
                    if self.w_target == 'allies none':
                        self.action_hotbar('w','allies none')
                if self.e_type == 'heal':
                    if self.e_target == 'unit':
                        self.action_hotbar('e','allies')
                    if self.e_target == 'allies none':
                        self.action_hotbar('e','allies none')
                if self.r_type == 'heal':
                    if self.r_target == 'unit':
                        self.action_hotbar('r','allies')
                    if self.r_target == 'allies none':
                        self.action_hotbar('r','allies none')
                if self.d_type == 'heal':
                    if self.d_target == 'unit':
                        self.action_hotbar('d','allies')
                    if self.d_target == 'allies none':
                        self.action_hotbar('d','allies none')

    def action_attack(self):
        location = game_screen.closest_red()
        self.target = 'enemy'
        
        if location != None:
            _thread.start_new_thread(right_click(location[0]+10, location[1]+50))
        if self.q_type == 'attack':
            self.action_hotbar('q','enemy')
        if self.w_type == 'attack':
            self.action_hotbar('w','enemy')
        if self.e_type == 'attack':
            self.action_hotbar('e','enemy')
        if self.r_type == 'attack':
            self.action_hotbar('r','enemy')
        if self.d_type == 'attack':
            self.action_hotbar('d','enemy')
        #self.step_away()
    def step_away(self):
        location = game_screen.opposite_closest_red()
        if location != None:
            if location[0] > 1260:
                location[0] = 1260
            if location[0] > 750:
                location[0] = 750
            if location[0] > 660:
                location[0] = 660
            if location[0] > 150:
                location[0] = 150
            if location != None:
                _thread.start_new_thread(right_click,(location[0]+10,location[1]+50))
    def action_run_away(self):
        location = None
        while game_screen.parsed_red_hero_locations() != None:
           if game_screen.blue_side == 'right':     
                location = ((random.randrange(1700,1800)), random.randrange(400,450))
           if game_screen.blue_side == 'left':
                location = ((random.randrange(100,200)), random.randrange(400,450))
           if location != None:
                _thread.start_new_thread(right_click,(location[0]+10,location[1]+50))
    def action_self_heal(self):
        if self.type == 'healer':
            self.target = 'self'
        else:
            debug('Im not a healer My type is')
            debug(self.type)

        if self.q_type == 'heal':
            if self.q_target == 'unit':
                self.action_hotbar('q','self')
    def action_stick_team_screen(self):
        ally_locations = game_screen.blue_hero_location()
        if ally_locations != None:
            location = None
            for ally_location in ally_locations:
                location = ally_location
            if location != None:
                _thread.start_new_thread(right_click,(location[0], location[1]))
        else:
            debug('no allies')
            if game_screen.blue_side == 'left':     
                location = ((random.randrange(1700,1800)), random.randrange(400,450))
            if game_screen.blue_side == 'right':
                location = ((random.randrange(100,200)), random.randrange(400,450))
            if location != None:
                _thread.start_new_thread(right_click,(location[0]+10,location[1]+50))
        
    def action_find_team(self):
        
        ally_location = self.find_ally_mini_map()
        self.action_mount()

        #while ally_location == None:
        #    ally_location = self.find_ally_mini_map()
        if ally_location != None:
            win32api.SetCursorPos((ally_location[0]+15,ally_location[1]+15))
            pyautogui.hotkey('a')
            self.find_ally_clock.start_timer()
            #attack_mini_map('redcore.png', 15, 15, 0.8, False)
    def action_hearth(self):
        _thread.start_new_thread(hit_key,('b',dt1,dt2))
        time.sleep(random.uniform(6.1,6.3))

    def action_mount(self):
        if pyautogui.locateOnScreen('hotbar\\mounted_hotbar.png', region=(660,1020,120,55)) == None:
            hit_key('z',dt1,dt2)
            time.sleep(random.uniform(1.1,1.3))
    
    def action_hotbar(self,key,target):
    
        if key == 'q':
            pic = self.q_pic
        if key == 'w':
            pic = self.w_pic
        if key == 'e':
            pic = self.e_pic
        if key == 'r':
            pic = self.r_pic
        if key == 'd':
            pic = self.d_pic
        if pyautogui.locateOnScreen(pic, region=(750,1000,510,60), confidence=0.8) != None:
            #debug((key,' is ready!'))
            location = None
            if target == 'self':
                _thread.start_new_thread(ability_self_target,(key))
            if target == 'allies' or target == 'allies none':
                location = game_screen.find_lowest_ally_healthbar()
                if location != None:
                    _thread.start_new_thread(ability_unit_target,(location[0],location[1],key))
            if target == 'enemy':
                location = game_screen.closest_red()
                if location != None:
                    _thread.start_new_thread(ability_unit_target,(location[0],location[1],key))

            #if ax != None and ay != None:
            #    if self.found_target == True:
            #            _thread.start_new_thread(ability_unit_target,(ax,ay,key))

    def target_ally(self):
        locations = game_screen.parsed_blue_hero_locations() 
    
        if locations == None:
            return None
        else:
            return locations[0], locations[1]
    def find_ally_mini_map(self):
        ally = pyautogui.locateOnScreen('blue_circle_mini.png', region=(1389,715,1919,1079), confidence=0.4)
        if ally != None:
            return ally.left, ally.top
        else:
            return None        

class clock_timer:
    def __init__(self,wait_time):
        self.wait_time = wait_time
        self.start_time = 0
    def start_timer(self):
        self.start_time = int(time.time())
    def check_timer(self):
        if int(time.time()) >= (self.start_time+self.wait_time):
            return True
        else:
            return False
    def reset_timer(self):
        self.start_time = 0         
#play location 960,450            
        #right_click(50,500)
def ability_unit_target(x,y,key):
    win32api.SetCursorPos((x+50, y+100))
    pyautogui.hotkey(key)

def ability_self_target(key):
    pyautogui.hotkey('alt',key)

def select_qm_hero():
    if check_region('role.png',0.8,350,100,100,50,0,0) != True:
        click(960,500,dt1,dt2)
    else:
        if move_cursor_through_heroes_last_row(1295, 820, 660): return True
        if move_cursor_through_heroes(1749, 740, 740): return True
        if move_cursor_through_heroes(1790, 660, 825): return True
        if move_cursor_through_heroes(1830, 580, 908): return True
        if move_cursor_through_heroes(1790, 500, 825): return True
        if move_cursor_through_heroes(1745, 420, 740): return True
        if move_cursor_through_heroes(1705, 340, 660): return True
        if move_cursor_through_heroes(1662, 260, 567): return True
def move_cursor_through_heroes_last_row(x,y,gap):
    for i in range (0,7):
        click(x,y,ft1,ft2)
        if i == 0:
            x = x - gap
        else:
            x = x - 83
        click(950,1050,ft1,ft2)
        if check_region('loadout.png',0.8,0,900,150,170,0,0) != True:
            return True

def move_cursor_through_heroes(x,y,gap):
    for i in range (0,12):
        click(x,y,ft1,ft2)
        if i == 5:
            x = x - gap
        else:
            x = x - 83
        click_region('smallready.png',0.8,900,950,150,150,0,0)
        if check_region('loadout.png',0.8,0,900,150,170,0,0) != True:
            return True


# Rows 260 add 80 each 820 time 8 rows
# columns 83 apart
# 1705 1625 1538
start_time=etime = int(time.time())
tentime = int(time.time())
fivetime = int(time.time())
onetime = int(time.time())
rotationtime = int(time.time())
redcoretime = int(time.time())
hero = 'default'
hero = 'abathur'

hero_1 = ''
hero_object_1 = ''
hero_2 = ''
hero_3 = ''
hero_4 = ''
hero_5 = ''

hero_select_setting='lowest'
#hero_select_setting='last'

gamemode = check_gamemode()

while keyboard.is_pressed('p') == False:
    #debug('getting etime')
    etime = int(time.time())

    if keyboard.is_pressed(']') != False:
        pyautogui.displayMousePosition()
    
    if gamemode == 1:
        if fivetime + 5 < etime:
            fivetime = int(time.time())
        if tentime + 10 < etime:
            tentime = int(time.time())            
            _thread.start_new_thread(talent_picker,())
            gamemode = check_gamemode()

        if hero_1 == '':
            hero_object_1=None
            hero_1 = check_hero()
        if hero_1 == 'tyrande':
            if hero_object_1 == None:
                hero_object_1 = hero_object('tyrande','healer',
                                            'unit','heal',          #q
                                            'projectile','attack',  #w
                                            'ground','attack',      #e
                                            'allies none','heal',   #r
                                            'unit','attack'         #d
                                            )
                hero_object_1.q_pic = pyautogui.screenshot(region=(760,1010,60,35))
                hero_object_1.w_pic = pyautogui.screenshot(region=(845,1010,60,35))
                hero_object_1.e_pic = pyautogui.screenshot(region=(930,1010,60,35))
                hero_object_1.r_pic = pyautogui.screenshot(region=(1015,1010,60,35))
                hero_object_1.d_pic = pyautogui.screenshot(region=(1100,1010,60,35))
                debug('Created Hero Object ' + hero_object_1.name)
            if game_screen == None:
                game_screen = check_game()
            hero_object_1.run_ai()
        if hero_1 == 'chen':
            if hero_object_1 == None:
                hero_object_1 = hero_object('chen','bruiser',
                                            'unit','attack',          #q
                                            'ground','attack',  #w
                                            'none','heal',      #e
                                            'none','attack',   #r
                                            'none','heal'         #d
                                            )
                hero_object_1.q_pic = pyautogui.screenshot(region=(760,1010,60,35))
                hero_object_1.w_pic = pyautogui.screenshot(region=(845,1010,60,35))
                hero_object_1.e_pic = pyautogui.screenshot(region=(930,1010,60,35))
                hero_object_1.r_pic = pyautogui.screenshot(region=(1015,1010,60,35))
                hero_object_1.d_pic = pyautogui.screenshot(region=(1100,1010,60,35))
                debug('Created Hero Object ' + hero_object_1.name)
            if game_screen == None:
                game_screen = check_game()
            hero_object_1.run_ai()
        if hero_1 == 'muradin':
            if hero_object_1 == None:
                hero_object_1 = hero_object('muradin','tank',
                                            'projectile','attack',          #q
                                            'ground','attack',  #w
                                            'ground','attack',      #e
                                            'unit','attack',   #r
                                            'unit','heal'         #d
                                            )
                hero_object_1.q_pic = pyautogui.screenshot(region=(760,1010,60,35))
                hero_object_1.w_pic = pyautogui.screenshot(region=(845,1010,60,35))
                hero_object_1.e_pic = pyautogui.screenshot(region=(930,1010,60,35))
                hero_object_1.r_pic = pyautogui.screenshot(region=(1015,1010,60,35))
                hero_object_1.d_pic = pyautogui.screenshot(region=(1100,1010,60,35))
                debug('Created Hero Object ' + hero_object_1.name)
            if game_screen == None:
                game_screen = check_game()
            hero_object_1.run_ai()
            
                    
        if hero_1 == 'abathur':
            if onetime + 1 < etime:
                onetime = int(time.time())
                q_hotbar = check_hotbar_ready('symbiote_hotbar.png')
                q2_hotbar = check_hotbar_ready('stab_hotbar.png')
                w2_hotbar = check_hotbar_ready('spike_burst_hotbar.png')
                e2_hotbar = check_hotbar_ready('carapace_hotbar.png')
                r2_hotbar = check_hotbar_ready('cancel_symbiote_hotbar.png')
                debug(f"Symbiote ready: {q_hotbar} Stab ready: {q2_hotbar} Spike Burst ready: {w2_hotbar} Carapace ready: {e2_hotbar}")
                if q_hotbar:
                    debug('Q is Ready!')
                    click_mini_map('blue_circle_mini.png', 15, 15, 0.4, False)
                    _thread.start_new_thread(hat,())
                if q2_hotbar:
                    if aim(25, 50):
                        hit_key('q', dt1, dt2)
                if w2_hotbar:
                    hit_key('w', dt1, dt2)
                if e2_hotbar:
                    hit_key('e', dt1, dt2)
                if r2_hotbar:
                    if random.uniform(1,20) < 2:
                        hit_key('r', dt1, dt2)
            if rotationtime + 5 < etime:
                rotationtime = int(time.time())
        if hero_1 == 'default':
            if hero_object_1 == None:
                hero_object_1 = hero_object('default','default',
                                            'unit','attack',          #q
                                            'unit','attack',  #w
                                            'unit','attack',      #e
                                            'unit','attack',   #r
                                            'unit','attack'         #d
                                            )
                hero_object_1.q_pic = pyautogui.screenshot(region=(760,1010,60,35))
                hero_object_1.w_pic = pyautogui.screenshot(region=(845,1010,60,35))
                hero_object_1.e_pic = pyautogui.screenshot(region=(930,1010,60,35))
                hero_object_1.r_pic = pyautogui.screenshot(region=(1015,1010,60,35))
                hero_object_1.d_pic = pyautogui.screenshot(region=(1100,1010,60,35))
                debug('Created Hero Object ' + hero_object_1.name)
            if game_screen == None:
                game_screen = check_game()
            hero_object_1.run_ai()
        if hero_1 == 'suicide':
            if rotationtime + 5 < etime:
                rotationtime = int(time.time())
                _thread.start_new_thread(rotation,())
                redcoretime = int(time.time())
                redcore = pyautogui.locateOnScreen('redcore.png', region=(1389,715,1919,1079), confidence=0.8)
                if redcore != None:
                    _thread.start_new_thread(attack_core,(redcore.left, redcore.top)) 
      
    if gamemode == 0:
        hero_1 = ''

        if check_region('smallready.png',0.8,900,950,150,150,0,0) == True:
            #debug('Found Ready Button!')
            if check_region('loadout.png',0.8,0,900,150,170,0,0) == True:
                #debug('In VS AI or QM')
                if hero_select_setting == 'lowest':
                   select_qm_hero()
                if hero_select_setting == 'last':
                    click_region('smallready.png',0.8,900,950,150,150,0,0)
            else:
                if check_region('smallready.png',0.8,900,950,150,150,0,0) == True:
                    debug('Not in VS AI or QM hitting ready!')
        if click_region('smallleave.png',0.9,95,980,245,200,0,0) == True:
            debug('Found Leave Button!')
        if click_region('smallrejoin.png',0.9,750,590,200,200,0,0) == True:
            debug('Found Rejoin Button!')
        if click_region('smallok.png',0.9,900,460,250,200,0,0) == True:
            debug('Found ok Button!')
        if click_region('smallexit.png',0.9,95,980,245,200,0,0) == True:
            debug('Found Exit Button!')
        gamemode = check_gamemode()
        game_screen = None
    if gamemode == 2:
        debug("Drafting!")
        ban_hero = pyautogui.locateOnScreen('ban_hero.png', region=(830,940,220,100), confidence=0.9)
        lock_in = pyautogui.locateOnScreen('lock_in.png', region=(830,940,220,100), confidence=0.9) #fixed
        lock_in_light = pyautogui.locateOnScreen('lock_in_light.png', region=(830,940,220,100), confidence=0.9)
        #if ban_hero != None:
        #    select_ban()
        if lock_in != None or lock_in_light != None:
            debug('lock in Found')
            select_hero()
        gamemode = check_gamemode()
        game_screen = None

       

            
            
 # 390,240,110,60 playerone tab portrait
   
#    pic = pyautogui.screenshot(region=(660,350,600,400))

#    width, height = pic.size

#    for x in range(0,width,5):
#        for y in range(0,height,5):

#            r,g,b = pic.getpixel((x,y))

#            if b == 195:
#                click(x+660,y+350)
#                time.sleep(0.05)
#                break

# hotbar locations
#top 1010
#bottom 1045
# ql 760 qr 820 wl 845 wr 905 el 930 er 990 rl 1015 rr 1075 dl 1100 dr 1160
# 760,1010,60,35


        #print(blue_hero_location)
        
        #for x2 in range(0,1919,4):
        #    for y2 in range (play_area_y[0],play_area_y[0],5):
        #        r,g,b = screen.getpixel((x2,y2))
        #        if r > 175 and g == 0:
        #            self.red_location.append((x2, y2))
                #opposite_x = 960-xy[0]+960
        #opposite_y = 450-xy[1]+450
        #move_cap = 300
        #if opposite_redx > 960+move_cap: opposite_redx = 960+move_cap
        #if opposite_redx < 960-move_cap: opposite_redx = 960-move_cap
        #if opposite_redy > 450+move_cap: opposite_redx = 450+move_cap
        #if opposite_redy < 450-move_cap: opposite_redx = 450-move_cap
#def action_q(self):
#        if self.q_pic == None: debug('q_pic = none')
##       else: debug('q_pic is not none')
 #       if pyautogui.locateOnScreen(self.q_pic, region=(760,1010,60,35), confidence=0.8) != None:
 #           debug('Q is ready!')
 #           ax = None
 #           ay = None
 #           if self.target == 'self':
 #               _thread.start_new_thread(ability_self_target,('q'))
 ##           if self.target == 'allies':
#                ally_location = self.target_ally()
#                if ally_location != None:
#                    self.found_target = True
#                    debug('ally location set')
#                    ax = ally_location[0]
#                    ay = ally_location[1]
#                else:
#                    self.found_target = False
#            if self.found_target == True:
#                debug('ally location used')
#                if ax != None:
##                    _thread.start_new_thread(ability_unit_target,(ax,ay,'q'))
# #               else:
#                    debug('error x not set')
#        debug('leaving action q')