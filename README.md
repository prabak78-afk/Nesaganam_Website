# Nesaganam_Website

Nesaganam is a Tamil online radio website for listening to live music, discovering videos, and supporting the station.

## Features

- 24/7 online Tamil radio player
- Play and pause controls with volume adjustment
- Responsive design for desktop and mobile
- YouTube channel page with featured videos
- Donation page with UPI details and QR code
- Google Play app link
- Nesaganam photo gallery
- Links to Instagram, Facebook, and YouTube
- Tamil-language content and typography support

## Pages

- [Live Radio](index.html) - Listen to the Nesaganam online stream.
- [YouTube](youtube.html) - Watch featured Nesaganam videos and visit the channel.
- [Donate](donate.html) - Support Nesaganam using the displayed UPI details or QR code.
- Automatic YouTube upload updates through GitHub Actions

## Project Structure

```text
.
├── index.html          # Main radio website
├── youtube.html        # YouTube videos and channel links
├── donate.html         # Donation information
├── logo 512.png        # Nesaganam logo
├── donate qrcode.jpg   # Donation QR code
├── Gallery/            # Website gallery images
├── .github/workflows/  # Automation for updating videos.json
├── scripts/            # YouTube data fetch script
├── videos.json         # Cached channel feed used by the site
├── CNAME               # Custom domain for GitHub Pages
├── LICENSE.txt         # Copyright notice
├── README.md           # Project overview
└── .vscode/            # Editor settings
```

## Automatic YouTube Videos

The YouTube page reads `videos.json`, which is generated from the channel's public feed by
`.github/workflows/update-videos.yml` every 15 minutes. The workflow can also be started
manually from the repository's **Actions** tab.

For automatic updates, enable **Settings > Actions > General > Workflow permissions > Read and
write permissions** in the GitHub repository, then run **Update YouTube videos** once. Publish the
repository with GitHub Pages so the page and `videos.json` share the same origin.

## Run Locally

This is a static HTML website and does not require a build step.

1. Clone or download the repository.
2. Open `index.html` in a browser, or serve the folder with a local web server.

For example, with Python:

```bash
python -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000).

## External Services

The website uses:

- Google Fonts
- FastCast4u for the live radio stream
- YouTube embeds and channel links
- Google Play for the Android app link

An internet connection is required for the live stream, external fonts, embedded videos, and app badge.

## Social Links

- [YouTube](https://www.youtube.com/@nesaganamchannel)
- [Instagram](https://www.instagram.com/arputha.raja.9235/)
- [Facebook](https://www.facebook.com/nesammedia)

## License

This project uses a **proprietary, all-rights-reserved license**. The original
source code, branding, photographs, artwork, text, and other project assets
may not be copied, modified, redistributed, or reused without prior written
permission from Nesam Media / Nesaganam.

Third-party materials, including embedded or linked media, fonts, streams, and
platform assets, are excluded and remain governed by their respective owners'
terms. See [LICENSE.txt](LICENSE.txt) for the complete notice.
