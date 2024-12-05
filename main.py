"""
	Требуется разработать компьютерную игру «крестики-нолики».
	Минимальные требования:
	1.Графичекский интерфейс (использовать внутреннюю библиотеку питона  tkinter).
	2.Игра с приложением (приложение не должно проигрывать)
	3. Минимальный комплект программной документации в соответствии с ГОСТ 19 группы:
	1.1.Техническое задание
	1.2.Пояснительная записка
	1.3.Руководство программиста
	4. Тестовая документация:
	2.1. Mind map
	2.2. Чек-лист
	2.3. Набор тест-кейсов  
"""

import tkinter as tk 
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Крестики-нолики")

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'  # Начинает игрок X

        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text="", font=('Helvetica', 60), width=4, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)
            if self.check_win():
                self.game_over()
                return
            if self.check_draw():
                self.game_over(draw=True)
                return
            self.turn = 'O' if self.turn == 'X' else 'X'
            self.computer_move()

    def check_win(self):
        # Проверка строк, столбцов и диагоналей
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def game_over(self, draw=False):
        if draw:
            message = "Ничья!"
        elif self.turn == 'X':
            message = "Выиграл компьютер!"
        else:
            message = "Вы проиграли!"

        result_window = tk.Toplevel(self.master)
        result_window.title("Результат")
        tk.Label(result_window, text=message, font=('Helvetica', 20)).pack(pady=20)
        tk.Button(result_window, text="Новая игра", command=self.restart).pack()


    def computer_move(self):
        if self.turn == 'O':
            best_move = self.find_best_move()
            if best_move:
                self.make_move(best_move[0], best_move[1])

    def find_best_move(self):
      # Пытается выиграть
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == '':
            self.board[i][j] = 'O'
            if self.check_win():
              self.board[i][j] = ''
              return (i, j)
            self.board[i][j] = ''

      # Блокирует выигрыш игрока
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == '':
            self.board[i][j] = 'X'
            if self.check_win():
              self.board[i][j] = ''
              return (i, j)
            self.board[i][j] = ''

      # Занимает центр, если свободен
      if self.board[1][1] == '':
        return (1, 1)

      # Занимает угол, если свободен
      corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
      for corner in corners:
        if self.board[corner[0]][corner[1]] == '':
          return corner

      # Занимает любое свободное место
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == '':
            return (i, j)

      return None

    def restart(self):
        self.master.destroy()
        root = tk.Tk()
        TicTacToe(root)
        root.mainloop()


def main():
	root = tk.Tk()
	game = TicTacToe(root)
	root.mainloop()

if __name__ == "__main__":
	main()