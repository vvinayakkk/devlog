from typing import List, Dict, Any

def sort_dicts(
    dicts: List[Dict[str, Any]],
    key: str,
    reverse: bool = False,
    missing_last: bool = True
) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries by a specified key.
    
    Handles missing keys by separating dictionaries containing the key from those that do not,
    sorting the ones with the key, and placing the ones without the key either at the end
    or the beginning of the list based on `missing_last`.
    
    Args:
        dicts: The list of dictionaries to sort.
        key: The key to sort by.
        reverse: If True, sort in descending order (default is False).
        missing_last: If True, dictionaries missing the key are placed at the end.
                      If False, they are placed at the beginning.
                      
    Returns:
        A new list of sorted dictionaries.
    """
    with_key = []
    without_key = []
    
    for d in dicts:
        if key in d:
            with_key.append(d)
        else:
            without_key.append(d)
            
    sorted_with_key = sorted(with_key, key=lambda x: x[key], reverse=reverse)
    
    if missing_last:
        return sorted_with_key + without_key
    else:
        return without_key + sorted_with_key
