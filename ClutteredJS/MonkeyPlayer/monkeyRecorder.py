#!/usr/bin/env monkeyrunner
# Copyright 2010, The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script was retrieved from Google Git webpage at
# https://android.googlesource.com/platform/sdk/+/ics-mr0/monkeyrunner/scripts/monkey_recorder.py


# noinspection PyUnresolvedReferences,PyPackageRequirements
from com.android.monkeyrunner import MonkeyRunner
# noinspection PyUnresolvedReferences,PyPackageRequirements
from com.android.monkeyrunner.recorder import MonkeyRecorder

device = MonkeyRunner.waitForConnection()
MonkeyRecorder.start(device)
