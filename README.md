# python-django-haposctl-webui

This project aims to provide a simplified web based user interface to switch between maintenance and ready/up states
in HAProxy Open Source edition.
If You are using HAProxy Enterprise edition you already have a sufficient UI to control your proxy.

The application uses the HAProxy backend to post specific states. This means it uses the stats site to manage states.
This way one does not have to publish an application which has to write into the HAProxy socket which can do a lot more
than the statistics backend.

The project is called _haposctl-webui_ or HAProxy Open Source Controller WebUI.

## Install

### Requirements



#### Test

#### Build

### How to install

### Configuration

## Contribute

Contributions are appreciated.

### Before you commit

We strongly advise to use `pre-commit` with our provided `.pre-commit-config.yaml` before you commit and push your
contribution.

This assures code style and some quality standards are met before you create some unclean states of your work.
However, since nobody can be trusted the same tools run in CI pipelines.

```shell
foo@bar:~$ pip install pre-commit
foo@bar:~$ pre-commit install
```

Pre commit hooks running `pylint`, `pytest` and `flake8` with `flake8-bandit` and `flake8-black`.

### Pipeline tests

Additionally, we use `atheris` to provide fuzzing and `pytest` for unit testing purposes.

We do not merge until everything is green.
