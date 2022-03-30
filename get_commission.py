from datetime import date


def get_commission(date_str: str) -> float:
    """Takes date string and returns commission value

    Args:
        date_str: date string in the format 'YYYY-MM-DD'.

    Returns:
        Value of commission based on current date.

    Raises:
        ValueError: If `date_str` has wrong date format.
    """
    commission_table = {1: 0.1,
                        2: 0.1,
                        3: 0.1,
                        4: 0.1,
                        5: 0.1,
                        6: 0.15,
                        7: 0.15,
                        8: 0.15,
                        9: 0.15,
                        10: 0.1,
                        11: 0.1,
                        12: 0.1,
                        }
    date_parsed = date.fromisoformat(date_str.strip())
    return commission_table[date_parsed.month]
