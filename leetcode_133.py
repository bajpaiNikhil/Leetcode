


from collections import deque

deck=[17,13,11,2,3,5,7]
deck.sort(reverse=True)

queue=deque()

for cards in deck:
    if queue:
        queue.appendleft(queue.pop())
    queue.appendleft(cards)
print(queue)