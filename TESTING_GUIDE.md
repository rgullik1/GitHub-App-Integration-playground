# GitHub App Integration Testing Guide

This repository provides a comprehensive testing environment for GitHub App integration.

## Overview

This repo is designed to help you test GitHub App webhooks, workflows, and integrations in a controlled environment.

## Contents

### 1. GitHub Actions Workflow
- **Location**: `.github/workflows/github-app-test.yml`
- **Purpose**: Demonstrates how GitHub Apps can trigger and interact with workflows
- **Triggers**: Push, Pull Request, Issues, Issue Comments, Manual dispatch

### 2. Sample Webhook Payloads
- **Location**: `test-data/webhooks/`
- **Files**:
  - `issue-opened.json` - Sample payload for issue opened event
  - `pull-request-opened.json` - Sample payload for PR opened event
  - `issue-comment-created.json` - Sample payload for comment created event

### 3. Test Scripts
- **Location**: `scripts/test-webhooks.sh`
- **Purpose**: Validates webhook payload JSON structure locally

## How to Test GitHub Apps

### Prerequisites
1. A GitHub App created in your account or organization
2. Appropriate permissions configured for your app
3. Webhook URL configured (or use this repo for testing triggers)

### Testing Steps

#### 1. Install Your GitHub App
Install your GitHub App on this repository through the GitHub App settings.

#### 2. Configure Webhooks
Subscribe to the following events in your GitHub App settings:
- Issues
- Pull requests
- Issue comments
- Push events

#### 3. Trigger Events
You can trigger events in several ways:
- Create an issue
- Create a pull request
- Comment on an issue
- Push code to the repository
- Manually trigger the workflow from the Actions tab

#### 4. Monitor Workflow Runs
1. Go to the "Actions" tab in this repository
2. Click on "GitHub App Integration Test" workflow
3. View the latest runs to see how your app interacts with the workflow

#### 5. Test Webhooks Locally
Run the test script to validate webhook payloads:
```bash
./scripts/test-webhooks.sh
```

## Webhook Payload Structure

Each webhook payload contains:
- `action`: The type of action that triggered the webhook
- `repository`: Information about this repository
- `installation`: GitHub App installation details
- Event-specific data (issue, pull_request, comment, etc.)

## Example: Testing Issue Creation

1. Create an issue in this repository
2. Your GitHub App will receive a webhook with the `issues` event
3. The workflow will be triggered automatically
4. Check the workflow run to see the event payload
5. Your app can process the webhook and take appropriate actions

## Debugging Tips

### View Event Payloads
The workflow automatically displays the complete event payload. Check the workflow logs to see:
- Event name
- Repository information
- Actor (user or bot)
- Complete JSON payload

### Common Issues
1. **Webhook not received**: Check app permissions and webhook URL
2. **Workflow not triggered**: Verify the event is configured in the workflow file
3. **Authentication errors**: Ensure your app has a valid installation token

## GitHub App Permissions

For full testing, your GitHub App should have these permissions:
- **Issues**: Read & Write
- **Pull requests**: Read & Write
- **Contents**: Read
- **Metadata**: Read (automatically granted)

## API Testing

You can use these webhook payloads to test your app's API endpoints locally:
```bash
curl -X POST http://localhost:3000/webhook \
  -H "Content-Type: application/json" \
  -d @test-data/webhooks/issue-opened.json
```

## Resources

- [GitHub Apps Documentation](https://docs.github.com/en/apps)
- [Webhook Events and Payloads](https://docs.github.com/en/webhooks/webhook-events-and-payloads)
- [Building GitHub Apps](https://docs.github.com/en/apps/creating-github-apps)

## Contributing

Feel free to add more webhook examples or test scenarios by:
1. Adding new payload files to `test-data/webhooks/`
2. Extending the workflow with additional test cases
3. Creating new test scripts

## License

This is a testing playground - use it freely for testing your GitHub Apps!
