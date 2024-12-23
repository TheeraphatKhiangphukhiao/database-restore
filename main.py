import os
import subprocess

path = 'D:\\Database\\1204205 - Database Design and Management'
dbname = ''

mysql_user = 'root'
mysql_password = 'digix02mci@theeraphat'
mysql_path = ''

file_paths = []

for file in os.listdir(path):
    file_paths.append(
        os.path.join(path, file)
    )

for file_path in file_paths:
    # print(file_path)

    command = [
        mysql_path,
        "-u", mysql_user,
        f"-p{mysql_password}",
        dbname
    ]

    try:
        with open(file_path, 'r') as file:
            subprocess.run(command,stdin=file,check=True)
        
        print("Database restore successfully.")
        print("in : ", file_path, "\n")
        print("-------------------------------------------")

    except subprocess.CalledProcessError as e:
        print(f"Error during restore: {e}")