# modules/advanced_search.py

def advanced_filter(records, risk=None, classification=None):

    filtered = []

    for record in records:

        if risk and record.get("risk") != risk:
            continue

        if classification and record.get("classification") != classification:
            continue

        filtered.append(record)

    return filtered