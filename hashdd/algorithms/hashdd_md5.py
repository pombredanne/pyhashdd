"""
@brad_anton 

License:
 
Copyright 2015 hashdd.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import re
import hashlib

from algorithm import algorithm


class hashdd_md5(algorithm):
    name = 'hashdd_md5'
    validation_regex = re.compile(r'^[a-f0-9]{32}$', re.IGNORECASE)
    sample = '6C93F080B3CC1D15955AF589FE5D021A'

    def setup(self, arg):
        self.h = hashlib.md5()

    def hexdigest(self):
        return self.h.hexdigest().upper()

    def update(self, arg):
        self.h.update(arg)

import hashlib
hashlib.hashdd_md5 = hashdd_md5 
