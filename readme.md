# Bulk Gmail Creator

Bulk Gmail Creator is a Python-based project designed to automate the process of creating Gmail accounts in bulk. This project leverages environment variables for configuration and uses a virtual environment to manage dependencies.

## Prerequisites

- Python 3.7+
- Git
- Terminal (CMD, PowerShell, or Unix Terminal)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Bulk_Gmail_Creator.git
cd Bulk_Gmail_Creator
```

### 2. Virtual Environment Setup

Create and activate a virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Unix/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root directory
2. Add the following configuration:

```env
API_KEY=your_api_key_here
DATABASE_URL=your_database_url
DEBUG=True
# Add other required configuration variables
```

## Usage

1. Ensure your virtual environment is activated
2. Run the script:

```bash
python main.py --count 10
```

Parameters:
- `--count`: Number of Gmail accounts to create
- `--output`: Output file path (default: accounts.txt)
- `--proxy`: Proxy list file (optional)

## Troubleshooting

### Windows PowerShell Script Execution

If you encounter script execution issues in PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### Common Issues

1. **Rate Limiting**: Wait a few minutes between bulk creation attempts
2. **Proxy Errors**: Ensure proxy list is properly formatted
3. **Authentication Failed**: Verify API credentials in .env file

## Features

- Bulk account creation
- Proxy support
- Custom output formatting
- Rate limit handling
- Error logging

## Project Structure

```
Bulk_Gmail_Creator/
├── main.py
├── requirements.txt
├── .env
├── accounts/
│   └── output/
├── proxies/
│   └── proxy_list.txt
└── logs/
    └── error.log
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Users are responsible for complying with Google's Terms of Service and applicable laws.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.