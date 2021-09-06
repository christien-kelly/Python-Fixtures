import data.data as dt

def main(data):
    """
    This function does some small mutations to 
    an input datafile. 
    
    Args: 
        data - a json dict
        
    Returns a modified dictionary
    """
    assert isinstance(data, dict), AssertionError("Wrong Type!")

    data['age'] += 3
    data['height'] += 10

    return data

if __name__ == '__main__':
    
    modified_data = []
    
    for item in dt.data:
        temp_result = main(item)
        modified_data.append(temp_result)
    
    print(modified_data)