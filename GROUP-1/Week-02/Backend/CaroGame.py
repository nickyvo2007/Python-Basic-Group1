import json
import time
from BoardManager import BoardManager  
from GameRule import GameRule    

class GomokuEngine:
    def __init__(self, board_size=15, time_limit=30):
        #Kết hợp nội dung từ các file BoardManager và GameRule
        self.bm = BoardManager(board_size= 15)
        self.gr = GameRule(self.bm)

        #Quản lý trạng thái Game
        self.game_state = "MENU" # MENU, PLAYING, GAME_OVER, TIME_OUT
        self.winner = None # None, 1, 2, "DRAW"
        
        #Quản lý thời gian
        self.time_limit = 30
        self.turn_start_time = 0

    def undo_move(self):
        """
        Hoàn tác lại về nước đi trước đó
        Chỉ cho phép hoàn tác khi game_state = PLAYING
        Đồng thời restart lại thời gian turn_start_time
        """
        pass

    def start_new_game(self):  
        """
        Khởi tạo lại bàn cờ, đặt game_state về PLAYING và bắt đầu đếm thời gian 
        """                                      
        print("New Game Start")

    def handle_click(self, r, c): #Hàm này sẽ được gọi khi xử lý Frontend
        """
        Kiểm tra trạng thái khi người chơi click vào bàn cờ
        Nếu vị trí hợp lệ thì trả về True và:
            + Nếu có người thắng thì chuyển game_state về GAME_OVER và winner = người chơi đó
            + Nếu dùng bm.is_board_full() = True thì game_state về GAME_OVER và winner = "DRAW"
            + Nếu vẫn chưa có người thắng và bàn cờ chưa đầy thì set lại turn_start_time = time.time()
        Nếu vị trí không hợp lệ hoặc trạng thái game_state != "PLAYING" thì trả về False
        """
        pass

    def update_logic(self):
        """
        Hàm để kiểm thời gian chơi mỗi lượt khi đang trong game
        Nếu như hết thời gian chuyển game_state = "TIME_OUT" và bm.current_player = người còn lại
        """
        pass

    def save_game(self, filepath="save_game.json"):
        """
        Lưu bàn cờ đang chơi dở bằng file json với dict data gồm các key là 'matrix', 'current_player', 'history', 'game_state', 'time_left'
        """
        pass

    def load_game(self, filepath="save_game.json"):
        """Đọc file json và khôi phục trạng thái bàn cờ với các dữ liệu trong dict data đã lưu 'matrix', 'current_player', 'history', 'game_state', 'time_left'"""
        pass


    