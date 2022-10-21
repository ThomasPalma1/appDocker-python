from subprocess import check_output


def getting_ip():
    ips = check_output(['hostname', '--all-ip-addresses'])

    return ips.decode('utf-8').split(' ')[0]  # converting bytes to string
    # and taking the first position, which is the correct ip


getting_ip()
