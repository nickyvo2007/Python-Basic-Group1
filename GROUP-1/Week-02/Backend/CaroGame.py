import json
import time
from BoardManager import BoardManager
from GameRule import GameRule
import pygame

class CaroGame:
    def __init__(self, board_size=15, time_limit=30):
        # Kết hợp nội dung từ các file BoardManager và GameRule
        self.bm = BoardManager(board_size=15)
        self.gr = GameRule(self.bm)

        # Quản lý trạng thái Game
        self.game_state = "MENU"  # MENU, PLAYING, GAME_OVER, TIME_OUT
        self.winner = None  # None, 1, 2, "DRAW"



    def start_new_game(self):
        """
        Khởi tạo lại trạng thái để bắt đầu chơi ngay lập tức.
        """
       
        self.bm.board = [[' ' for _ in range(15)] for _ in range(15)]
        
        self.current_turn = 1 
        
        self.game_state = "PLAYING"
        
        self.winner = None
        
        print("--- Game Started / Reset ---")
       

    def save_game(self, filepath="save_game.json"):
        state_save = {
            "board": self.bm.board,
            "turn": getattr(self, 'current_turn', 1), # Safely get current_turn
            "game_state": self.game_state
        }
        with open(filepath, 'w') as file:
            json.dump(state_save, file)
        print('Game saved successfully to ', filepath)

    def load_game(self, filepath="save_game.json")
        try: 
            open(filepath, 'r') as file:
            load_state = json.load(file)
            self.bm.board = load_state["board"]
            self.current_turn = load_state["turn"]
            self.game_state = load_state["game_state"]
            print("Game successfully loaded from ", filepath)
        except FileNotFoundError:
           print("Save file not found. Try again")
        except json.JSONDecodeError:
           print("Json code error. Try again")


    def handle_click(self, r, c):
        if self.game_state != "PLAYING":
            return

        # 2. Logic check: Make sure the space is empty via BoardManager
        # (Assuming BoardManager has an is_empty and place_piece method)
        if self.bm.board[r][c] == ' ':
            self.bm.board[r][c] = self.current_turn

            # 3. Rule check: Delegate to GameRule to see if this move won
            if self.gr.is_winner(r, c):
                self.game_state = "GAME_OVER"
                self.winner = self.current_turn
                print(f'Player {self.winner} wins!')
            else:
                # 4. Swap turn: 1 becomes 2, 2 becomes 1
                self.current_turn = 2 if self.current_turn == 1 else 1
