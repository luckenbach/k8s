# ssh keys
This folder will be scanned for ssh keys.
For every found key new user on created vms will be added with coresponded ssh key.
All keys should have format: **(?P<username>[a-z_][a-z0-9_-]*[$]?)\.pub**
