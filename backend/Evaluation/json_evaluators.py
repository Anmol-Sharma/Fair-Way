def is_structurally_matching(json1, json2):
    """
    Check if two JSON objects have the same structure (same keys and value types),
    regardless of the actual values.

    Args:
        json1: First JSON object (dict, list, or primitive)
        json2: Second JSON object (dict, list, or primitive)

    Returns:
        bool: True if structures match, False otherwise
    """
    # Check if both are dictionaries
    if isinstance(json1, dict) and isinstance(json2, dict):
        # Check if they have the same keys
        if set(json1.keys()) != set(json2.keys()):
            return False

        # Check each key-value pair recursively
        for key in json1:
            if not is_structurally_matching(json1[key], json2[key]):
                return False
        return True

    # Check if both are lists
    elif isinstance(json1, list) and isinstance(json2, list):
        # Check if they have the same length
        if len(json1) != len(json2):
            return False

        # If lists are empty, they match
        if len(json1) == 0:
            return True

        # For non-empty lists, we need to check if all items follow the same structure
        # This is tricky because list items can be in different order
        # For simplicity, we'll check if the first item's structure appears in all items

        # Get structure of first item in json1
        sample_item = json1[0]

        # Check if all items in both lists match the structure of the sample item
        for item1 in json1:
            if not is_structurally_matching(item1, sample_item):
                return False

        for item2 in json2:
            if not is_structurally_matching(item2, sample_item):
                return False

        return True

    # Check if they are the same primitive type
    else:
        return type(json1) == type(json2)


def is_exact_json_match(json1, json2):
    """
    Check if two JSON objects match exactly (same keys, types, and values).

    Args:
        json1: First JSON object (dict, list, or primitive)
        json2: Second JSON object (dict, list, or primitive)

    Returns:
        bool: True if they match exactly, False otherwise
    """
    # Check if both are dictionaries
    if isinstance(json1, dict) and isinstance(json2, dict):
        # Check if they have the same keys
        if set(json1.keys()) != set(json2.keys()):
            return False

        # Check each key-value pair recursively
        for key in json1:
            if not is_exact_json_match(json1[key], json2[key]):
                return False
        return True

    # Check if both are lists
    elif isinstance(json1, list) and isinstance(json2, list):
        # Check if they have the same length
        if len(json1) != len(json2):
            return False

        # For exact matching, order matters in JSON, so compare each position
        for i in range(len(json1)):
            if not is_exact_json_match(json1[i], json2[i]):
                return False
        return True

    # For primitives, use direct equality comparison
    else:
        return json1 == json2


# Example usage
if __name__ == "__main__":
    # Example 1: Structural match but not exact match
    json_a = {
        "name": "John",
        "age": 30,
        "address": {"city": "New York", "zip": 10001},
        "hobbies": ["reading", "swimming"],
    }

    json_b = {
        "name": "Jane",
        "age": 25,
        "address": {"city": "Boston", "zip": 20001},
        "hobbies": ["painting", "hiking"],
    }

    # Example 2: Different structure
    json_c = {
        "name": "John",
        "age": 30,
        "address": {"street": "Main St", "zip": 10001},  # Different key
        "hobbies": ["reading", "swimming"],
    }

    # Example 3: Exact match
    json_d = json_a.copy()

    print(
        "Structural match between A and B:", is_structurally_matching(json_a, json_b)
    )  # True
    print("Exact match between A and B:", is_exact_json_match(json_a, json_b))  # False

    print(
        "Structural match between A and C:", is_structurally_matching(json_a, json_c)
    )  # False
    print("Exact match between A and C:", is_exact_json_match(json_a, json_c))  # False

    print(
        "Structural match between A and D:", is_structurally_matching(json_a, json_d)
    )  # True
    print("Exact match between A and D:", is_exact_json_match(json_a, json_d))  # True
