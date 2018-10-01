#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as en:
        print("Exception: {:s}".format(str(en)), file=sys.stderr)
        return False
