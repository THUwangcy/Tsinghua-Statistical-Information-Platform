import hashlib


def md5encode(act_id):
    m = hashlib.md5()
    m.update(act_id)
    return m.hexdigest()
