from django.core.cache.backends.db import DatabaseCache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import connection
from readonly.wrappers import override_readonly


class ReadOnlyOverrideDatabaseCache(DatabaseCache):
    def _base_set(self, mode, key, value, timeout=DEFAULT_TIMEOUT):
        with connection.execute_wrapper(override_readonly):
            super()._base_set(mode, key, value, timeout)

    def _base_delete_many(self, keys):
        with connection.execute_wrapper(override_readonly):
            super()._base_delete_many(keys)
