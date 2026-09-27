---
title: Hardware & Input
nav_order: 4
layout: default
---

# Hardware & Input

ZenOS boots directly on x86-64 hardware or in QEMU, offering simple but reliable hardware support.

## Supported Devices
- **Bootloader**: Uses the Limine bootloader to seamlessly boot the 64-bit kernel.
- **Input**: Standard PS/2 keyboard and mouse drivers are fully implemented and working in the graphical desktop environments.

*Note: USB peripherals, trackpads, and sound do not currently work natively on bare metal hardware yet.*
