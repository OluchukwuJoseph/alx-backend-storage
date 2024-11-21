#!/usr/bin/env python3
""" This module contains the Cache class """
import redis
import uuid
from typing import Union, Callable


class Cache():
    """
    Generate a redis client.
    Use it methods to perform operations on redis server
    """
    def __init__(self):
        """ Initialize class """
        self.__redis = redis.Redis()
        self.__redis.flushdb()
    
    def store(self, data: Union[str, int, bytes, float]) -> str:
        """
        Generate a random key,
        store `data` in Redis using the random key,
        and return the random key"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable=None):
        """ Retrieve the value of key then call `fn` on it """
        value = self.__redis.get(key)
        try:
            value = fn(value)
        except TypeError:
            pass
        return value
    
    def get_str(self, key: str):
        """
        Call `get` but automatically use a conversion function (fn)
        to convert the value to a string.
        """
        return self.get(key, lambda string: string.decode('utf-8'))
    
    def get_int(self, key: str):
        """
        Call `get` but automatically use a conversion function (fn)
        to convert the value to an integer.
        """
        return self.get(key, int)
