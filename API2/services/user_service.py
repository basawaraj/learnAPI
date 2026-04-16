def get_user_data(name):
    return {
        "user-name": name,
        "role": "admin"
    }

def search_data(query):
    data={
        "query": query,
        "results":[1,2,3,4]
    }
    return data