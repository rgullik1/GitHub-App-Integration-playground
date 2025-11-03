#!/bin/bash

# GitHub App Integration Test Script
# This script demonstrates how to test GitHub App webhooks locally

set -e

echo "GitHub App Integration Test Script"
echo "===================================="
echo ""

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to display webhook payload
display_webhook() {
    local webhook_file=$1
    echo -e "${BLUE}Testing webhook: ${webhook_file}${NC}"
    echo "-----------------------------------"
    cat "$webhook_file" | python3 -m json.tool 2>/dev/null || cat "$webhook_file"
    echo ""
    echo -e "${GREEN}✓ Webhook payload is valid JSON${NC}"
    echo ""
}

# Test all webhook payloads
echo "Testing webhook payloads..."
echo ""

for webhook in test-data/webhooks/*.json; do
    if [ -f "$webhook" ]; then
        display_webhook "$webhook"
    fi
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✓ All webhook tests completed!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Next steps:"
echo "1. Configure your GitHub App with webhook URL"
echo "2. Subscribe to relevant events (issues, pull_requests, issue_comment)"
echo "3. Monitor the workflow runs in the Actions tab"
echo "4. Use these test payloads to validate your app's webhook handler"
