# Feishu Webhook Skill

A Claude Code skill for sending messages to Feishu (飞书/Lark) via Webhook.

## Overview

This skill enables Claude Code to send various types of messages to Feishu, including:

- Plain text messages
- Rich text (post) messages
- Interactive card messages
- Messages with images

## Installation

Add this skill to your Claude Code configuration:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/feishu-webhook-skill.git

# Add to your Claude Code skills directory
```

## Usage

Once installed, invoke the skill in Claude Code:

```
/feishu-webhook-skill
```

The skill will guide you through sending messages to Feishu webhooks.

## Features

### Message Types

- **Text**: Simple text messages
- **Rich Text (Post)**: Messages with formatting, links, mentions, images, and code blocks
- **Interactive Cards**: Complex card layouts with buttons, forms, and visualizations

### Image Upload

The `scripts/upload_image.py` tool allows you to upload images to Feishu:

```bash
# Install dependencies
pip install requests requests-toolbelt

# Upload an image
python scripts/upload_image.py ./image.png --token YOUR_TOKEN
```

Supported formats: JPG, JPEG, PNG, WEBP, GIF, BMP, ICO, TIFF, HEIC

## Documentation

- `SKILL.md` - Main skill definition and message content guide
- `webhook-card-common.md` - Card structure basics
- `webhook-card-content.md` - Card content components
- `webhook-card-container.md` - Card container components
- `webhook-card-visual.md` - Chart and visualization components
- `webhook-image.md` - Image handling guide

## Environment Variables

| Variable | Description |
|----------|-------------|
| `FEISHU_TENANT_ACCESS_TOKEN` | Feishu tenant access token for API calls |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Related Links

- [Feishu Open Platform](https://open.feishu.cn/)
- [Feishu Webhook Documentation](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot)
- [Claude Code](https://github.com/anthropics/claude-code)
