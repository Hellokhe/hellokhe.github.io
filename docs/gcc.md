# Compiler Commands

ZenOS provides basic compiler command interfaces for building C/C++ programs and system code.

---

## cc

`cc` is the default C compiler command.

It typically points to GCC in ZenOS:

```bash
cc file.c -o output.elf
```

Used for:

* Simple C compilation
* System builds
* Default compiler entry point

---

## gcc

`gcc` is the GNU C Compiler frontend.

```bash
gcc file.c -o output.elf
```

Used for:

* Full control over compilation
* Kernel and low-level builds
* Cross-compiling in ZenOS toolchain

Common flags:

```bash
gcc -ffreestanding -mno-red-zone -nostdlib
```

---

## tcc

`tcc` (Tiny C Compiler) is a lightweight compiler.

```bash
tcc file.c -o output.elf
```

Used for:

* Fast compilation
* Testing small programs
* Simple scripts

---

## cpp

`cpp` is the C preprocessor.

```bash
cpp file.c
```

Used for:

* Macro expansion
* Header inclusion processing
* Debugging preprocessed output
