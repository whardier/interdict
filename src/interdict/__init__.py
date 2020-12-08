# https://github.com/whardier/interdict/blob/main/src/interdict/__init__.py

# ╻┏┓╻╺┳╸┏━╸┏━┓╺┳┓╻┏━╸╺┳╸       ╻┏┓╻╻╺┳╸
# ┃┃┗┫ ┃ ┣╸ ┣┳┛ ┃┃┃┃   ┃        ┃┃┗┫┃ ┃
# ╹╹ ╹ ╹ ┗━╸╹┗╸╺┻┛╹┗━╸ ╹ ╹╺━╸╺━╸╹╹ ╹╹ ╹ ╺━╸╺━╸

# SPDX-License-Identifier: MIT

# MIT License

# Copyright (c) 2020 Shane R. Spencer

# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from typing import Any, Dict, List, Union

from flatten_dict import flatten, unflatten


def filter_obj(  # dead: disable
    obj: Dict[Any, Any],
    filter: Union[Dict[Any, Any], List[Dict[Any, Any]]],
    default: bool = False,
) -> Dict[Any, Any]:
    """ Filter an object based on a somewhat complex filter of booleans """

    flattened_obj = flatten(obj)  # noqa

    if isinstance(filter, dict):
        filter = [filter]

    filtered_flattened_obj: Dict[Any, Any]

    for _filter in filter:
        flattened_filter = flatten(_filter)
        filtered_flattened_obj = {}
        for obj_key, obj_val in flattened_obj.items():
            # Set default
            flattened_filter.setdefault(obj_key, default)
            for filter_key, filter_val in flattened_filter.items():
                len_filter_key = len(filter_key)

                if filter_key == obj_key[:len_filter_key]:
                    if filter_val is True:
                        filtered_flattened_obj[obj_key] = obj_val
        flattened_obj = filtered_flattened_obj

    return unflatten(flattened_obj)
