# Hellokhe iOS 7.x Cydia / APT Repository 🍏

A dedicated Cydia / APT package repository configured specifically for jailbroken **iOS 7.0 &ndash; 7.1.2** devices, hosted via GitHub Pages for **Hellokhe**.

Featuring **AppSync Unified** for installing unsigned and fakesigned IPAs without expiration or revokes, plus essential iOS 7 fixes including the **ISRG Root X1 Modern SSL CA Fix**, **Checkmate, Store!**, and legacy system enhancements.

---

## 🚀 Live Repository URL

To add this repository to your jailbroken iOS 7 device:

```text
https://hellokhe.github.io/
```

> **Note for iOS 7 Devices:** Modern HTTPS certificates require the modern Let's Encrypt ISRG Root X1 certificate. If you see SSL handshake or timeout errors when adding via HTTPS, tap **"Install ISRG Root X1 Profile"** on the website homepage, or add via plain HTTP:
> ```text
> http://hellokhe.github.io/
> ```

---

## 📦 Hosted iOS 7 Packages

| Package Name | Version | Identifier | Description |
| :--- | :--- | :--- | :--- |
| **AppSync Unified** | `116.2` | `ai.akemi.appsyncunified` | Allows installing unsigned, fakesigned, or ad-hoc signed IPAs on iOS 7 without revokes. |
| **appinst** | `2.1.1` | `ai.akemi.appinst` | Command-line IPA installer for MobileTerminal and SSH. |
| **ISRG Root X1 CA Fix** | `1.0.0` | `com.hellokhe.isrgrootx1` | Fixes Cydia and Safari HTTPS/SSL errors on iOS 7. |
| **Checkmate, Store!** | `1.2` | `uk.invoxiplaygames.checkmatestore` | Bypasses capability checks in App Store to download last compatible app versions. |
| **PreferenceLoader** | `2.2.6` | `preferenceloader` | Enables tweak settings panes in iOS Settings.app. |
| **SwipeSelection** | `1.5.2-1` | `com.iky1e.swipeselection` | Swipe across keyboard to move cursor &amp; select text. |
| **iFile Crash Fix** | `1.0` | `com.parrotgeek.ifilefix` | Fixes startup crash when opening iFile on iOS 7. |
| **Jailbreak App Icons Fix** | `1.0.0` | `com.lukezgd.iconsfix` | Restores missing Cydia icons on SpringBoard. |
| **Cydia Webview Modifier** | `1.0` | `com.lukezgd.cydiawebviewmodifier` | Fixes URL loading and rendering inside Cydia webviews. |

---

## ⚡️ AppSync Unified on iOS 7

AppSync Unified patches `installd` to permit unsigned IPA installation.

### How to use AppSync Unified once installed:
1. Install **AppSync Unified** from Cydia (or download the `.deb` from `debs/ai.akemi.appsyncunified_116.2_iphoneos-arm.deb`).
2. **Reboot or respring** your device once to ensure MobileSubstrate attaches to `installd`.
3. Sideload IPAs using any of these methods:
   - **Method 1 (Desktop USB):** Connect to PC/Mac and use **iFunBox** or **3uTools** &rarr; *Install App (.ipa)*.
   - **Method 2 (CLI on device):** In MobileTerminal or SSH, run:
     ```bash
     appinst /var/mobile/Downloads/YourApp.ipa
     ```
   - **Method 3 (iFile / Filza):** Open any `.ipa` in iFile/Filza and tap *Installer*.

---

## 🛠️ Repository Structure

