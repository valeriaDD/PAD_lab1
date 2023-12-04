import logging
import time
import grpc

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s | [%(levelname)s]: %(message)s")


class CircuitBreakerException(Exception):
    pass


class RerouteException(Exception):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = grpc.RpcError
        self.failures = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def call(self, func, *args, **kwargs):
        if self.is_open():
            logging.error("Circuit breaker is OPEN")
            raise CircuitBreakerException("Circuit breaker is OPEN")

        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INTERNAL:
                self.on_failure()
                raise RerouteException('Service failed: reroute!')
            raise e

    def is_open(self):
        if self.state == "OPEN":
            if (time.time() - self.last_failure_time) > self.recovery_timeout:
                self.state = "HALF-OPEN"
                logging.info("Circuit breaker is HALF-OPEN")
                return False
            return True
        return False

    def on_success(self):
        self.state = "CLOSED"
        self.failures = 0
        logging.info("Request succeeded")

    def on_failure(self):
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"
            self.last_failure_time = time.time()
            logging.error("Request failed")
