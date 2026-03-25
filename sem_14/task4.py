def breach_attempts(hackers, security_level, increase):
    count = 0

    for hacker in hackers:
        if hacker > security_level:
            count += 1
        else:
            security_level += increase

    return count
