# GitHub App Configuration Reference

## Overview
This document provides guidance on configuring a GitHub App to work with this testing repository.

## App Permissions

### Repository Permissions
Configure these permissions in your GitHub App settings:

- **Contents**: Read (to access repository files)
- **Issues**: Read & Write (to create/update issues)
- **Pull requests**: Read & Write (to create/update PRs)
- **Metadata**: Read (automatically granted)

### Organization Permissions
Optional, depending on your use case:
- **Members**: Read (if you need to access organization membership)

## Webhook Configuration

### Webhook URL
Set this to your app's webhook endpoint, for example:
```
https://your-app.example.com/webhooks/github
```

For local development, use a service like ngrok:
```
https://abc123.ngrok.io/webhooks/github
```

### Webhook Secret
Generate a secure random string and configure it in both:
1. Your GitHub App settings
2. Your app's environment variables

Example generation:
```bash
ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'
```

### Subscribe to Events
Enable these webhook events for comprehensive testing:

#### Issues
- Issues opened
- Issues closed
- Issues edited
- Issues labeled

#### Pull Requests
- Pull request opened
- Pull request closed
- Pull request synchronize (new commits)
- Pull request review requested

#### Comments
- Issue comment created
- Issue comment edited
- Issue comment deleted
- Pull request review comment created

#### Repository
- Push (for commit events)
- Repository created/deleted

## Authentication

### Installation Token
Your app authenticates using installation access tokens. These are short-lived tokens that your app requests using:
1. Your app's private key (generated during app creation)
2. The installation ID (provided in webhook payloads)

### Example Flow
```
1. Receive webhook with installation ID
2. Generate JWT using your app's private key
3. Use JWT to request installation access token
4. Use installation token to make GitHub API calls
```

## Environment Variables

Recommended environment variables for your app:

```bash
GITHUB_APP_ID=123456
GITHUB_APP_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\n..."
GITHUB_WEBHOOK_SECRET=your_webhook_secret_here
```

## Testing Checklist

- [ ] App installed on test repository
- [ ] Webhook URL configured and reachable
- [ ] Webhook secret configured in both locations
- [ ] All required permissions granted
- [ ] Webhook events subscribed
- [ ] Test issue created successfully
- [ ] Webhook received and processed
- [ ] API calls working with installation token

## Useful API Endpoints

### Get Installation Token
```
POST /app/installations/{installation_id}/access_tokens
Headers: 
  Authorization: Bearer {JWT}
  Accept: application/vnd.github.v3+json
```

### Create Issue
```
POST /repos/{owner}/{repo}/issues
Headers:
  Authorization: token {installation_access_token}
  Accept: application/vnd.github.v3+json
Body:
  {
    "title": "Issue Title",
    "body": "Issue description"
  }
```

### Create Comment
```
POST /repos/{owner}/{repo}/issues/{issue_number}/comments
Headers:
  Authorization: token {installation_access_token}
  Accept: application/vnd.github.v3+json
Body:
  {
    "body": "Comment text"
  }
```

## Debugging

### Check Webhook Deliveries
In your GitHub App settings, you can view:
- Recent webhook deliveries
- Request/response payloads
- Delivery status codes
- Redeliver failed webhooks

### Common Issues

1. **403 Forbidden**: Missing or insufficient permissions
2. **404 Not Found**: Wrong installation ID or repository
3. **401 Unauthorized**: Invalid or expired token
4. **Webhook not received**: Check URL, firewall, or ngrok status

## Security Best Practices

1. ✅ Store private key securely (environment variable or secrets manager)
2. ✅ Validate webhook signatures using the webhook secret
3. ✅ Use HTTPS for all webhook endpoints
4. ✅ Request minimal required permissions
5. ✅ Rotate webhook secret periodically
6. ✅ Log webhook events for debugging
7. ✅ Handle rate limits gracefully

## Resources

- [GitHub Apps Documentation](https://docs.github.com/en/apps)
- [Authenticating as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app)
- [Webhook Events](https://docs.github.com/en/webhooks/webhook-events-and-payloads)
- [GitHub REST API](https://docs.github.com/en/rest)
