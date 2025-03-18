class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["", "", ""], ["", "", ""], ["", "", ""]]
        move_count = 0
        for move in moves:
            if move_count % 2 == 0:  # Player X's turn
                if board[move[0]][move[1]] == "":
                    board[move[0]][move[1]] = "X"
                    result = self.winnercheck(board)
                    if result:  # If a winner is found, return the winner
                        return result
            else:  # Player O's turn
                if board[move[0]][move[1]] == "":
                    board[move[0]][move[1]] = "O"
                    result = self.winnercheck(board)
                    if result:  # If a winner is found, return the winner
                        return result
            move_count += 1
        if move_count < 9:
            return "Pending"
        return "Draw"
                        
        '''board =[ 
                 ["","",""],
                 ["","",""],
                 ["","",""] 
                 ]
        move_count = 0
        while move_count <= 9:
            for move in moves:
                if moves.index(move) % 2 == 0:
                    if board[move[0]][move[1]] == "":
                        board[move[0]][move[1]] = "X"
                        self.winnercheck(board,move_count)
                        move_count+=1
                elif moves.index(move) % 2 != 0:
                    if board[move[0]][move[1]] == "":
                        board[move[0]][move[1]] = "O"
                        self.winnercheck(board,move_count)
                        move_count +=1'''

    '''def winnercheck(self,board, move_count):
        if board[0][0] == board[0][1] == board[0][2] == "X" or \
        board[1][0] == board[1][1] == board[1][2] == "X" or \
        board[2][0] == board[2][1] == board[2][2] == "X" or \
        board[0][0] == board[1][0] == board[2][0] == "X" or \
        board[0][1] == board[1][1] == board[2][1] == "X" or \
        board[0][2] == board[1][2] == board[2][2] == "X" or \
        board[0][0] == board[1][1] == board[2][2] == "X" or \
        board[0][2] == board[1][1] == board[2][0] == "X":
            return "A"
        elif board[0][0] == board[0][1] == board[0][2] == "O" or \
        board[1][0] == board[1][1] == board[1][2] == "O" or \
        board[2][0] == board[2][1] == board[2][2] == "O" or \
        board[0][0] == board[1][0] == board[2][0] == "O" or \
        board[0][1] == board[1][1] == board[2][1] == "O" or \
        board[0][2] == board[1][2] == board[2][2] == "O" or \
        board[0][0] == board[1][1] == board[2][2] == "O" or \
        board[0][2] == board[1][1] == board[2][0] == "O": 
            return "B"
        else:
            if move_count > 9:
                return "Draw"'''
    
    def winnercheck(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return "A" if board[i][0] == "X" else "B"
            if board[0][i] == board[1][i] == board[2][i] != "":
                return "A" if board[0][i] == "X" else "B"
        
        if board[0][0] == board[1][1] == board[2][2] != "":
            return "A" if board[0][0] == "X" else "B"
        if board[0][2] == board[1][1] == board[2][0] != "":
            return "A" if board[0][2] == "X" else "B"
        
        return None 

           


            
        
        
                    

                    
                
        