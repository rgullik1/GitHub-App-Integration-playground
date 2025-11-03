# GitHub App Integration Playground

A comprehensive testing environment for GitHub App integration, webhooks, and workflows.

## 🚀 Quick Start

This repository provides everything you need to test GitHub App integrations:

- **Automated Workflows**: Pre-configured GitHub Actions that respond to various events
- **Sample Webhooks**: Ready-to-use webhook payload examples
- **Test Scripts**: Tools to validate webhook structures locally
- **Documentation**: Complete guide for testing GitHub Apps

## 📁 Repository Structure

```
├── .github/workflows/          # GitHub Actions workflows
│   └── github-app-test.yml    # Main integration test workflow
├── test-data/webhooks/        # Sample webhook payloads
│   ├── issue-opened.json
│   ├── pull-request-opened.json
│   └── issue-comment-created.json
├── scripts/                   # Test utilities
│   └── test-webhooks.sh      # Webhook validation script
├── TESTING_GUIDE.md          # Detailed testing documentation
└── README.md                 # This file
```

## 🧪 Testing Your GitHub App

1. **Install your GitHub App** on this repository
2. **Configure webhooks** for events you want to test
3. **Trigger events** by creating issues, PRs, or comments
4. **Monitor workflow runs** in the Actions tab
5. **Review event payloads** in the workflow logs

## 📖 Documentation

See [TESTING_GUIDE.md](TESTING_GUIDE.md) for comprehensive instructions on:
- Setting up GitHub Apps
- Configuring webhooks
- Testing different event types
- Debugging common issues

## 🔧 Quick Test

Run the webhook validation script:
```bash
./scripts/test-webhooks.sh
```

## ✨ Features

- ✅ Multiple webhook event examples
- ✅ Automated workflow triggers
- ✅ Event payload inspection
- ✅ Local testing capabilities
- ✅ Comprehensive documentation

## 🤝 Contributing

Add more test cases, webhook examples, or improve documentation by submitting a PR!

## 📚 Resources

- [GitHub Apps Documentation](https://docs.github.com/en/apps)
- [Webhook Events](https://docs.github.com/en/webhooks)
- [GitHub Actions](https://docs.github.com/en/actions)
