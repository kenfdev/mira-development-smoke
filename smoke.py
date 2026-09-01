def smoke_status(name, passed):
    return f"{name}: {'PASS' if passed else 'FAIL'}"
