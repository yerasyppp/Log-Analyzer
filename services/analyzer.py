def filter_logs_by_status(logs, status):
    """
    Filters a list of log entries by their status.
    Uses filter() and a lambda function for efficiency.
    """
    return list(filter(lambda log: log.status == status, logs))


def count_log_statuses(logs):
    """
    Counts the occurrences of each log status in the provided logs list.
    Uses map() to extract the statuses.
    """
    statuses = list(map(lambda log: log.status, logs))

    status_counts = {}
    for current_status in statuses:
        status_counts[current_status] = status_counts.get(current_status, 0) + 1

    return status_counts