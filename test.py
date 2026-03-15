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

    assert "250px-Toler%C3%A2ncia.jpg" in crawler.images
    assert "40px-Flag_of_Brazil.svg.png" in crawler.images

    assert len(crawler.links) == 127
