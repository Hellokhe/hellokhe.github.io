---
title: Compiling
nav_order: 4
---

# Compiling zenOS

Compiling zenOS is simple. The project uses a Makefile, so all you need to do is:

```bash
git clone (ZenOS hasn't been published yet!)
cd zenOS
make run
```

# Requirements

**macOS:**

```bash
brew install x86_64-elf-gcc xorriso qemu
```

**Linux:**
Install:

* gcc or x86_64-elf-gcc
* xorriso
* qemu-system-x86

**Windows:**

{: .warning } 
Hint: Use WSL!

That’s it. (Thank me for making it easy!)