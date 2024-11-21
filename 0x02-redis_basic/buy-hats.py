import redis
import logging
import time


logging.basicConfig()

server = redis.Redis(db=0)

class OutOfStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""

def buyitem(item_id):
    with server.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                pipe.watch(item_id)
                n_hats = server.hget(item_id, 'quantity')
                if n_hats > b'0':
                    pipe.multi()
                    pipe.hincrby(item_id, 'quantity', -1)
                    time.sleep(30)
                    pipe.hincrby(item_id, 'npurchased', 1)
                    pipe.execute()
                    # break
                else:
                    raise OutOfStockError(f'Sorry, {item_id} is out of stock!')
            except redis.WatchError:
                error_count += 1
                logging.warning("WatchError #%d: %s; retrying", error_count, item_id)

    return None


if __name__ == "__main__":
    for _ in range(1):
        buyitem('hats:2076161522')
    print(server.hgetall('hats:2076161522'))