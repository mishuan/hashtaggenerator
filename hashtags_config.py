import hashtags_data as hd

GEN_PORTS = {
    hd.POPULAR_PORTRAIT: 1.0,
}

GEN_PORTS_SMALL = {
    hd.PORTRAIT_S: 0.4,
    hd.PORTRAIT_M: 0.5,
    hd.PORTRAIT_L: 0.1,
}

YAYAREA_PORTS = {
    hd.POPULAR_PORTRAIT: 0.75,
    hd.YAYAREA: 0.25,
}

YAYAREA_PORTS_SMALL = {
    hd.PORTRAIT_S: 0.10,
    hd.AESTHETIC_S: 0.15,
    hd.AESTHETIC_S: 0.25,
    hd.POPULAR_PORTRAIT: 0.25,
    hd.YAYAREA: 0.25,
}

GEN_SMALL = {
    hd.FILM_FEATURES: 0.2,
    hd.AESTHETIC_S: 0.5,
    hd.AESTHETIC_M: 0.2,
    hd.AESTHETIC_L: 0.1,
}

GEN_FILM = {
    hd.FILM: 0.8,
    hd.FILM_FEATURES: 0.2,
}

ASIA_FILM = {
    hd.FILM: 0.5,
    hd.FILM_FEATURES: 0.2,
    hd.JP_FILM: 0.2,
    hd.KR_FILM: 0.1,
}

GGB = {
    hd.GGB: 1.0,
}

TYPE_MAP = {
    'portraits': GEN_PORTS,
    'gen_ports_small': GEN_PORTS_SMALL,
    'gen_small': GEN_SMALL,
    'bayareaportraits': YAYAREA_PORTS,
    'general_film': GEN_FILM,
    'asia_film': ASIA_FILM,
    'ggb': GGB,
}
