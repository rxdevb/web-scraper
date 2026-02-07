# My Web Scraper

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## About The Project

My Web Scraper is a simple, Dockerized Python application designed to demonstrate web scraping capabilities. It efficiently fetches data from Hacker News, extracting page titles and the latest news headlines.

The project showcases how to containerize a Python script, manage dependencies, and interact with web content using popular libraries.

### Built With

*   **Language**: Python 3.9
*   **Containerization**: Docker
*   **Libraries**: Requests, BeautifulSoup4

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Docker
*   Git (optional)

### Installation

1.  **Clone the repository** (if you haven't already)
    ```sh
    git clone https://github.com/your_username/my-web-scraper.git
    cd my-web-scraper
    ```

2.  **Build the Docker Image**
    ```sh
    docker build -t my-scraper .
    ```

3.  **Run the Scraper**
    ```sh
    docker run my-scraper
    ```

## Features

*   **Automated Scraping**: Fetches and parses HTML content automatically.
*   **Dockerized Environment**: Runs in a consistent, isolated environment.
*   **Error Handling**: Robust handling of network errors and parsing exceptions.
