class GameRule:
    def __init__(self, board_manager):
        self.bm = board_manager
        pass

    def count_consecutive(self, r, c, dr, dc, current_player):
        """
        Đếm số quân cờ liên tiếp của cùng một người chơi theo hướng (dr, dc)
        
        Tham số:
            r, c: Tọa độ bắt đầu
            dr, dc: Hướng di chuyển và có tổng cộng 4 hướng di chuyển [(1,0), (0, 1), (1, 1), (1, -1)] và 4 hướng ngược lại.
            current_player: Người chơi (1 hoặc 2)
            count: Số lượng quân cờ liên tiếp
        
        Trả về:
            count
        """
        pass

    def is_winner(self, r, c):
        """
        Kiểm tra quân cờ vừa đặt tại vị trí (row, col) có tạo chuỗi thắng không
        
        Tham số:
            r, c: Tọa độ vừa đặt quân cờ
        
        Trả về:
            True nếu tạo chuỗi thắng, False nếu không
        """
        pass

    def check_draw(self):
        #Kiểm tra hòa nếu như bàn cờ đã đầy
        return self.bm.is_board_full()