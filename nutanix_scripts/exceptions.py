# Copyright (c) 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Custom exceptions"""


class ConfigurationError(ValueError):
    """Exception for configuration validation purpose."""
    INVALID_NUMBER_OF_MASTERS = 'Number of master nodes must belongs to set {}'
    INVALID_TYPE = 'Invalid config field value: {}'
    MISSING_SECTION = 'Missing {} section in configuration file'
    MISSING_CLUSTER = 'Missing {} cluster configuration'
    MISSING_FIELD = 'Configuration missing field {}'
    INVALID_CREDENTIALS = 'Invalid credentials'
    CONNECTION_PROBLEM = """Problem with connection to Nutanix API.
        Check your Nutanix Prism address, port and Prism connectivity"""
    INVALID_DOMAIN = "Kubernetes cluster name(domain) need to match RFC 1035"


class InvalidNumberOfItems(Exception):
    """Exception for validating number of items."""
    INVALID_COUNT = 'There is {} {} with name {}, expected number was {}.'


class ItemDoesNotExist(Exception):
    """Exception for items not found."""
    MESSAGE = '{} {} does not exist'


class TaskFailed(Exception):
    """Exception for handling task failure"""
    MESSAGE = 'Task Failed. Detailed info: {}'


class MissingKeys(Exception):
    """Exception for missingi/wrongly named ssh keys in ssh keys directory"""
    MESSAGE = "There weren't any file matching {} format in ssh keys directory"
