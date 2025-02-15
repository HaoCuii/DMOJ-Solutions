inp = int(input())
score_moves = []
for i in range(inp * 2):
    score_moves.append(int(input()))

for j in range(inp):
    score = list(str(score_moves[j * 2]))
    score = [int(val) for val in score]
    final_score = []
    x = score_moves[j * 2 + 1]
    if ''.join(map(str, final_score + score)) == min(score):
        break
    else:
        for k in range(x):
            if len(score) != 0:
                moving_val = score[:x + 1]
                moving_val_min = min(moving_val)
                while True:
                    if len(moving_val) != 0:
                        if score[0] == moving_val_min:
                            final_score.append(score[0])
                            score.pop(0)
                            moving_val = score[:x + 1]
                            if len(moving_val) != 0:
                                moving_val_min = min(moving_val)
                        else:
                            break
                    else:
                        break
                if x > 0 and len(moving_val) != 0:
                    before_moving_val = moving_val[:moving_val.index(moving_val_min)]
                    before_moving_val_sorted = sorted(before_moving_val)
                    score.pop(score.index(before_moving_val_sorted[0]))
                    score.append(before_moving_val_sorted[0])
                    x -= 1
        print(''.join(map(str, final_score + score)))
