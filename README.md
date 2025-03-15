# SendEase - Bulk Email Customization Tool

SendEase is a powerful tool that enables you to send personalized emails to multiple recipients using data from Excel files. This application streamlines the process of customizing email content for each recipient, making bulk emailing more efficient and personal.


## 🚀 Features

- **Excel Integration**: Import recipient data directly from Excel spreadsheets
- **Dynamic Templates**: Create email templates with custom variables
- **Personalization**: Automatically customize emails based on recipient data
- **Batch Processing**: Send emails to multiple recipients in one go
- **Preview Functionality**: Review emails before sending
- **User-friendly Interface**: Easy-to-use Streamlit web interface
- **SMTP Support**: Compatible with various email service providers

## 📋 Prerequisites

- Python 3.7+
- Excel file with recipient data
- Email account with SMTP access

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SendEase.git
cd SendEase
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Create a `.env` file in the project root directory with your email credentials:
```
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
```

## 🧑‍💻 Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the web interface at `http://localhost:8501`

3. Upload your Excel file containing recipient data
   - Your Excel file should include columns like `email`, `name`, and any other variables you want to use in your templates

4. Create your email template with variables in curly braces, e.g., `Hello {name},`

5. Preview personalized emails and send them

## 📊 Excel File Format

Your Excel file should follow this structure:
| email | name | variable1 | variable2 | ... |
|-------|------|-----------|-----------|-----|
| recipient1@example.com | Recipient 1 | Value 1 | Value 2 | ... |
| recipient2@example.com | Recipient 2 | Value 1 | Value 2 | ... |

## 🔒 Security

- SendEase doesn't store your email credentials permanently
- Sensitive information is only kept in memory during execution
- Use app-specific passwords for services like Gmail for enhanced security

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Support

For questions and support, please open an issue in the GitHub repository or contact the maintainers.
