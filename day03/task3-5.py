default_settings = {"theme": "light", "notifications": True, "volume": 50, "auto_save": False}
user_settings = {"theme": "dark", "volume": 80}

combined_settings = {**default_settings, **user_settings}

print("Final Combined Settings:")
print(combined_settings)