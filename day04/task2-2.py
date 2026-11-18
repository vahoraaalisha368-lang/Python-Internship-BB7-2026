def make_greeting(language):
    def greet(name):
        if language == "hindi":
            print(f"Namaste, {name}")
        else:
            print(f"Hello, {name}")
    return greet

hindi_greet = make_greeting("hindi")
hindi_greet("Alisha")  

english_greet = make_greeting("english")
english_greet("Alisha") 