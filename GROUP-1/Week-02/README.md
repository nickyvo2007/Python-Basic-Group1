# Caro Game Project

Structure chung hiện tại của project sẽ là như sau: 
```
Caro_Project/
│
├── main.py                 # File chạy chính
├── constants.py            # Quy ước chung về màu sắc, kích thước - hiện tại chưa cập nhật
│
├── Backend/       
│   ├── BoardManager.py     # Dữ liệu ma trận, đặt quân, Undo
│   ├── GameRule.py         # Logic trò chơi (kiểm tra 5 quân liên tiếp, kiểm tra thắng, kiểm tra hòa)
│   └── CaroGame.py         # bộ xử lý chính kết hợp BoardManager và GameRule, xử lý thời gian, Save/Load
│
└── Frontend/               
    ├── Interaction.py      # Bắt sự kiện chuột, chuyển tọa độ pixel -> grid
    ├── Render.py           # Vẽ lưới bàn cờ, vẽ quân cờ
    ├── UIManager.py        # Vẽ Menu, nút bấm, đồng hồ đếm ngược
    └── assets/             # Thư mục chứa hình ảnh, âm thanh
```
Trong tuần này tụi mình sẽ cùng nhau xử lý phần Backend của Project 

# Hướng Dẫn Code Backend (Caro Game) - Tránh Xung Đột Biến

## 1. Công dụng từng class (tương ứng với tên file .py)

- **`BoardManager` (`BoardManager.py`)**: Chỉ quản lý **dữ liệu vật lý** của bàn cờ (`matrix`, `size`, `history`, `current_player`)

- **`GameRule` (`GameRule.py`)**: Chứa **thuật toán logic** (kiểm tra thắng, đếm số quân, kiểm tra hòa), nhận tham chiếu `board_manager` và **chỉ** đọc dữ liệu từ nó.

- **`CaroGame` (`CaroGame.py`)**: Là **bộ xử lý chính**, bao gồm và liên kết `BoardManager` và `GameRule`. Xử lý lưu/tải game, đếm thời gian (`time_limit`, `turn_start_time`), điều khiển trạng thái game (`game_state`, `winner`).

---

## 2. Quy Tắc Đặt Tên Biến 

### Hệ Tọa độ Bàn cờ

- **`(r, c)`** (như trong hàm mẫu) để chỉ số dòng và số cột của bàn cờ.

### Định Danh Trạng Thái Ô & Người chơi

- **`current_player`** là biến để xác định người chơi hiện hành

- Quy ước đánh số: `0` (trống), `1` (người chơi X), `2` (người chơi O). 

### Đối tượng tham chiếu chéo
Khi gọi class này trong class khác, tuân thủ đúng tên biến định sẵn sau: 

- Tham chiếu tới `BoardManager`: **`self.bm`** (dùng trong `GameRule` và `CaroGame`).

- Tham chiếu tới `GameRule`: **`self.gr`** (trong `CaroGame`).

---

## 3. Quy Tắc Giao Tiếp Giữa Các Class 

**Quan trọng:** Hạn chế truy cập và sửa đổi trực tiếp (Direct Access) thuộc tính của class khác mà dùng qua các Method (hàm).

- **Khi cần xem giá trị ô cờ:**
  - ✅ **NÊN:** Sử dụng `self.bm.get_value(r, c)`.
  - ❌ **KHÔNG NÊN:** Viết `self.bm.matrix[r][c]`.

- **Khi cần đặt quân cờ:**
  - ✅ **NÊN:** Gọi `self.bm.place_stone(r, c)`. Hàm này sẽ lo mọi việc (kiểm tra ô, lưu mảng, ghi lịch sử, đổi turn).
  - ❌ **KHÔNG NÊN:** Tự gán `self.bm.matrix[r][c] = current_player` và tự tính `self.bm.history.append()`.

---

## 4. Các "Từ Khóa" Quan Trọng

Dưới đây là các biến đã được khai báo ở `__init__`. **TUYỆT ĐỐI KHÔNG KHAI BÁO** biến cục bộ trong thuật toán ghi đè lại tên của những biến này:

*Thuộc về `BoardManager`:*
- `size` (Kích thước bàn cờ, mặc định 15)
- `matrix` (Mảng 2 chiều lưu trữ)
- `history` (Mảng lưu các tuple nước đi)
- `current_player` (Biến theo dõi phiên hiện tại)

*Thuộc về `CaroGame` (`CaroGame.py`):*
- `game_state`: Trạng thái trò chơi. (Được quy định chỉ chứa chuỗi: `"MENU"`, `"PLAYING"`, `"GAME_OVER"`, `"TIME_OUT"`)
- `winner`: Xác định thắng cuộc. (Quy định: `None`, `1`, `2`, `"DRAW"`)
- `time_limit`, `turn_start_time`: Các thông số đo đếm giờ.

*Thuộc về `GameRule`:*
- Khi xét các hướng đi trong mảng thuật toán, hãy dùng **`dr, dc`** (delta row, delta col).

---

## 5. Checklist Bắt Buộc Trước Khi Ghép Code (Merge / Push)
1. [ ] Biến đếm (loop variables) trong các vòng `for` có tên rõ ràng chưa? Tránh việc đặt biến toàn cụ thể.
2. [ ] Bạn đã tận dụng hết các Method (hàm định nghĩa sẵn) giữa 3 file chưa? Hay đang can thiệp ngầm vào mảng `self.bm.matrix`?
3. [ ] Tham số đầu vào các hàm xử lý tọa độ đều là `(r, c)` chứ không phải mâu thuẫn hệ tọa độ?

