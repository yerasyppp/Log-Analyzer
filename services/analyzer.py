def filter_logs_by_status(logs, status):
    return list(filter(lambda log: log.status == status, logs))


def count_log_statuses(logs):
    statuses = list(map(lambda log: log.status, logs))

    status_counts = {}
    for current_status in statuses:
        status_counts[current_status] = status_counts.get(current_status, 0) + 1

    return status_counts