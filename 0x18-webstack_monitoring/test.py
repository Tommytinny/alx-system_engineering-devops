"""
Get the total number of active hosts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="420922-web-01"
    )

    print(response)

