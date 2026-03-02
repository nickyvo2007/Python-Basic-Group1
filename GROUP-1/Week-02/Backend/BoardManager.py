class BoardManager:
    def __init__(self, size=15):
        self.size= size
        # Khởi tạo ma trận bàn cờ 15x15 với 0 - trống, 1 - quân X, và 2 - quân O
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

        # Quản lý lượt đi hiện tại với 1 - X, 2 - O
        self.current_player = 1 

        # Quản lý lịch sử nước đi, mỗi phần tử là một tuple (row, col, current_player)
        self.history = []

    def reset_board(self):
        # Dùng để reset game và chơi ván mới
        pass

    def is_valid_pos(self, r, c):
        #Kiểm tra tọa độ có nằm trong phạm vi bàn cờ hay không
        #Trả về True nếu tọa độ hợp lệ, False nếu không hợp lệ
        pass

    def get_value(self, r, c):
        #Lấy giá trị tại ô (row, col) vừa đánh, trả về -1 nếu tọa độ không hợp lệ
        #Trả về giá trị tại ô đó self.matrix[row][col]
        pass

    def place_stone(self, r, c):
        #Đặt quân cờ vào ô (row, col). 
        # Trả về True, lưu nước đi vào self.history nếu đặt thành công và chuyển đổi người chơi
        # Trả về False nếu đã có quân cờ hoặc tọa độ không hợp lệ
        pass

    def undo(self):
        #Hoàn tác nước đi gần nhất và cuối cùng
        #Trả về None nếu chưa có nước đi nào cả
        #Trả về tuple chứa nước đi trước đó (last_row, last_col, last_player)
        pass

    def is_board_full(self):
        #Kiểm tra bàn cờ xem đã đầy chưa
        #Trả về True nếu bàn cờ đã đầy, False nếu còn ô trống
        pass