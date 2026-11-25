def _quota_units(value):
    # The billing feed sometimes sends negative corrections. They cannot
    # authorize extra work, so the admission service treats them as zero.
    return max(0, value)


def _format_units(value):
    return f"{value} units"


def show_limit(value):
    return _format_units(_quota_units(value))


def available_units(value, consumed):
    return max(0, _quota_units(value) - consumed)
