class Filters:
    @staticmethod
    def to_lower(_s: str) -> str:
        return _s.lower()

    @staticmethod
    def to_upper(_s: str) -> str:
        return _s.upper()

    @staticmethod
    def convert_to_ru(_s: str, abc: any) -> str:
        _t = ""
        words = _s.split()
        for _i in words:
            for _l in _i:
                found = False
                for l_dict in abc:
                    for ru_l, translit in l_dict.items():
                        if _l in translit:
                            _t += ru_l
                            found = True
                            break
                    if found:
                        break
                if not found:
                    _t += _l
            _t += " "
        return _t.strip()
