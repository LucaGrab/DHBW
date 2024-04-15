def one_time_passwords(initial_value, num_passwords):
    passwords = []
    r = initial_value
    for _ in range(num_passwords):
        password = r
        passwords.append(password)
        r = (r ** 2) % 1000
    return passwords

initial_value = 769
num_passwords = 6

password_list = one_time_passwords(initial_value, num_passwords)
for i, password in enumerate(password_list):
    print(f"H{i+1}(r) = {password}")
