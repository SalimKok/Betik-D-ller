from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        print("total_time:", time.perf_counter() - t0)
        return result
    return wrapper


def required_columns(requireds: set[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rows = func(*args, **kwargs)

            if not rows:
                raise ValueError("CSV boş veya okunamadı!")

            first = rows[0]
            if not isinstance(first, dict):
                raise TypeError("CSV satırları sözlük formatında olmalı.")

            keys = set(first.keys())
            missing = requireds - keys
            if missing:
                raise ValueError(f"Eksik kolonlar: {missing}")

            return rows
        return wrapper
    return decorator
