from concurrent import futures
import grpc
import connectfour_pb2
import connectfour_pb2_grpc
from queue import Queue
import threading

class ConnectFourServicer(connectfour_pb2_grpc.ConnectFourServicer):
    def __init__(self):
        self.clients = {}
        self.message_queues = {}
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.lock = threading.Lock()
        self.game_over = False
        self.winner = 0

    def Connect(self, request, context):
        with self.lock:
            client_name = request.name
            player_id = len(self.clients) + 1
            if player_id > 2:
                return connectfour_pb2.ConnectionStatus(connected=False, player_id=0)

            self.clients[client_name] = player_id
            self.message_queues[client_name] = Queue()
            print(f"Cliente {client_name} conectado como jogador {player_id}.")
            return connectfour_pb2.ConnectionStatus(connected=True, player_id=player_id)

    def MakeMove(self, request, context):
        with self.lock:
            if self.game_over:
                return connectfour_pb2.GameStatus(valid_move=False, message="Jogo já terminou.", game_over=True, winner=self.winner)

            if request.player_id != self.current_player:
                return connectfour_pb2.GameStatus(valid_move=False, message="Não é a sua vez.", game_over=False)

            col = request.col
            if col < 0 or col >= 7 or self.board[0][col] != ' ':
                return connectfour_pb2.GameStatus(valid_move=False, message="Movimento inválido.", game_over=False)

            for row in range(5, -1, -1):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X' if self.current_player == 1 else 'O'
                    self.current_player = 2 if self.current_player == 1 else 1
                    break

            self.check_winner()
            update = connectfour_pb2.GameUpdate(
                board=self.create_board_message(),
                message=f"Jogador {request.player_id} moveu.",
                game_over=self.game_over,
                winner=self.winner
            )
            for queue in self.message_queues.values():
                queue.put(update)

            return connectfour_pb2.GameStatus(valid_move=True, message="Movimento válido.", game_over=self.game_over, winner=self.winner)

    def GetUpdates(self, request, context):
        client_name = request.name
        while True:
            if client_name in self.message_queues:
                update = self.message_queues[client_name].get()
                yield update

    def check_winner(self):
        board = self.board

        # Verificar vitória horizontal
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                if board[row][col] != ' ' and board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                    self.end_game(board[row][col])

        # Verificar vitória vertical
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                if board[row][col] != ' ' and board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                    self.end_game(board[row][col])

        # Verificar vitória diagonal (para cima)
        for row in range(3, len(board)):
            for col in range(len(board[0]) - 3):
                if board[row][col] != ' ' and board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                    self.end_game(board[row][col])

        # Verificar vitória diagonal (para baixo)
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                if board[row][col] != ' ' and board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                    self.end_game(board[row][col])

        # Verificar empate
        if all(board[0][col] != ' ' for col in range(len(board[0]))):
            self.end_game(' ')

    def end_game(self, winner_symbol):
        self.game_over = True
        if winner_symbol == 'X':
            self.winner = 1
        elif winner_symbol == 'O':
            self.winner = 2
        else:
            self.winner = 0
        for queue in self.message_queues.values():
            queue.put(connectfour_pb2.GameUpdate(
                board=self.create_board_message(),
                message="Fim de jogo.",
                game_over=True,
                winner=self.winner
            ))

    def create_board_message(self):
        return connectfour_pb2.Board(rows=[connectfour_pb2.Row(cells=row) for row in self.board])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connectfour_pb2_grpc.add_ConnectFourServicer_to_server(ConnectFourServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor Connect Four conectado na porta 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()