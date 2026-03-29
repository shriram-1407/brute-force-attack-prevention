import time
from datetime import datetime

correct_password = "secure123"

attempts = 0
max_attempts = 5
time_window = 5
lock_time = 10

start_time = time.time()

while True:

    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted!")
        break

    else:
        attempts += 1
        print("Wrong password")

        current_time = time.time()
        elapsed_time = current_time - start_time

        if attempts >= max_attempts and elapsed_time <= time_window:

            print("⚠ Possible brute force attack detected")
            print(f"{attempts} attempts in {round(elapsed_time,2)} seconds")

            # logging the attack
            log_time = datetime.now()
            log = f"{log_time} | Brute force suspected | Attempts: {attempts} | Time: {round(elapsed_time,2)} seconds\n"

            file = open("security_log.txt", "a")
            file.write(log)
            file.close()

            print(f"System locked for {lock_time} seconds")
            time.sleep(lock_time)

            attempts = 0
            start_time = time.time()

        elif elapsed_time > time_window:
            attempts = 1
            start_time = time.time()