import time
from collections import defaultdict, Counter
from app import calculate_latency, process_entries, print_availability

def test_calculate_latency():
    # Example test for calculate_latency function
    url = "http://example.com"
    method = "GET"
    headers = {"User-Agent": "TestAgent"}
    body = {"key": "value"}

    latency = calculate_latency(url, method, headers, body)
    print(latency)
    assert latency is not None
    assert latency >= 0

def test_process_entries():
    # Example test for process_entries function
    file_path = "input.yaml"  # Create a test YAML file for testing
    url_dict = defaultdict(Counter)

    # Call the function
    result_url_dict = process_entries(file_path, url_dict)

    assert result_url_dict is not None
    assert isinstance(result_url_dict, defaultdict)


test_calculate_latency()
test_process_entries()