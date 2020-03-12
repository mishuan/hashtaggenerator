import hashtags_data as hd

GEN_PORTS = {
    hd.POPULAR_PORTRAIT: 1.0,
}

YAYAREA_PORTS = {
    hd.POPULAR_PORTRAIT: 0.75,
    hd.YAYAREA: 0.25,
}

GEN = {
    hd.GENERIC: 1.0,
}

GEN_FILM = {
    hd.FILM: 0.8,
    hd.FILM_FEATURES: 0.2,
}

ASIA_FILM = {
    hd.FILM: 0.5,
    hd.FILM_FEATURES: 0.2,
    hd.JP_FILM: 0.2,
    hd.KR_FILM: 0.1
}

TYPE_MAP = {
    'portraits': GEN_PORTS,
    'general': GEN,
    'bayareaportraits': YAYAREA_PORTS,
    'general_film': GEN_FILM,
    'asia_film': ASIA_FILM
}

