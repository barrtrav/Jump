class Settings:    
    def __init__(self) -> None:

        # Game setting
        self.game_active = True
        
        # Screen settings
        self.screen_caption = "Jump"
        self.screen_size = (1600, 800)
        self.screen_color = (230, 230, 230)

        # Avatar settings
        self.avatar_speed = 5
        self.avatar_jump_speed = 5

        # Block settings
        self.block_width = 400
        self.block_height = 30
        self.block_color = (30, 30, 30)
        self.block_speed = 5