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
