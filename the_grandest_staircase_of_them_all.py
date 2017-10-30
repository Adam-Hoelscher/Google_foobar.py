def answer(n):

    cache = dict()

    def recur(n, min_height):

        # check to see if this is in the cache
        if (n, min_height) in cache:
            return (cache[(n, min_height)])
        temp = 1

        for step in range(min_height, n + 1):
            next_n = n - step
            next_min = step + 1
            if next_min <= next_n:
                temp += recur(next_n, next_min)

        # store to the cache and then return
        cache[(n, min_height)] = temp
        return (temp)

    # we've got to knock one off the recursive call because we have to have at
    # least two stairs in our staircase
    return(recur(n, 1) - 1)

if __name__ == '__main__':
    print(answer(3))
    print(answer(200))
