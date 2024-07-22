Here is an example of a `README.md` file for your CLI app:


# STD (Sexually Transmitted Disease)

`std` is a CLI tool to scan codebases for exposed secrets. It helps developers ensure that sensitive information such as API keys, passwords, and private keys are not accidentally pushed to remote repositories.

## Features

- Scans directories and files for exposed secrets
- Detects various types of secrets including API keys, passwords, and private keys
- Uses `tqdm` for a progress bar while scanning
- Beautifies the output using the `rich` library
- Provides a simple CLI interface using `click`

## Installation

### From PyPi
```bash
pip install std
# OR
poetry add std

# after installation you can check to make sure it's installed properly by running the below command:
std --help
```
### Building From Source

Ensure you have [Poetry](https://python-poetry.org/) installed. Then, run the following commands:

```bash
# Clone the repository
git clone https://github.com/ProfessorBlackman/std.git
cd std

# Install dependencies
poetry install

# Build the package
poetry build

# Install the package
pip install dist/std-0.1.0-py3-none-any.whl


## Usage

After installing the package, you can use the `std` command to scan files and directories.

### Scan a Directory

```bash
std scan-directory /path/to/directory
```

### Scan a File

```bash
std scan-file /path/to/file
```

## Example

Here is an example of how to use the `std` tool:

```bash
# Scan a directory
std scan-directory ./my_project

# Scan a single file
std scan-file ./my_project/config.py
```

## Development

If you want to contribute or modify the tool, follow these steps to set up your development environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/ProfessorBlackman/std.git
    cd std
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

3. Run tests:
    ```bash
    pytest
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

This project uses the following libraries:
- [Click](https://click.palletsprojects.com/) for the CLI interface
- [Tqdm](https://tqdm.github.io/) for the progress bar
- [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- [Poetry](https://python-poetry.org/) for dependency management and packaging

## Contact

For any questions or suggestions, please contact [Methuselah Nwodobeh](mailto:methuselahnwodobeh@gmail.com).
```

### Tips for Customization
1. **Repository URL**: Replace `https://github.com/yourusername/std.git` with the actual URL of your repository.
2. **Author Information**: Update the contact section with your actual name and email.
3. **License**: Ensure the license type matches your project's license file.

This `README.md` provides a comprehensive overview of your project, instructions for installation, usage examples, and development guidelines.