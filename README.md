# Docker images

[![Build Status](https://travis-ci.org/NYAG/dockers.svg?branch=master)](https://travis-ci.org/NYAG/dockers)

This repository contains Dockerfiles intended for use by the
Department of Research and Analytics at the
[New York State Office of the Attorney General][nyag].

## dumpling

[dumpling][dumpling] is our Docker image containing common
packages and tools for a consistent data science environment,
including Python 3, Pandas, Jupyter, Git, and [oaglib].

When contributing changes, please add tests to
[`bin/dumpling-test`](bin/dumpling-test).

## lab-asst

lab-asst is a tool that we use to manage Jupyter lab instances,
in case they're left open in the background. lab-asst shows information
about currently running notebooks and kernels, including CPU
usage percentage, memory usage percentage, the time the notebook or kernel was opened,
and if it's a notebook what URL it can be reached at.
lab-asst can also be used to close currently running instances. lab-asst
will attempt to close the instance and warn the user if it appears that there is
unsaved work that could be lost on close.

Kernels should be stopped by stopping the parent ID associated with the kernel.
Stopping the kernel ID will just cause Jupyter to restart the kernel.

### Usage

```text
lab-asst: An assistant for managing Jupyter lab instances.

Usage: ./lab-asst [argument]
Possible arguments:

-l              List all running Jupyter lab instances. Includes time the notebook was opened, CPU usage, and RAM usage.
-s [id]         Stop given Jupyter lab instance gracefully.

```

### Example output

![screenshot showing listing of lab instances][screenshot_1]
![screenshot showing instance stop][screenshot_2]

[nyag]: https://ag.ny.gov/
[dumpling]: https://hub.docker.com/r/nyag/dumpling/
[oaglib]: https://github.com/NYAG/oaglib
[screenshot_1]: lab-asst_listing.PNG
[screenshot_2]: lab-asst_stop.PNG
