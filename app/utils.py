def to_dict(obj):
    """
    Converts a MongoDB document object to a dictionary, converting ObjectId to string.
    """
    if '_id' in obj:
        obj['_id'] = str(obj['_id'])
    return obj
