#!/usr/bin/env python3
"""Unit tests for client module."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import (org_payload, repos_payload,
                      expected_repos, apache2_repos)

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @parameterized.expand([
        ("google", org_payload),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test GithubOrgClient.org method."""
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url property."""
        mock_org.return_value = org_payload
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, org_payload["repos_url"])
        mock_org.assert_called_once()

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        mock_public_repos_url.return_value \
            = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = repos_payload

        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), repos_payload)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)

@parameterized_class((
        'org_payload', 'repos_payload',
        'expected_repos', 'apache2_repos'
), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up class method."""
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method."""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mocked requests.get method."""
        if url == "https://api.github.com/orgs/google":
            return Mock(ok=True, json=lambda: org_payload)
        elif url == "https://api.github.com/orgs/google/repos":
            return Mock(ok=True, json=lambda: repos_payload)
        return Mock(ok=False)

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), repos_payload)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos method with license."""
        client = GithubOrgClient("google")
        self.assertEqual(
            [repo for repo in client.public_repos()
             if client.has_license(repo, "apache-2.0")],
            apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
