balls = [1, 2, 3, 4, 5, 6]
boxes = [[],[],[]]
for ball in balls:
    for box in boxes:
        if len(box)==0:
            box.append(ball)
            continue
print(boxes)