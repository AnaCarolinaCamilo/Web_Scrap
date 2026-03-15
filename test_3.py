from scrapper import Crawler


def test_get_movie():
    url = "https://pt.wikipedia.org/wiki/Ayo_Edebiri"
    crawler = Crawler(url)
    crawler.craw()

    assert len(crawler.indexes) > 0
    assert crawler.indexes == [
        "Biografia",
        "Vida pessoal",
        "Filmografia",
        "Referências",
        "Ligações externas"
    ]

    assert "wikipedia.png" in crawler.images
    assert "40px-Flag_of_the_United_States.svg.png" in crawler.images

    assert len(crawler.links) == 329
