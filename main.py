import requests
import time
import yaml
from collections import defaultdict, Counter

def calculate_latency(url, method="GET", headers=None, body=None):
    """
    Calculate latency for an HTTP request.

    Args:
        url (str): The URL for the HTTP request.
        method (str): The HTTP method (GET or POST).
        headers (dict): Headers for the request.
        body (dict): JSON body for POST requests.

    Returns:
        float or None: Latency of the request or None if unsuccessful.
    """
    start_time = time.time()
    try:
        if method.upper() == "GET" or method is None:
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, json=body)
        else:
            raise ValueError("Invalid HTTP method")

        latency = time.time() - start_time
        return latency if response.status_code == 200 else None

    except requests.RequestException:
        return None

def process_entries(file_path, url_dict):
    """
    Process entries from a YAML file and update the url_dict with latencies.

    Args:
        file_path (str): Path to the YAML file.
        url_dict (defaultdict): Dictionary to store latencies for each URL.

    Returns:
        defaultdict: Updated url_dict.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        for entry in data:
            url = entry.get('url')
            headers = entry.get('headers', {})
            method = entry.get('method', 'GET')
            name = str(entry.get('name', '')).split()[0]
            body = entry.get('body')

            latency = calculate_latency(url, method, headers, body)
            url_dict[name].update([latency])

    return url_dict

def print_availability(url_dict):
    """
    Print the availability percentage for each URL.

    Args:
        url_dict (defaultdict): Dictionary containing latencies for each URL.
    """
    for name, latencies in url_dict.items():
        total_requests = len(latencies)
        successful_requests = sum(1 for latency in latencies if latency is not None and latency <= 0.5)
        availability_percentage = (successful_requests / total_requests) * 100 if total_requests > 0 else 0
        print(f"{name} has {availability_percentage:.2f}% availability")

if __name__ == "__main__":
    file_path = "input.yaml"

    # Using defaultdict and Counter for efficient counting
    url_dict = defaultdict(Counter)

    while True:
        url_dict = process_entries(file_path, url_dict)
        print_availability(url_dict)
        time.sleep(15)
