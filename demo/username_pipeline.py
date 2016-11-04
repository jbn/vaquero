from vaquero.transformations import sstrip


def extract_username(src_d, dst_d):
    # Copy the user's name, then normalize it.
    dst_d['name'] = sstrip(src_d['user_name']).lower()

def _robust_int(s):
    # Try to convert s into an int.
    try:
        return int(s)
    except ValueError:
        return int(float(s))

def extract_age(src_d, dst_d):
    # Extract the age as an int.
    dst_d['age'] = _robust_int(src_d['user_age'])
