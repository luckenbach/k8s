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

# pylint: disable=invalid-name
"""
    Logging configuration for scripts.
    To use it just `from .logger import logger`.
    INFO is sent to STDOUT and DEBUG is sent to file.

"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename='/tmp/k8s_installer.log',
    filemode='w'
)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s %(name)-12s: %(levelname)-8s %(message)s'
)

console.setFormatter(formatter)

logger = logging.getLogger('k8s_installer')
logger.addHandler(console)