```text
hellokhe-ios7-repo/
├── .nojekyll                 # Ensures GitHub Pages serves raw files without Jekyll processing
├── CydiaIcon.png             # 128x128 Cydia repository icon
├── index.html                # iOS 7 styled website landing page & package browser
├── isrgrootx1.mobileconfig   # Apple Configuration Profile for 1-click SSL fix
├── isrgrootx1.pem            # Raw ISRG Root X1 PEM certificate
├── isrgrootx1.crt            # Raw ISRG Root X1 CRT certificate
├── scan.py                   # Automated repository indexer & hash generator
├── update.sh                 # One-command build and update script
├── Release                   # APT repository metadata & checksums (MD5, SHA1, SHA256)
├── Packages                  # APT uncompressed package catalog
├── Packages.bz2              # bzip2 compressed catalog (Required by iOS 7 Cydia!)
├── Packages.gz               # gzip compressed catalog
├── Packages.xz               # xz compressed catalog (Sileo / Zebra)
├── debs/                     # Hosted .deb Debian packages
│   ├── ai.akemi.appsyncunified_116.2_iphoneos-arm.deb
│   ├── ai.akemi.appinst_2.1.1_iphoneos-arm.deb
│   ├── com.hellokhe.isrgrootx1_1.0.0_iphoneos-arm.deb
│   └── ...
└── depictions/               # Rich depiction web pages rendered inside Cydia
    ├── style.css
    ├── index.html            # Dynamic depiction redirector (?p=package.id)
    ├── ai.akemi.appsyncunified.html
    └── ...
```

---

## ➕ Adding New Packages

Whenever you want to add new iOS 7 tweaks or `.deb` files:

1. Place your `.deb` file into the `debs/` directory:
   ```bash
   cp mytweak.deb debs/
   ```
2. Run the update script:
   ```bash
   ./update.sh
   ```
   *(This automatically extracts control metadata, calculates MD5/SHA1/SHA256, generates `Packages.bz2`, and updates `Release`).*

3. (Optional) Create a custom depiction in `depictions/<package_id>.html`.

4. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Add new iOS 7 tweak"
   git push origin main
   ```

---

## 🌐 Publishing to GitHub Pages

To publish this repository under your GitHub account (`Hellokhe`):

### Option A: Replace / Deploy to `Hellokhe/hellokhe.github.io`
If you want the root website `https://hellokhe.github.io/` to host the repository:
```bash
cd /Users/maxdelgado/.gemini/antigravity-ide/scratch/hellokhe-ios7-repo
git remote add origin https://github.com/Hellokhe/hellokhe.github.io.git
git branch -M main
git push -u origin main --force
```

### Option B: Deploy as a Sub-Repository (e.g. `https://hellokhe.github.io/repo/`)
If you want to keep your ZenOS wiki at the root and host the repo under `/repo/`:
1. Create a repository on GitHub named `repo` (or create a `repo/` subfolder in `hellokhe.github.io`).
2. Update `BASE_URL` in `scan.py` to `https://hellokhe.github.io/repo` and run `./update.sh`.
3. Push to `https://github.com/Hellokhe/repo.git`.
4. In GitHub Repo Settings &rarr; **Pages**, set Source to **main branch / root**.

---

## 📱 Supported Devices on iOS 7

- **iPhone 4** (`iPhone3,1`, `iPhone3,2`, `iPhone3,3`)
- **iPhone 4s** (`iPhone4,1`)
- **iPhone 5** (`iPhone5,1`, `iPhone5,2`)
- **iPhone 5c** (`iPhone5,3`, `iPhone5,4`)
- **iPhone 5s** (`iPhone6,1`, `iPhone6,2`)
- **iPad 2**, **iPad 3**, **iPad 4**, **iPad mini 1**
- **iPad Air**, **iPad mini 2**
- **iPod touch 5G** (`iPod5,1`)

---

## ⚖️ Credits & Licenses
- **AppSync Unified** and **appinst** created by [Karen/あけみ](https://github.com/akemin-dayo) and Linus Yang.
- **Checkmate, Store!** created by [InvoxiPlayGames](https://cydia.invoxiplaygames.uk/).
- **SwipeSelection** created by [iKy1e](https://github.com/freerunnering).
- **PreferenceLoader** created by Dustin Howett &amp; Sam Bingner.
- **Cydia** created by Jay Freeman (saurik).
