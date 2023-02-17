# Simple Deque example


from pythonds.basic.deque import Deque

def palchecker(aString):
    charDeque = Deque()

    for i in aString:
        charDeque.addRear(i)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("Eazy"))
print(palchecker("radar"))
