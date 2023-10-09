# Scraper - Detailed Documentation

## Overview

The Scraper is a Python command-line tool designed to scrape code submissions from various online programming platforms and store them in a GitHub repository. It supports platforms such as Codeforces, CSES (University of Helsinki), and Vjudge. This documentation provides a detailed overview of the Scraper's functionalities and how to use them.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Initialization](#initialization)
    - [Scraping](#scraping)
4. [Command-Line Interface](#command-line-interface)
5. [Scraper Configuration](#scraper-configuration)
6. [Customization](#customization)
7. [Data Storage](#data-storage)
8. [FAQs](#faqs)
9. [Contributing](#contributing)
10. [License](#license)

## 1. Features <a name="features"></a>

- **Supported Platforms**: The Scraper supports the following programming platforms:
  - Codeforces
  - CSES (University of Helsinki)
  - Vjudge

- **GitHub Integration**: Code submissions are stored in a GitHub repository, making it easy to manage and share your solutions.

- **Automatic README Generation**: The Scraper automatically generates a README file for your GitHub repository, listing all your code submissions with problem details, links, and tags.

- **Incremental Scraping**: The Scraper keeps track of previously scraped submissions, ensuring that only new submissions are added to your repository.

- **Authentication**: Securely authenticate with the supported platforms to access your submissions.

- **Customization**: Customize the formatting of your README and configure other scraper options.

## 2. Installation <a name="installation"></a>

To use the Scraper, follow these installation steps:

1. **Clone the Repository**: Clone the Scraper repository to your local machine:

    ```shell
    git clone https://github.com/your-username/scraper.git
    ```

2. **Install Dependencies**: Install the necessary Python dependencies by navigating to the repository directory and running:

    ```shell
    pip install -r requirements.txt
    ```

3. **Configuration**: Set up your GitHub repository and obtain a GitHub access token.

4. **Initialize**: Run the initialization command to set up your user data and repository configuration:

    ```shell
    python main.py -c init
    ```

    Follow the prompts to provide your GitHub username, repository name, and access token.

## 3. Usage <a name="usage"></a>

The Scraper has two primary modes of operation: initialization and scraping.

### Initialization <a name="initialization"></a>

Initialization is the first step to configure your scraper for a GitHub repository.

1. Run the initialization command:

    ```shell
    python main.py -c init
    ```

2. Follow the prompts to enter your GitHub username, repository name, and access token.

### Scraping <a name="scraping"></a>

Scraping allows you to retrieve code submissions from supported platforms and store them in your GitHub repository.

1. To scrape submissions, use the following command:

    ```shell
    python main.py -s PLATFORM_NAME
    ```

    Replace `PLATFORM_NAME` with one of the supported platforms: `codeforces`, `cses`, or `vjudge`.

2. Depending on the platform, you may need to provide additional information such as your platform username and password.

3. The Scraper will fetch new submissions and update your GitHub repository.

## 4. Command-Line Interface <a name="command-line-interface"></a>

The Scraper provides a command-line interface with the following options:

- `-c`, `--command`: Specify the command (`init` for initialization or `update` for scraping).

- `-s`, `--scrap`: Specify the platform to scrape data from (`codeforces`, `cses`, or `vjudge`).

- `--help`: Display usage instructions and available options.

Example usage:

```shell
python main.py -c init
python main.py -s codeforces
```

## 5. Scraper Configuration <a name="scraper-configuration"></a>

The Scraper can be configured in several ways:

- **GitHub Configuration**: Set up your GitHub repository details and access token during initialization.

- **Platform Authentication**: Authenticate with your platform credentials (e.g., Codeforces username and password) for scraping.

- **Customization**: Customize the formatting of your README and configure scraper options in the code (e.g., maximum requests, submission per update).

## 6. Customization <a name="customization"></a>

You can customize the Scraper's behavior by modifying the source code. Here are some customization options:

- **Formatting**: Customize the formatting of the generated README for each platform. You can modify the formatting in the corresponding `Formatter` class.

- **Configuration**: Adjust the scraper's settings, such as maximum requests, submissions per update, or other platform-specific parameters.

## 7. Data Storage <a name="data-storage"></a>

The Scraper stores code submissions and related information in your GitHub repository. Each submission is listed in the README with details such as problem name, language, solution link, tags, and submission date.

## 8. FAQs <a name="faqs"></a>

- **What platforms does the Scraper support?**
  - The Scraper currently supports Codeforces, CSES (University of Helsinki), and Vjudge.

- **Is it safe to store my GitHub access token?**
  - Access tokens should be stored securely. The Scraper stores them in a configuration file, and it's essential to protect this file.

- **How can I customize the README format?**
  - You can customize the README format by modifying the corresponding `Formatter` class for each platform.

## 9. Contributing <a name="contributing"></a>

Contributions to the Scraper are welcome! Feel free to fork the repository, make improvements, and create pull requests.

## 10. License <a name="license"></a>

The Scraper is released under the MIT License. See the [LICENSE](https://github.com/your-username/scraper/blob/main/LICENSE) file for details.

---

*Note: This documentation provides an overview of the Scraper's functionality and usage. For detailed code explanations, refer to the source code and comments in the Scraper's repository.*