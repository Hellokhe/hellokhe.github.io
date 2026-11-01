#!/usr/bin/env python3
"""
scan.py - APT / Cydia Repository Generator for Hellokhe's iOS 7 Repository
Generates: Packages, Packages.gz, Packages.bz2, Packages.xz, and Release files
with proper MD5, SHA1, and SHA256 checksums.
"""

import os
import sys
import glob
import hashlib
import subprocess
import gzip
import bz2
import lzma
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DEBS_DIR = os.path.join(REPO_ROOT, "debs")
OUTPUT_PACKAGES = os.path.join(REPO_ROOT, "Packages")
OUTPUT_RELEASE = os.path.join(REPO_ROOT, "Release")

# Repository Metadata
REPO_ORIGIN = "Hellokhe Repo"
REPO_LABEL = "Hellokhe (iOS 7.x)"
REPO_SUITE = "stable"
REPO_VERSION = "1.0"
REPO_CODENAME = "ios7"
REPO_ARCHITECTURES = "iphoneos-arm"
REPO_COMPONENTS = "main"
REPO_DESCRIPTION = "Dedicated Cydia / APT repository for iOS 7.x devices. Hosts AppSync Unified, modern SSL fixes, and essential legacy tweaks."
BASE_URL = "https://hellokhe.github.io/repo"

