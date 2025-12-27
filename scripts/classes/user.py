import output

USER_FILE_PATH = "scripts/files/users.txt"
    
def test_for_user_file(file_path:str = USER_FILE_PATH):
    try:
        f= open(file_path, 'r')
    except:
        return False
    f.close()
    return True

def create_user_file(file_path: str= USER_FILE_PATH):
    if not test_for_user_file():
        f= open(file_path,'w')
        f.close
        return True
    else:
        print(f"User file found at {file_path}. No new file was created")
        return False
    
def load_user_file_to_memory(file_path: str= USER_FILE_PATH)-> dict:
    if test_for_user_file():
        with open(file_path,'r') as user_f:
            user_file_list = user_f.readlines
    else:
        create_user_file()
        user_file_list=[]
    user_dict = {}
    for user in user_file_list:
        user_list = user.split('|')
        user_dict[user_list[0]] = user_list[1:]
    return user_dict

def write_to_user_file(user_id:str, user_data:list, file_path: str= USER_FILE_PATH):
    successfully_wrote = False
    all_users = load_user_file_to_memory()
    all_users[user_id] = user_data
    with open(file_path,'w') as user_f:
        user_f = all_users
    successfully_wrote = True
    return True

class User():
    def __init__(self, user_id: str|None=None, refernce_name: str|None = None):
        while user_id is None:
            output.output("Enter a userid that you would like to be your unique identfier")
            requested_user_id = input("")
            all_ids = load_user_file_to_memory()
            if requested_user_id not in all_ids:
                all_ids[user_id] = []
                user_id = requested_user_id
                write_to_user_file()
            else:
                output.output("The username you selected is already in use. If that is you, you " \
                "can use it. If not, try with a different ID")
        


    def create_user(self, name: str|None = None):
        if name is None:
            user_name = input("Enter a name for your user")

    create_user_file(USER_FILE_PATH)
    def check_user_file_for_me(self, user_dict):
        raise NotImplementedError

if __name__ == "__main__":
    pass