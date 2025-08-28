# Podcast RSS Feed Generator

![GitHub Actions](https://github.com/bishwathakuri/podcast/workflows/Generate%20Podcast%20Feed/badge.svg)

A GitHub Action that automatically generates a podcast RSS feed (`podcast.xml`) from a YAML file (`feed.yml`) and updates it in your repository. This allows you to manage podcast content easily using YAML and publish updates via GitHub Pages.

---

## Features

- Convert a simple YAML file into a fully valid RSS feed for your podcast.
- Automatically commits and pushes updates to your repository.
- Works in a Docker container for consistent environments.
- Fully automated using GitHub Actions.

---

## Usage

### 1. Prepare Your Repository

- Add a `feed.yml` file in the root of your repository with your podcast episodes.

Example `feed.yml`:

```yaml
title: "My Awesome Podcast"
description: "A podcast about tech and programming."
link: "https://example.com"
episodes:
  - title: "Episode 1: Introduction"
    description: "Getting started with our podcast."
    pubDate: "2025-08-28"
    url: "https://example.com/episode1.mp3"
    length: 12345678
    type: "audio/mpeg"
  - title: "Episode 2: Advanced Topics"
    description: "Diving deeper into technology."
    pubDate: "2025-09-04"
    url: "https://example.com/episode2.mp3"
    length: 23456789
    type: "audio/mpeg"
```

### 2. Add GitHub Action

Create .github/workflows/main.yml:
```yaml
name: Generate Podcast Feed

on:
  push:
    paths:
      - 'feed.yml'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Run Podcast Feed Generator
        uses: <your-username>/<your-repo>@main
        with:
          name: ${{ github.actor }}
          email: ${{ github.actor }}@users.noreply.github.com
```

### 3. Docker Setup
- The action uses a Docker container:
- Python is installed in a virtual environment.
- Dependencies like PyYAML are installed inside the container.
- `feed.py` reads `feed.yml` and generates `podcast.xml`.

### 4. How It Works
- Action runs whenever `feed.yml` is updated.
- `feed.py` parses the YAML and generates `podcast.xml`.
- `entrypoint.sh` commits and pushes `podcast.xml` only if there are changes.

### 5. Inputs
| Input | Description       | Default                      |
|-------|-------------------|------------------------------|
| name  | Committer's name  | ${{ github.actor }}           |
| email | Committer's email | ${{ github.actor }}@localhost |

### 6. Outputs
Updates `podcast.xml` in the repository root.

### 7. License
This project is licensed under the [MIT License](LICENSE).