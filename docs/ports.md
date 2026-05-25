---
title: Ports System
nav_order: 6
---

# Ports System

ZenOS can build real userspace software.

## Setup
```
make ports-sysroot
make ports-env
```

## Features

- musl libc,
- X11 libraries,
- pixman rendering.

## X11 Support

Run ``x11-desktop`` in the ZenOS terminal, or choose **X11 / twm** in the the dropdown. The dropdown is located on the bottom-left corner. It's only visible in the login screen.

## Status

- X11 apps: yes (i luv xeyes)
- TWM: yes
- Runtime integration: eh idk i havent checked lol