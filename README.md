# Splunk app packager

The Splunk app packager runs as a cli tool to package your Splunk app, validate the app, and push it to your Splunk instance.

## Install splunk-app-packager

```shell
$ pip install splunk-app-packager
```

## Run splunk-app-packager

### Set environment variables

```shell
$ export SPLUNK_USER=<splunk.com user account>
$ export SPLUNK_PASSWORD=<splunk.com user password>
$ export SPLUNK_ACS_TOKEN=<splunkcloud acs token>
$ export SPLUNK_ACS_STACK=<splunkcloud acs stack name>
```

### Create a config.toml file

Create a `package_config` section within your config.toml file and set the app name and splunk_user name as shown below:
```
[package_config]
app = "NAME"
environment = ""
version = ""
splunk_user = "SPLUNK_APP_ACCOUNT"
```

splunk_app_packager will look for a `config.toml` file in your current working directory, otherwise you can use the `--config-path` option to specify it's name and location.

### CLI arguments

```shell
$ sap --help
Usage: splunk_app_packager [OPTIONS] APP_PACKAGE

Options:
  --splunkuser TEXT      The splunk.com username. Can also be set via
                         SPLUNK_USER environment variable  [required]
  --splunkpassword TEXT  The splunk.com password. Can also be set via
                         SPLUNK_PASSWORD environment variable  [required]
  --justvalidate         Provied a package .tag.gz instead of a directory and
                         validate it.
  --prod                 Build a PRODUCTION package
  --nodeploy             Do NOT do the Deploy leg, just validate
  --outfile TEXT         Provied a package .tag.gz instead of a directory and
                         validate it.
  --acs-stack TEXT       The name of the ACS stack. Can also be set via
                         SPLUNK_ACS_STACK environment variable.
  --acs-token TEXT       A bearer token for Splunk ACS. Can also be set via
                         SPLUNK_ACS_TOKEN environment variable.
  --config-path TEXT     A path to the config.toml file.  [required]
  --help                 Show this message and exit.
```

### Example usage

```shell
$ sap /path/to/app/folder  --prod
```

## Use as GitHub Action

### Example production deployment

```yaml
name: Production Deployment 

on:
  push:
    branches:
      - main
    paths:
      - APP_NAME/**
  workflow_dispatch:

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: dfe-digital/splunk-app-packager@v0.0.2
        with:
          app_package_path: 'APP_NAME'
          splunk_username: ${{ secrets.SPLUNK_USERNAME }}
          splunk_password: ${{ secrets.SPLUNK_PASSWORD }}
          splunk_acs_token: ${{ secrets.SPLUNK_ACS_TOKEN }}
          splunk_acs_stack: ${{ secrets.SPLUNK_ACS_STACK }}
```

### Example with a different path for config.toml

```yaml
name: Production Deployment 

on:
  push:
    branches:
      - main
    paths:
      - APP_NAME/**
  workflow_dispatch:

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: dfe-digital/splunk-app-packager@v0.0.2
        with:
          app_package_path: 'APP_NAME'
          splunk_username: ${{ secrets.SPLUNK_USERNAME }}
          splunk_password: ${{ secrets.SPLUNK_PASSWORD }}
          splunk_acs_token: ${{ secrets.SPLUNK_ACS_TOKEN }}
          splunk_acs_stack: ${{ secrets.SPLUNK_ACS_STACK }}
          config_toml_path: 'conf/config.toml' 
```

## Contributing
Refer to [our contributing guidelines](.github/CONTRIBUTING.md) if you'd like to raise a bug or pull request.