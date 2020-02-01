def reorderDataLogFiles(logs):
    digits = []
    letters = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # when suffix is tie, sort by identifier
    letters.sort(key=lambda x: x.split()[0])
    # sort by suffix
    letters.sort(key=lambda x: x.split()[1:])

    # put digits after logs
    return letters + digits
