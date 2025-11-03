#!/usr/bin/env python3
"""
Example GitHub App Integration Script

This script demonstrates how to interact with GitHub's API
in the context of a GitHub App integration test.
"""

import json
import os
from pathlib import Path


def load_webhook_payload(payload_file):
    """Load a webhook payload from the test data directory."""
    payload_path = Path(__file__).parent.parent / "test-data" / "webhooks" / payload_file
    with open(payload_path, 'r') as f:
        return json.load(f)


def display_payload_info(payload):
    """Display key information from a webhook payload."""
    print(f"Action: {payload.get('action', 'N/A')}")
    print(f"Repository: {payload.get('repository', {}).get('full_name', 'N/A')}")
    
    if 'installation' in payload:
        print(f"Installation ID: {payload['installation']['id']}")
    
    # Display specific information based on payload type
    if 'issue' in payload:
        issue = payload['issue']
        print(f"Issue #{issue.get('number', 'N/A')}: {issue.get('title', 'N/A')}")
    
    if 'pull_request' in payload:
        pr = payload['pull_request']
        print(f"PR #{pr.get('number', 'N/A')}: {pr.get('title', 'N/A')}")
        print(f"  From: {pr.get('head', {}).get('ref', 'N/A')}")
        print(f"  To: {pr.get('base', {}).get('ref', 'N/A')}")
    
    if 'comment' in payload:
        comment = payload['comment']
        print(f"Comment ID: {comment.get('id', 'N/A')}")
        print(f"Body: {comment.get('body', 'N/A')}")


def main():
    """Main function to demonstrate webhook payload processing."""
    print("GitHub App Integration - Webhook Payload Processor")
    print("=" * 60)
    print()
    
    # List of available webhook payloads
    webhook_files = [
        "issue-opened.json",
        "pull-request-opened.json",
        "issue-comment-created.json"
    ]
    
    for webhook_file in webhook_files:
        print(f"\nProcessing: {webhook_file}")
        print("-" * 60)
        
        try:
            payload = load_webhook_payload(webhook_file)
            display_payload_info(payload)
        except FileNotFoundError:
            print(f"Error: Could not find {webhook_file}")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {webhook_file}")
        
        print()
    
    print("=" * 60)
    print("✓ Webhook payload processing complete!")
    print()
    print("Next steps:")
    print("1. Use these payloads to test your GitHub App webhook handler")
    print("2. Implement your app logic based on different event types")
    print("3. Test authentication with GitHub App installation tokens")


if __name__ == "__main__":
    main()

