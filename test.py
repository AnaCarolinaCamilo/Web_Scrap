import pytest
from scrapper import Crawler


def test_get_movie():
    url = "https://pt.wikipedia.org/wiki/Toler%C3%A2ncia_(filme)"
    crawler = Crawler(url)
    crawler.craw()

    assert len(crawler.indexes) > 0
    assert crawler.indexes == [
        "Sinopse",
        "Recepção",
        "Elenco",
        "Trilha sonora",
        "Referências",
    ]

    assert len(crawler.links) == 127
