def to_ini_value(v):
    """
    Provide a string or a Python built-in list or dict.

    Variables may be complex built-in data structures, so format the
    value to a string to determine if it contains a valid data
    structure.

    This will default `v` to an _empty_ string. It does so to be
    functionality equivalent with the Jinja2 filter approach:

        {{ v | default('')}}

    Custom Filter Plugin:
      This can be used from within a Jinja2 template file
    """

    # default to an empty string
    if v is None:
        v = ''

    strVal = str(v)
    if ('[' in strVal or '{' in strVal) and '__' not in strVal:
        return v
    else:
        return "\"%s\"" % (v,)


class FilterModule(object):
    """
    Utility filters for formating values in INI files
    """

    def filters(self):
        return {
            'to_ini_value': to_ini_value
        }