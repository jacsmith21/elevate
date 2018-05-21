import collections

class DotDict(dict):
    def __getattr__(self, item):
        if item not in self:
            self._raise_not_found(item)

        return self[item]

    def __setattr__(self, key, value):
        if key not in self:
            self._raise_not_found(key)

        self[key] = value

    def _raise_not_found(self, key):
        raise ValueError('{} does not exist. The available keys are: {}'.format(key, list(self.keys())))


def dict_merge(dct, merge_dct):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """
    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict) and isinstance(merge_dct[k], collections.Mapping)):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]

    return dct
