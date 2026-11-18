def outer():
    status = "pending"
    
    def inner():
        nonlocal status
        status = "completed"
    
    inner()
    print(f"Final status: {status}")

outer()