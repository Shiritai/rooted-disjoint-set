# (有根) 併查集

> [!IMPORTANT]
> 這可能是我見過最優雅、使用者友好且 Python 風格的實作!

## 懶人包

是個併查集 (`dict[key, root_of_key]`)，其

* 行為如同 Python 的 `dict`
    * 有基於 `dict` 和基於 `disjoint-set` 的方法以供訪問
    * 兩者功能完全相同
* 保留各節點之根-子節點關係
* 使用深度降低演算法優化複雜度

## 使用方式

### 建構

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

### 設定依賴 (合併)

```python
ds[key] = value
# or
ds.set_dependent(key, value)
```

### 尋找根節點 (查詢)

```python
ds[key]
# or
ds.find_root(key)
```

### 確認是否同根 (確認)

```python
ds[key1] == ds[key2]
# or
ds.has_same_root(key1, key2)
```

### 是否為相同併查集

```python
ds1 = RootedDisjointSet()
ds2 = RootedDisjointSet()
ds1 == ds2
```

## 小記

歡迎任何留言、issue 和 PR ;)
