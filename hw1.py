"""
Aditya Sinha
Programming Assignment 1: A Barebones HTTP/1.1 Client
"""
#import logging
import socket
import sys


def retrieve_url(url):
    """
    return bytes of the body of the document at url
    """
    host_path = parse_url(url)

    if host_path is None:
        return None

    response = socket_communication(host_path)
    return response


def parse_url(url):
    """
    Parse the url and return list contains host, path, and port
    """
    parse_list = []
    url_length = len(url)

    if url.find("http://", 0, 7) != -1:
        parse_list = (url[7:url_length].split("/", 1))
        if len(parse_list) < 2 or parse_list[1] == "":
            path = "/"
        else:
            path = "/" + parse_list[1]
        split_port = parse_list[0].split(":", 1)
        host = split_port[0]
        if len(split_port) == 2:
            port = int(split_port[1])
        else:
            port = 80
        web_services = [host, path, port]
        return web_services
    elif url.find("https://", 0, 8) != -1:
        parse_list = (url[8:url_length].split("/", 1))
        if len(parse_list) < 2 or parse_list[1] == "":
            path = "/"
        else:
            path = "/" + parse_list[1]
        split_port = parse_list[0].split(":", 1)
        host = split_port[0]
        if len(split_port) == 2:
            port = int(split_port[1])
        else:
            port = 80
        web_services = [host, path, port]
        return web_services

    else:
        return None


def create_request(host_path):
    """
    Create an http request
    """
    request = ("GET " + host_path[1] +
               " HTTP/1.1\r\nHost:" + host_path[0] +
               "\r\nConnection: close\r\n\r\n")
    return request


def socket_communication(host_path):
    """
    Send request to server and returns the response body
    """
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysocket.connect((host_path[0], int(host_path[2])))
        request = create_request(host_path)
        mysocket.send(request.encode())
    except socket.error:
        return None

    data_packets = []
    while True:
        data = None
        try:
            data = mysocket.recv(4096)

            if data:
                data_packets.append(data)
                data = None
                continue
            else:
                break
        except socket.error:
            return None
    send_back = b"".join(data_packets)
    data = send_back
    if data.find(b"200 OK", 0, len(data)) != -1:
        new_data = data.split(b"\r\n\r\n", 1)
        return new_data[1]

if __name__ == "__main__":
    # pylint: disable=no-member
    sys.stdout.buffer.write(retrieve_url(sys.argv[1]))
