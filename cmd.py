import os
import sys
import platform
import psutil

while True:
    current_directory_path = os.getcwd()
    prompt_for_command = current_directory_path + "> "
    user_input = input(prompt_for_command)
    command_and_arguments = user_input.split()
    

    command = command_and_arguments[0]

    if "exit" == command:
        sys.exit()

    elif "dir" == command:
        current_directory_message = "Directory of " + current_directory_path
        print(current_directory_message)

        directory_entries = os.listdir(current_directory_path)
        for items in directory_entries:
            print(items)

    elif "mkdir" == command:
        path_of_directory_to_create = command_and_arguments[1]
        os.mkdir(path_of_directory_to_create)

    elif "cd" == command:
        path_of_directory_to_change_to = command_and_arguments[1]
        os.chdir(path_of_directory_to_change_to)

    elif "type" == command:
        path_of_file_to_print = command_and_arguments[1]
        with open(path_of_file_to_print) as file:
            file_contents = file.read()
            print(file_contents)

    elif "rmdir" == command:
        folder_to_delete = command_and_arguments[1]
        os.rmdir(folder_to_delete)
        print("Successfully deleted " + command_and_arguments[1] + ".")

    elif "rmfile" == command:
        file_to_delete = command_and_arguments[1]
        os.remove(file_to_delete)
        print("Successfully deleted " + command_and_arguments[1] + ".")
    
    elif "rename" == command:
        file_or_folder_to_rename = command_and_arguments[1]
        new_name = command_and_arguments[2]
        os.rename(file_or_folder_to_rename, new_name)
        print("File/folder successfully renamed")

    elif "systeminfo" == command:
        print(f"Computer network name: {platform.node()}")
        print(f"Machine type: {platform.machine()}")
        print(f"Processor type: {platform.processor()}")
        print(f"Platform type: {platform.platform()}")
        print(f"Operating system: {platform.system()}")
        print(f"Operating system release: {platform.release()}")
        print(f"Operating system version: {platform.version()}")
        
    elif "cpuinfo" == command:
        print(f"Number of phisical cores: {psutil.cpu_count(logical=False)}")
        print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
        print(f"Current CPU frequency: {psutil.cpu_freq().current}")
        print(f"Minimum CPU frequency: {psutil.cpu_freq().min}")
        print(f"Maximum CPU frequency: {psutil.cpu_freq().max}")
        print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
        print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1, percpu=True)}")

    elif "raminfo" == command:
        print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
        print(f"Available RAM: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
        print(f"Used RAM: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
        print(f"RAM usage: {psutil.virtual_memory().percent}%")
        

    
    else:
        unknown_command = "'" + command + "'" + " is not recognized as an internal or external command, operable program or batch file."
        print(unknown_command)
        
