from board import Board

results = Board()
for i in range(1000):
    board = Board()
    board.simulate()
    results += board

print(results)
print(results.player.rolls)