def get_hashes(filepath):
    """Calculate MD5, SHA1, SHA256, and size for a file."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    size = os.path.getsize(filepath)

    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    return {
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest(),
        "size": size,
        "name": os.path.basename(filepath)
    }

def extract_control(deb_path):
    """Extract control file from deb using dpkg-deb or ar/tar fallback."""
    try:
        res = subprocess.run(
            ["dpkg-deb", "-f", deb_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return res.stdout.strip()
    except Exception as e:
        # Fallback using ar
        print(f"dpkg-deb failed for {deb_path}, trying ar fallback: {e}")
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            subprocess.run(["ar", "x", deb_path], cwd=tmpdir, check=True)
            control_tar = glob.glob(os.path.join(tmpdir, "control.tar*"))[0]
            subprocess.run(["tar", "-xf", control_tar, "./control"], cwd=tmpdir, check=True)
            with open(os.path.join(tmpdir, "control"), "r", errors="ignore") as f:
                return f.read().strip()

def build_package_entry(deb_file):
    deb_path = os.path.join(DEBS_DIR, deb_file)
    rel_path = f"debs/{deb_file}"
    control_text = extract_control(deb_path)
    hashes = get_hashes(deb_path)

    # Parse control fields into dict while maintaining order
    lines = control_text.splitlines()
    fields = {}
    current_key = None

    for line in lines:
        if line.startswith(" ") or line.startswith("\t"):
            if current_key:
                fields[current_key] += "\n" + line
        elif ":" in line:
            key, val = line.split(":", 1)
            current_key = key.strip()
            fields[current_key] = val.strip()

    pkg_id = fields.get("Package", "")

    # Ensure Depiction points to local depiction if one exists, or fallback to BASE_URL
    local_depiction = os.path.join(REPO_ROOT, "depictions", f"{pkg_id}.html")
    if os.path.exists(local_depiction):
        fields["Depiction"] = f"{BASE_URL}/depictions/{pkg_id}.html"
    elif not fields.get("Depiction"):
        fields["Depiction"] = f"{BASE_URL}/depictions/?p={pkg_id}"

    # Ensure Architecture is set for legacy iOS
    if "Architecture" not in fields:
        fields["Architecture"] = "iphoneos-arm"

    # Add Filename, Size, and Checksums
    fields["Filename"] = rel_path
    fields["Size"] = str(hashes["size"])
    fields["MD5sum"] = hashes["md5"]
    fields["SHA1"] = hashes["sha1"]
    fields["SHA256"] = hashes["sha256"]

    # Order priority fields first
    preferred_order = [
        "Package", "Name", "Version", "Architecture", "Maintainer", "Author",
        "Section", "Installed-Size", "Depends", "Pre-Depends", "Conflicts",
        "Provides", "Replaces", "Filename", "Size", "MD5sum", "SHA1", "SHA256",
        "Tag", "Homepage", "Depiction", "Description"
    ]

    out_lines = []
    seen = set()

    for k in preferred_order:
        if k in fields:
            val = fields[k]
            out_lines.append(f"{k}: {val}")
            seen.add(k)

    for k, val in fields.items():
        if k not in seen:
            out_lines.append(f"{k}: {val}")

    return "\n".join(out_lines)

def generate_repo():
    if not os.path.isdir(DEBS_DIR):
        print(f"Error: {DEBS_DIR} not found.")
        sys.exit(1)

    deb_files = sorted([f for f in os.listdir(DEBS_DIR) if f.endswith(".deb")])
    if not deb_files:
        print("No .deb files found in debs/")
        sys.exit(1)

    print(f"Found {len(deb_files)} deb packages in {DEBS_DIR}")

    package_entries = []
    for deb in deb_files:
        print(f" - Processing {deb}...")
        entry = build_package_entry(deb)
        package_entries.append(entry)

    packages_content = "\n\n".join(package_entries) + "\n"

    # 1. Write Packages (uncompressed)
    with open(OUTPUT_PACKAGES, "w", encoding="utf-8") as f:
        f.write(packages_content)
    print("✓ Wrote Packages")

    # 2. Write Packages.gz (gzip)
    with gzip.open(f"{OUTPUT_PACKAGES}.gz", "wb", compresslevel=9) as f:
        f.write(packages_content.encode("utf-8"))
    print("✓ Wrote Packages.gz")

    # 3. Write Packages.bz2 (bzip2) - MANDATORY for iOS 7 Cydia!
    with bz2.open(f"{OUTPUT_PACKAGES}.bz2", "wb", compresslevel=9) as f:
        f.write(packages_content.encode("utf-8"))
    print("✓ Wrote Packages.bz2 (iOS 7 Cydia Standard)")

    # 4. Write Packages.xz (lzma)
    with lzma.open(f"{OUTPUT_PACKAGES}.xz", "wb", preset=9) as f:
        f.write(packages_content.encode("utf-8"))
    print("✓ Wrote Packages.xz (Sileo/Zebra Modern)")

    # Calculate checksums for Release file
    pkg_files = [
        "Packages",
        "Packages.gz",
        "Packages.bz2",
        "Packages.xz"
    ]
    file_hashes = [get_hashes(os.path.join(REPO_ROOT, pf)) for pf in pkg_files]

    # Build Release file
    release_lines = [
        f"Origin: {REPO_ORIGIN}",
        f"Label: {REPO_LABEL}",
        f"Suite: {REPO_SUITE}",
        f"Version: {REPO_VERSION}",
        f"Codename: {REPO_CODENAME}",
        f"Architectures: {REPO_ARCHITECTURES}",
        f"Components: {REPO_COMPONENTS}",
        f"Description: {REPO_DESCRIPTION}",
        f"Date: {datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S UTC')}",
        "MD5Sum:"
    ]
    for h in file_hashes:
        release_lines.append(f" {h['md5']} {h['size']} {h['name']}")

    release_lines.append("SHA1:")
    for h in file_hashes:
        release_lines.append(f" {h['sha1']} {h['size']} {h['name']}")

    release_lines.append("SHA256:")
    for h in file_hashes:
        release_lines.append(f" {h['sha256']} {h['size']} {h['name']}")

    release_content = "\n".join(release_lines) + "\n"

    with open(OUTPUT_RELEASE, "w", encoding="utf-8") as f:
        f.write(release_content)
    print("✓ Wrote Release")

    print("\nRepo generation completed successfully!")

if __name__ == "__main__":
    generate_repo()
