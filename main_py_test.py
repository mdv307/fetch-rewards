import pytest
import time
from collections import defaultdict, Counter
from unittest.mock import patch, Mock
from app import calculate_latency, process_entries, print_availability

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch('your_module_name.requests.get')

@pytest.fixture
def mock_requests_post(mocker):
    return mocker.patch('your_module_name.requests.post')

def test_calculate_latency_get_success(mock_requests_get):
    mock_response = Mock(status_code=200)
    mock_response.elapsed.total_seconds.return_value = 0.5
    mock_requests_get.return_value = mock_response

    latency = calculate_latency("https://example.com", method="GET")
    assert latency == 0.5

def test_calculate_latency_get_failure(mock_requests_get):
    mock_response = Mock(status_code=404)
    mock_requests_get.return_value = mock_response

    latency = calculate_latency("https://example.com", method="GET")
    assert latency is None

def test_calculate_latency_post_success(mock_requests_post):
    mock_response = Mock(status_code=200)
    mock_response.elapsed.total_seconds.return_value = 0.7
    mock_requests_post.return_value = mock_response

    latency = calculate_latency("https://example.com", method="POST", headers={}, body={})
    assert latency == 0.7

def test_calculate_latency_post_failure(mock_requests_post):
    mock_response = Mock(status_code=404)
    mock_requests_post.return_value = mock_response

    latency = calculate_latency("https://example.com", method="POST", headers={}, body={})
    assert latency is None

def test_process_entries(mocker):
    mocker.patch('your_module_name.open', mocker.mock_open(read_data="""- url: https://example.com
      method: GET
      name: Example GET
    - url: https://example.com
      method: POST
      name: Example POST"""))
    mocker.patch('your_module_name.calculate_latency', side_effect=[0.2, 0.4])  # Latency values for the two requests

    url_dict = defaultdict(Counter)
    updated_url_dict = process_entries("input.yaml", url_dict)

    assert updated_url_dict["Example GET"] == Counter([0.2])
    assert updated_url_dict["Example POST"] == Counter([0.4])

def test_print_availability(capsys):
    url_dict = defaultdict(Counter)
    url_dict["Example GET"].update([0.1, 0.2, 0.6])
    url_dict["Example POST"].update([0.3, 0.4, 0.5])

    print_availability(url_dict)
    captured = capsys.readouterr()

    assert "Example GET has 66.67% availability" in captured.out
    assert "Example POST has 100.00% availability" in captured.out
