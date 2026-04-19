def create_response(Data):
    return{
        "status":"success",
        "Data":Data
    }

print(create_response("User Created"))
#{'status': 'success', 'Data': 'User Created'}