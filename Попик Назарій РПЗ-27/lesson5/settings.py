class Settings:
    """Клас для зберігання усіх налаштувань для гри"""

    def __init__(self):
        #Screen settings
        self.screen_color = (230,230,230) # rgb
        self.screen_width = 1200
        self.screen_height = 700
        self.screen_caption = 'Alien Invasion'

        #Ship 
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 - рух праворуч, -1 - рух ліворуч