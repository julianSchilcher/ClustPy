from clustpy.deep import DEC, IDEC
from clustpy.data import load_optdigits
import numpy as np


def test_simple_dec_with_optdigits():
    X, labels = load_optdigits()
    dec = DEC(10, pretrain_epochs=10, clustering_epochs=10)
    assert not hasattr(dec, "labels_")
    dec.fit(X)
    assert dec.labels_.dtype == np.int32
    assert dec.labels_.shape == labels.shape


def test_simple_idec_with_optdigits():
    X, labels = load_optdigits()
    idec = IDEC(10, pretrain_epochs=10, clustering_epochs=10)
    assert not hasattr(idec, "labels_")
    idec.fit(X)
    assert idec.labels_.dtype == np.int32
    assert idec.labels_.shape == labels.shape