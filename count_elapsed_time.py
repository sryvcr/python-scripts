from time import time as __time


def count_elapsed_time(f):
    """
        Decorator.
        Execute the function and calculate the elapsed time.
        Print the result to the standard output.

        How to use:
        
        @count_elapsed_time
        def foo():
            pass
    """
    def wrapper(*args, **kwargs):
        # Start counting.
        start_time = __time()
        # Take the original function's return value.
        ret = f(*args, **kwargs)
        # Calculate the elapsed time.
        elapsed_time = __time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret

    return wrapper
