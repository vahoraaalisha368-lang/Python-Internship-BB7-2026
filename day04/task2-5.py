mode = "global"  

def outer():
    mode = "outer"  
    
    def inner():
        mode = "inner"  
        print(f"Inside inner: {mode}")  
    
    inner()
    print(f"Inside outer: {mode}")  

outer()
print(f"Outside: {mode}") 