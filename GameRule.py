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
        counts = 0
        cur_r = r + dr
        cur_c = c + dc
        while (0 <= cur_c < self.bm.size 
               and 0 <= cur_r < self.bm.size
               and self.bm.get_value(cur_r, cur_c) == current_player):
            counts += 1
            cur_r += dr
            cur_c += dc
        return counts

    def is_winner(self, r, c):
        """
        Kiểm tra quân cờ vừa đặt tại vị trí (row, col) có tạo chuỗi thắng không
        
        Tham số:
            r, c: Tọa độ vừa đặt quân cờ
        
        Trả về:
            True nếu tạo chuỗi thắng, False nếu không
        """
        cur_pos = self.bm.get_value(r, c)
        if cur_pos == 0:
            return False
        directions = [(0,1), (1,0), (1,1), (1,-1)]
        for dr, dc in directions:
            total = 1 + self.count_consecutive(r, c, dr, dc, cur_pos) \
                      + self.count_consecutive(r, c, -dr, -dc, cur_pos) 
            if total >= 5:
                return True
        return False

    def check_draw(self):
        #Kiểm tra hòa nếu như bàn cờ đã đầy
        return self.bm.is_board_full()