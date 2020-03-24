import chess

class Board(object):
  def __init__(self):
    self.getBoard()
  def getBoard(self):
    self.board = chess.Board()
    return self.board

if __name__ == "__main__":
  s = Board()
