# TerraBot: Simplifying Infrastructure Management with Telegram

Managing infrastructure using Terraform is already a breeze, but what if there was a way to make it even easier, more convenient, and accessible from anywhere? Well, that's where TerraBot comes into play.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

We all know that creating and destroying instances, configuring networks, and provisioning cloud resources via Terraform is super easy. But what if you could do it all with just a few taps on your smartphone, without even having to open your laptop? Here's the solution you've been waiting for - TerraBot!

TerraBot is a simple yet powerful Telegram bot designed to streamline your infrastructure management tasks. It leverages the power of Terraform and the convenience of Telegram, making your life easier, whether you're in the office, at home, or on the go.

## Getting Started

Getting started with TerraBot is a straightforward process. Here are the basic steps:

1. **Installation**: Clone this repository to your local environment and for easier use, you can copy the app.py to the same DIR as your terraform files.

2. install python telegram bot with pip3 (pip3 install python-telegram-bot==13.5)

3. **Configuration**: Set up your TerraBot by configuring it with your Telegram API token, Replace the token with your own Telegram bot token.

4. In Telegram, change your bot settings and disable groups after you add it to your group, so your bot cant be added to any other groups

5. **Interact with TerraBot**: Start using TerraBot right away! Send commands and interact with your infrastructure using simple text messages. Refer to the [Usage](#usage) section for a list of available commands and examples.

## Features

TerraBot comes packed with a range of features to simplify your infrastructure management:

- **Resource Creation**: Easily create and manage resources like EC2 instances, databases, and networks.

- **State Management**: Check the current state of your infrastructure at any time.

- **Rollback**: In case something goes wrong, quickly roll back to a previous state.

- **Customization**: Define your infrastructure templates and configurations in Terraform, and TerraBot will execute them.

- **Access Control**: Set access controls and permissions to ensure security and manageability.

- **Notifications**: Receive status updates and alerts right in your Telegram chat.

## Usage

TerraBot is designed to be intuitive and user-friendly. You can use it for a variety of tasks like creating, updating, and destroying resources. Here are some sample commands to get you started:

- `/apply 2`: Create 2  instances.

- `/show`: Show your current infrastructure.

- `/plan 4`: show a simple plan output.


## Contributing

We welcome contributions from the community to make TerraBot even more powerful and user-friendly. If you have ideas for improvements, bug fixes, or new features, please check out our [Contribution Guidelines](CONTRIBUTING.md) and join us in making TerraBot better for everyone.

## License

TerraBot is open-source and is distributed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed. We hope that TerraBot makes your life easier and enhances your Terraform experience.

If you have any questions or need assistance, don't hesitate to reach out. Happy automating with TerraBot!

---
