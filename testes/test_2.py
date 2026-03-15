from scrapper import Crawler


def test_get_movie():
    url = "https://pt.wikipedia.org/wiki/Uno_(jogo_de_cartas)"
    crawler = Crawler(url)
    crawler.craw()

    assert len(crawler.indexes) > 0
    assert crawler.indexes == [
        'Regras oficiais', 
        'Referências', 
        'Ligações externas'
    ]

    assert "250px-Uno.jpg" in crawler.images
    assert "250px-UNO_cards_deck.svg.png" in crawler.images

    assert len(crawler.links) == 88
