import time
import grpc


class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = grpc.RpcError
        self.failures = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def is_open(self):
        if self.state == "OPEN":
            if (time.time() - self.last_failure_time) > self.recovery_timeout:
                self.state = "HALF-OPEN"
                return False
            return True
        return False

    def on_success(self):
        self.state = "CLOSED"
        self.failures = 0

    def on_failure(self):
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            self.last_failure_time = time.time()

    def call(self, func, *args, **kwargs):
        if self.is_open():
            raise grpc.RpcError("Circuit breaker is OPEN")

        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except self.expected_exception as e:
            self.on_failure()
            raise e
