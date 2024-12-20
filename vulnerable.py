# vulnerable_app.py
def insecure_function():
    password = "hard_coded_password123"  # Dit zal de secrets check triggeren
    exec(input("Enter command: "))  # Dit zal de SAST scan triggeren