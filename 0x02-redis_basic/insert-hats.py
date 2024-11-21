import redis
import random


server = redis.Redis(db=0)

hats = {f"hats:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}

# with server.pipeline() as pipe:
#     for key, value in hats.items():
#         pipe.hmset(key, value)
#     print(pipe.execute())

print(server.keys())