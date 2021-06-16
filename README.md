<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">VK API for groups</h3>

  <p align="center">
    Python package, that allows posting to groups with ease.
    <br />
    <a href="#usage">How to Use</a>
    ·
    <a href="https://github.com/rokoel/vk_api_for_groups/issues">Report Bug</a>
    ·
    <a href="https://github.com/rokoel/vk_api_for_groups/issues">Request Feature</a>
  </p>




<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#todo">TODO (planned)</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Post to vk groups with ease.



### Built With

* [Python](https://www.python.org/)
* [Python's package requests](https://pypi.org/project/requests/)

### TODO

* Add text formatting from .md files
* Add attachment support
* Add ability to change groups' settings.
* Add auto attachments uploading to vk servers



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Python language is necessary, obviously.
You need to also install Python requests:
```shell
pip install requests
```

### Installation

```shell
pip install vk_api_for_groups
```


<!-- USAGE EXAMPLES -->
## Usage

Usage example is located in examples/example.py

### Intended usage

```python
from src.vk_api_for_groups import Api

token = "____________________________________..."  # your token here
group_id = -000000000  # your group's id
group_api = Api(token, group_id, ver=5.131)  # you may leave version blank
# (in that case latest will be used)

group_api.send_post(post="Message")
# OR
group_api.send_post(post_path="path/to/file.txt")
```
Look at example for further details.

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@rokoel_dude](https://twitter.com/rokoel_dude)

Project Link: [https://github.com/rokoel/vk_api_for_groups](https://github.com/rokoel/vk_api_for_groups)
