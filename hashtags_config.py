import hashtags_data as hd

GEN_PORTS = {
	hd.POPULAR_PORTRAIT: 1.0
}

YAYAREA_PORTS = {
	hd.POPULAR_PORTRAIT: 0.75,
	hd.YAYAREA: 0.25,
}

GEN = {
	hd.GENERIC: 1.0
}

GEN_FILM = {
	hd.FILM: 0.67,
	hd.FILM_FEATURES: 0.33,
}

TYPE_MAP = {
    'portraits': GEN_PORTS,
    'general': GEN,
    'bayareaportraits': YAYAREA_PORTS,
    'general_film': GEN_FILM
}
