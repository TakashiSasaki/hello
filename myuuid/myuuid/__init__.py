import uuid
MY_NAMESPACE_UUID = uuid.UUID('c8ee7542-57d0-4fb3-880a-739391e7c131')
print('MY_NAMESPACE_UUID', MY_NAMESPACE_UUID)

def get_new_uuidv5(name):
    return uuid.uuid5(MY_NAMESPACE_UUID, name)