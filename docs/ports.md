---
title: Ports System
nav_order: 6
---

# Ports System

ZenOS can build real userspace software.

## Setup
``zash
make ports-sysroot
make ports-env
``

## Features

- musl libc,
- X11 libraries,
- pixman rendering.

## X11 Support

``zash
x11-desktop
``

## Status

- X11 apps: yes (kind of)
- TWM: yes
- Runtime integration: WIP