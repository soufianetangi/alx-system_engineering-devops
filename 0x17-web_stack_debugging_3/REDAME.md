# Web Stack Debugging - Task 0: Strace is Your Friend

## Project Overview

This project is part of the ALX System Engineering DevOps curriculum. The goal of this task is to debug and fix an Apache 500 Internal Server Error using `strace`, and then automate the fix using Puppet.

### Task Details

1. **Problem Description**:
   Apache is returning a 500 Internal Server Error. The objective is to identify the cause of the error using `strace` and then apply a fix with Puppet.

2. **Solution Approach**:
   - **Debugging with `strace`**: Use `strace` to monitor system calls and signals of the Apache process to identify the root cause of the error.
   - **Automating with Puppet**: Create a Puppet manifest to apply the necessary fixes and ensure that Apache is properly configured and running.

## Setup Instructions

### Prerequisites

- **Ubuntu 14.04 LTS**: The Puppet manifests and testing should be performed on Ubuntu 14.04 LTS.
- **Puppet**: Puppet version 3.4 must be installed.
- **puppet-lint**: Install version 2.1.1 for linting the Puppet manifests.

### Installing Dependencies

1. **Install Ruby and Puppet**:
   ```bash
   sudo apt-get update
   sudo apt-get install -y ruby
   sudo gem install puppet -v 3.4

