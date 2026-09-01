def smoke_status(name, passed):
    name = name.strip()
    return f"{name}: {'PASS' if passed else 'FAIL'}"
