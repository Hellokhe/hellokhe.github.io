---
title: Web Browser
nav_order: 2
layout: default
---

# Web Browser

ZenOS includes support for **NetSurf v3.11**, a lightweight, standards-compliant web browser. 

## Features
- HTTP/HTTPS networking (via curl + OpenSSL)
- PNG and JPEG image rendering
- Full HTML5/CSS3 support
- Statically linked for maximum compatibility (only 838 KB!)

## What Works
- Local file browsing
- Simple websites without JavaScript (e.g., Wikipedia articles, news sites, blogs)
- Image-heavy pages

*Note: JavaScript execution and dynamic content/form submissions are not currently supported.*

## Usage
Launch from the terminal:
```bash
netsurf
netsurf http://example.com
```
