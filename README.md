[![CircleCI](https://circleci.com/gh/whardier/interdict.svg?style=svg)](https://circleci.com/gh/whardier/interdict)

# interdict
Python dictionary filter

# Installation

`pip install interdict`

# Examples

## Default (inclusion False)

```python
>>> from interdict import filter_obj
>>> obj = {'name': 'shane', 'job': {'salary': 1000000, 'role': 'master of universe'}}
>>> filter = {'name': True, 'job': {'role': True}}
>>> filter_obj(obj, filter)
{'name': 'shane', 'job': {'role': 'master of universe'}}
```

## Inclusive (a.k.a. TMI)

```python
>>> filter_obj(obj, filter, default=True)
{'name': 'shane', 'job': {'salary': 1000000, 'role': 'master of universe'}}
```

## Inclusive with better filter

```python
>>> filter = {'job': {'salary': False}}
>>> filter_obj(obj, filter, default=True)
{'name': 'shane', 'job': {'role': 'master of universe'}}
```

## Stacked filters

```python
>>> obj = {'name': 'shane', 'job': {'salary': 1000000, 'role': {'title': 'master of universe', 'reality': 'dumpster fire starter'}}}
>>> filter_1 = {'name': False}
>>> filter_2 = {'job': {'salary': False, 'role': {'reality': False}}}
>>> filter_obj(obj, [filter_1, filter_2], default=True)
{'job': {'role': {'title': 'master of universe'}}}
```
