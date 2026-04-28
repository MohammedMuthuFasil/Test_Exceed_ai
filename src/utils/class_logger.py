import time

class ClassLogger:
    def __init__(self,func):
        self.func = func
        
    def __get__(self,instance,owner):
        return lambda *args, **kwargs: self(instance,*args,**kwargs)
    
    def __call__(self,*args,**kwargs):
        instance = args[0]
        start_time= time.time()
        result = self.func(instance,*args[:1],**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Executed {self.func.__name__} in {execution_time:.4f} seconds")
        return result
    
class ExampleClass:
    @ClassLogger
    def example_method(self,x):
        time.sleep(1)
        return x * x
    
example = ExampleClass()
example.example_method(5)