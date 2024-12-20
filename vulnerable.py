# vulnerable_app.py

def insecure_function():
    # Hardcoded credentials (triggers secret detection)
    AWS_SECRET_KEY = "AKIA1234567890ABCDEF"
    DATABASE_PASSWORD = "super_secret_password123"
    
    # Dangerous function call (triggers SAST)
    exec(input("Enter command: "))
    
    # SQL Injection vulnerability (triggers SAST)
    query = "SELECT * FROM users WHERE id = " + user_input
    
    return "Done"
