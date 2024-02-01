from Controller.Data_loader import *
class Player:
    def __init__(self,user_id):
        self.dataloader = Data
        self.user_id = user_id
        self.progress = self.dataloader.load_user_data(self.user_id)

    def player_move(self):
        pass
    
    def next_turn(self):
        pass
    
    def build_smth(self):
        pass

    def player_info(self):
        pass
    