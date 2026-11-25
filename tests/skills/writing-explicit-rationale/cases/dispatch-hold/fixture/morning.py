TITLE = "Morning dispatch"


def include_in_morning(status, already_loaded):
    return already_loaded or status != "manual_hold"
