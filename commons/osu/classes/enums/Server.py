from enum import Enum
import commons.osu.classes as osu

class Server(Enum):
    BANCHO = (0, 'https://i.imgur.com/0aZpJjl.png',
        'https://osu.ppy.sh/api/get_user',
        'https://osu.ppy.sh/api/get_beatmaps',
        'https://osu.ppy.sh/api/get_user_best',
        'https://osu.ppy.sh/api/get_user_recent',
        'https://osu.ppy.sh/osu/',
        'https://a.ppy.sh/',
        'https://osu.ppy.sh/users/',
        'https://osu.ppy.sh/b/',
        'https://osu.ppy.sh/api/get_scores'
    )

    RIPPLE = (1, 'https://i.imgur.com/l4tTouZ.png',
        'https://ripple.moe/api/get_user',
        'https://osu.ppy.sh/api/get_beatmaps',
        'https://ripple.moe/api/get_user_best',
        'https://ripple.moe/api/get_user_recent',
        'https://ripple.moe/osu/',
        'https://a.ripple.moe/',
        'https://ripple.moe/u/',
        'https://ripple.moe/b/',
        'https://ripple.moe/api/get_scores'
    )

    AKATSUKI = (2, 'https://i.imgur.com/ic7kEkO.png',
        'https://akatsuki.pw/api/get_user',
        'https://osu.ppy.sh/api/get_beatmaps',
        'https://akatsuki.pw/api/get_user_best',
        'https://akatsuki.pw/api/get_user_recent',
        'https://osu.ppy.sh/osu/',
        'https://a.akatsuki.pw/',
        'https://akatsuki.pw/u/',
        'https://akatsuki.pw/b/',
        'https://akatsuki.pw/api/get_scores'
    )

    AKATSUKIRX = (3, 'https://i.imgur.com/ic7kEkO.png',
        'http://akatsuki.pw/api/v1/users/rxfull',
        'https://osu.ppy.sh/api/get_beatmaps',
        'https://akatsuki.pw/api/get_user_best',
        'https://akatsuki.pw/api/get_user_recent',
        'https://osu.ppy.sh/osu/',
        'https://a.akatsuki.pw/',
        'https://akatsuki.pw/rx/u/',
        'https://akatsuki.pw/b/',
        'https://akatsuki.pw/api/get_scores'
    )

    ENJUU = (4, 'https://i.imgur.com/OO6MrW7.png',
        'https://enjuu.click/api/get_user',
        'https://osu.ppy.sh/api/get_beatmaps',
        'https://enjuu.click/api/get_user_best',
        'https://enjuu.click/api/get_user_recent',
        'https://osu.ppy.sh/osu/',
        'https://a.enjuu.click/',
        'https://enjuu.click/u/',
        'https://enjuu.click/b/',
        'https://enjuu.click/api/get_scores')
    
    #TODO: Add gatari API links
    GATARI = (5, 'https://i.imgur.com/IAkYdrI.png', '', '', '', '', '', '', '', '', '')

    def __init__(self, id:int, icon:str,
            api_getuser:str,
            api_getbmap:str,
            api_getusrtop:str,
            api_getrecent:str,
            api_getbmaposu:str,
            url_avatar:str,
            url_profile:str,
            url_beatmap:str,
            api_getusrscores:str):
        self.__id = id
        self.__icon = icon
        self.api_getuser:str = api_getuser
        self.api_getbmap:str = api_getbmap
        self.api_getusrtop:str = api_getusrtop
        self.api_getrecent:str = api_getrecent
        self.api_getbmaposu:str = api_getbmaposu
        self.api_getusrscores:str = api_getusrscores

        self.url_avatar:str = url_avatar
        self.url_profile:str = url_profile
        self.url_beatmap:str = url_beatmap        

    # Maybe there is a better way to provide public members for an enum
    @property
    def id(self) -> str:
        return self.__id

    @property
    def icon(self) -> str:
        return self.__icon

    @staticmethod
    def from_name(param:str) -> 'Server':
        if param.startswith('-'):
            param = param[1:]
        return Server[param.upper()]
