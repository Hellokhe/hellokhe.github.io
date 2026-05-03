---
title: Architecture
nav_order: 2
---

# Architecture

ZenOS runs with privilege separation:

- **Ring 0** → Kernel
- **Ring 3** → Userspace apps

## Userspace

- ELF64 loader
- X11 applications
- TWM window manager

## Status

- Ring 3: yea
- ELF: yep
- X11: yes
- Full syscall layer: idk