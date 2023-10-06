#!/usr/bin/env python3
# coding: utf-8

import contextlib


@contextlib.contextmanager
def numpy_temp_seed(seed):
    state = np.random.get_state()
    if seed is not None:
        np.random.seed(seed)
    try:
        yield
    finally:
        if seed is not None:
            np.random.set_state(state)
