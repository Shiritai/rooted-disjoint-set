from typing import Optional, TypeVar, overload


T = TypeVar("T")


class RootedDisjointSet(dict[T, T]):
    """A disjointed set (`dict[key, root_of_key]`) that

    * behaves completely the same as a Python `dict`
        * has `dict` based and `disjoint-set` based methods for accessing
        * with complete the same effect
    * reserve the root-child relation of the keys
    * optimized with flattening
    * has perhaps
        * the most user-friendly usage
        * the simplest codebase
    """

    @overload
    def __init__(self): ...

    @overload
    def __init__(self, deps: dict[T, T]): ...

    def __init__(self, deps: Optional[dict[T, T]] = None):
        """Construct according to the given dependency map

        Args:
            deps (dict[T, T]): dependency map `dict[key, parent_of_key]`
        """
        if deps is not None:
            for k, v in deps.items():
                self[k] = v

    def __eq__(self, other):
        return isinstance(other, RootedDisjointSet) and all(
            self[key1] == other[key2]
            for key1, key2 in zip(self, other)
        )

    def __getitem__(self, key: T):
        """Get the root dependency of the given key
        a.k.a. the `find` method of a disjoint set.
        """
        # find the root first
        root = self._brutal_find_root(
            # add new entry if DNE
            self.setdefault(key, key)
        )
        # then flatten the whole set
        while key != super().__getitem__(key):
            nxt_pos = super().__getitem__(key)
            super().__setitem__(key, root)
            key = nxt_pos
        return root

    def __setitem__(self, key: T, depends_on: T):
        """Set `key` to be dependent on `depends_on`,
        a.k.a. the `merge` or `union` method of a disjoint set.

        Does nothing if the given `key` already depends on `depends_on`
        ***OR EVEN*** `depends_on` already depends on `key`.
        """
        pp, pc = self[depends_on], self[key]
        if pp == pc:
            return
        super().__setitem__(pc, pp)

    def _brutal_find_root(self, key: T):
        while key != super().__getitem__(key):
            key = super().__getitem__(key)
        return key

    def find_root(self, key: T):
        """Get the root dependency of the given key
        a.k.a. the `find` method of a disjoint set.

        Same as `self[key]`.
        """
        return self[key]

    def have_same_root(self, key1: T, key2: T):
        """Check whether the two keys depend on the same root
        a.k.a. the `check` method of a disjoint set.

        Same as `self[key1] == self[key2]`.
        """
        return self[key1] == self[key2]

    def set_dependent(self, key: T, depends_on: T):
        """Set `key` to be dependent on `depends_on`,
        a.k.a. the `merge` or `union` method of a disjoint set.

        Does nothing if the given `key` already depends on `depends_on`
        ***OR EVEN*** `depends_on` already depends on `key`.

        Same as `self[key] = depends_on`.
        """
        self[key] = depends_on
