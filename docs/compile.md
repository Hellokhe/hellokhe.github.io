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
brew install x86_64-elf-gcc x86_64-elf-binutils make ninja pkg-config curl tar python3 xorriso qemu
```

and hdiutil

**Linux:**
Install:

* x86_64-elf-gcc
* gcc or clang
* x86_64-elf-binutils
* make
* ninja
* pkg-config
* curl
* tar
* python3
* xorriso
* qemu-system-x86_64
* mtools
* gzip
* bzip2
* xz
* git
* patch
* flex
* bisom
* texinfo

**Windows:**

{: .hint } 
Use WSL!

That’s it. (Thank me for making it easy!)
