import time
from fastapi import HTTPException
from redis import Redis

class TokenBucket:
    def __init__(self, redis: Redis, key: str, rps: float):
        self.redis = redis
        self.key = key
        self.rps = rps
        self.capacity = max(1, int(rps*3))

    def allow(self) -> bool:
        now = time.time()
        with self.redis.pipeline() as p:
            p.zremrangebyscore(self.key, 0, now - 1)
            p.zcard(self.key)
            p.execute()
            count = self.redis.zcard(self.key)
            if count >= self.capacity:
                return False
            self.redis.zadd(self.key, {str(now): now})
            self.redis.expire(self.key, 2)
            return True
        
def enforce_rate_limit(bucket: TokenBucket):
    if not bucket.allow():
        raise HTTPException(status_code=429, detail = "Rate Limit Exceeded")