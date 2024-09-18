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