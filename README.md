# (Rooted) Disjoint set

> [!NOTE]
> 可參閱[中文文檔](./README.zh_TW.md)。

> [!IMPORTANT]
> This is perhaps the most elegant, user-friendly and Python-styled implementation I've ever seen!

## TL;DR

A disjointed set (`dict[key, root_of_key]`) that

* behaves completely the same as a Python `dict`
    * has `dict` based and `disjoint-set` based methods for accessing
    * with complete the same effect
* reserve the root-child relation of the keys
* optimized with flattening

## Usage

### Instantiate

```python
ds = RootedDisjointSet()

# or
ds = RootedDisjointSet({ 1: 1, 2: 1, 3: 2 })
# 1 <- 2 <-3

# or
ds = RootedDisjointSet({ 1: '1', '2': '1', 3: 1 })
# '1' <- 1 <- 3
# '1' <- '2'
# note that key can be any hashable type
```

### Set dependent (Merge)

```python
ds[key] = value
# or
ds.set_dependent(key, value)
```

### Find root (Find)

```python
ds[key]
# or
ds.find_root(key)
```

### Has same root (Check)

```python
ds[key1] == ds[key2]
# or
ds.has_same_root(key1, key2)
```

### Is same disjoint set

```python
ds1 = RootedDisjointSet()
ds2 = RootedDisjointSet()
ds1 == ds2
```

## Note

Welcome to give any kinds of comment, open issues or make PR ;)
