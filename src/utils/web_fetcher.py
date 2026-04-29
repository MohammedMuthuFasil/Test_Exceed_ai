from __future__ import annotations

from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser


def is_allowed(url: str, user_agent: str = "*") -> bool:
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    robots_url = urljoin(base_url, "/robots.txt")

    robot_parser = RobotFileParser()
    robot_parser.set_url(robots_url)
    robot_parser.read()

    return robot_parser.can_fetch(user_agent, url)


def main() -> None:
    start_url = "http://example.com"
    allowed = is_allowed(start_url)
    print(f"allowed={allowed} url={start_url}")


if __name__ == "__main__":
    main()
