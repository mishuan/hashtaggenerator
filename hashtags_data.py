#!/usr/bin/env python
# Map string identifier to list
LIST_MAP = {}

FUJIFLM = 'fujifilm'
fujifilm = [
    "#fujilove",
    "#fujifeed",
    "#fujifilm_global",
]
LIST_MAP[FUJIFLM] = fujifilm

# 100k+ followers
PORTRAIT_L = 'portrait_l'
portrait_l = [
    "@quietthechaos #quietthechaos",
    "@portraitpage #portraitpage",
    "@waitingontheworld #ftwotw",
    "@ofhumans #featuredmeofh",
    "@expofilm #expofilm",
    "@dark.daisies #ftmedd",
    "@l0tsabraids_ #l0tsabraids",
    "@hinfluencercollective #hinfluencercollective",
    "@sticks_and_stones_agency #postmypicssticks",
    "@cheadsmagazine #cheadsmagazine",
    "@marvelous_shots #marvelous_shots",
    "@myphotoshop_ #myphotoshop",
    "@of2humans #of2humans",
    "@earth_portraits #earth_portraits",
    "@aovportraits #aovportraits",
    "@theportraitpr0ject #theportraitpr0ject",
    "@portraitmood #portraitmood",
    "@darkmornings #darkmornings",
    "@filmpalette #featurepalette",
    "@portraitmood",
    "@silver.seas #featuremeseas",
    "@igpodium_portraits #igpodium_portraits",
    "@freepeople -#freepeople",
    "@hot_is_the_new_black #hotisthenewblack",
    "@createcommune #createcommune",
    "@portraitsfromtheworld #portraitsfromtheworld",
    "@kdpeoplegallery  #kdpeoplegallery",
    "@majestic_people_ #majestic_people_",
    "@portraits_mf #portraits_mf",
    "@portraitfestival #portraitfestival",
    "@peoplephotatoes #peoplephotatoes",
    "@portraitsfromtheworld #portraitsfromtheworld",
    "@ourmoodydays #ourmoodydays",
    "@endlessfaces #endlessfaces",
    "@bravogreatphoto #bravogreatphoto",
    "@last.daze #lastdaze",
    "@thoughtcatalog #thoughtcatalog 172k followers",
]
LIST_MAP[PORTRAIT_L] = portrait_l

# 50k-100k followers
PORTRAIT_M = 'portrait_m'
portrait_m = [
    "@tangledinfilm #tangledinfilm",
    "@pursuitofportraits #pursuitofportraits",
    "@oblivioncreature #featureacreature",
    "@winterwillneverend #ftwwne",
    "@portraitvision #portraitvision",
    "@postthepeople #postthepeople",
    "@peoplefeature #featuremepf",
    "@makeportrait #makeportraits",
    "@instagramskilla #gramkilla",
    "@oceanfeatures #cooloceann",
    "@globe_people #globe_people",
    "@2instagood #2instagoodportraitlove",
    "@seekingthestars #seekingthestars",
    "@portraits_mf #portraits_mf",
    "@moodyports #moodyports",
    "@pr0ject_soul #pr0ject_soul",
    "@bravoportraits #bravoportraits",
    "@rainbow.features #rainbowfeatures",
    "@vscoportrait #vcsoportrait",
    "@folkportraits #folkportraits",
    "@makeportrait #makeportrait",
    "@vscoportrait #vscoportrait",
]
LIST_MAP[PORTRAIT_M] = portrait_m

# 20k-50k followers
PORTRAIT_S = 'portrait_small'
portrait_s = [
    "@vogove #vogove",
    "@portrait_society #portraitsociety",
    "@luisthechickengod #theswaggingchicken",
    "@herefallsthenight #herefallsthenight",
    "@discoverportrait #discoverportrait",
    "@makeportraitsmag #makeportraitsmag",
    "@earth.portraits #earthportraits",
    "@portraitgames #portraitgames",
    "@portrait_perfection #portraitperfection",
    "@portraitfolk #portraitfolk",
    "@creative_portraits #creative_portraits",
    "@hvmansouls #hvmansouls",
    "@lensofourlives #lensofourlives",
    "@portraitstream #portraitstream",
    "@portraitsmag #portraitsmag",
    "@yourvisiongallery #yourvisiongallery",
    "@projectphotoshop #projectphotoshop",
]
LIST_MAP[PORTRAIT_S] = portrait_s

# less than 20k followers
PORTRAIT_XS = 'portrait_xsmall'
portrait_xs = [
    "less than 20k followers",
    "@portraitsofgirls #portraitsofgirls",
    "@portrait_vision #portrait_vision",
    "@portraitfeature #portraitfeature",
    "@artofportrait_ #artofportrait",
    "@777luckyfish #777luckyfish",
    "@pulsefilm #pulsefilm",
    "@ig_muse #ig_muse",
    "@skilled_portraits #skilled_portraits",
    "@iiwiimag #iiwiimag",
    "@watchingfilms #featuremefilms",
    "@envisiontones #envisiontones",
    "@oursecrethidden #oursecrethidden",
    "@modernmoons #modernmoons",
    "@chasingessence #chasingessence",
    "@featureacc #featureworlds",
    "@flakemagazine #featuremeflake",
    "@obliviousfilm #featuremeof",
    "@creative_portraits #creative_portraits",
    "@portraitsatl #portraitsatl",
    "@portraits_la #portraitsla",
    "@portraitkillers #portraitkillers",
    "@ambientfeature #ambientfeature",
    "@artistfound #artistfound",
    "@exploremoreportraits #exploremore",
    "#shootlikeaboss",
    "#xelfies",
    "#portraitmeet",
    "#awesomeportrait",
    "#hurtlamb",
    "#theportraitcentral",
]
LIST_MAP[PORTRAIT_XS] = portrait_xs

YAYAREA = 'yayarea'
yayarea = [
    "#bayareaphotographer",
    "#bayareaphotography",
    "#bayareamodel",
    "#bayareamodels",
    "#sacramentophotographer",
    "#sacramentophotography",
    "#sacmodel",
    "#sacramentomodel",
    "#norcalphotographer",
    "#norcalphotography",
    "#californiaphotographer",
    "#californiaphotography",
    "#sanjosephotographer",
    "#sanjosephotography",
    "#sfphotographer",
    "#sfphotography",
    "#sfmodel",
    "#westcoastusa",
]
LIST_MAP[YAYAREA] = yayarea

VIDEOGRAPHY_GENERAL = 'videography_general'
videography_general = [
    "#freelancevideographer",
    "#videoproductioncompany",
    "#videographers",
    "#videography",
    "#mediacompany",
    "#videoproduction",
    "#cameradept",
    "#cameralust",
    "#eventvideography",
    "#eventvideographer",
    "#corporatevideo",
    "#onlocation",
    "#onset",
    "#production",
    "#productionhouse",
    "#productionmanager",
    "#productioncompany",
    "#directorofphotography",
    "#directorslife",
    "#dp",
    "#dop",
    "#doplife",
    "#filmmkrs",
    "#filmmakerlife",
    "#filmmakersworld",
    "#filmmakersofinstagram",
    "#filmmakers",
    "#filmgear",
    "#filmset",
    "#filmcrew",
    "#filmsetlife",
    "#cameraoperator",
    "#cinematographers",
    "#cinematography",
    "#moviemaker",
    "#indiefilmmaking",
    "#filmmaking",
    "#moviemaking",
    "#videoedit",
    "#videoedits",
    "#motiongraphics",
    "#cameraman",
    "#lifeonset",
]
LIST_MAP[VIDEOGRAPHY_GENERAL] = videography_general

POPULAR_PORTRAIT = 'popular_portrait'
popular_portrait = [
    "#portraitphotography",
    "#artofvisuals",
    "#777luckyfish",
    "#portvisual",
    "#pursuitofportrait",
    "#theportraitpro0ject",
    "#portraitvisuals",
    "#weshoothumans",
    "#portraitsociety",
    "#portrait_mood",
    "#portrait_star",
    "#portrait_vision",
    "#portraitvision",
    "#portrait_mf",
    "#discoverportraits",
    "#portraitstream",
    "#portraitgasm",
    "#portraitsquad",
    "#portraitkillers",
    "#portrait_wizard",
    "#under10kportraits",
    "#wmportraits",
    "#portraitfeed",
    "#portraituniverse",
    "#nextvisualportraits",
    "#aovportraits",
    "#ourportraitdays",
    "#bravogreatportrait",
    "#portraitsinspire",
    "#portraitspg",
    "#justportrait",
    "#bestshooter_portraits",
    "#portrait_shots",
    "#portrait_today",
    "#portraitlovers",
    "#portraitureinspirations",
    "#germanportraiture",
    "#portraitshooting",
    "#ig_ports",
    "#top_portraits",
    "#portraitstyles_gf",
    "#life_portraits",
    "#rsa_portraits",
    "#portraits_universe",
    "#majestic_people",
    "#portraitpage",
    "#igpodium_portraits",
    "#portraitmood",
    "#portraiture",
    "#portraits",
    "#portraitphotographer",
    "#agameofportraits",
    "#moodyports",
    "#portraidhood",
    "#portraitcentral",
    "#theportraitcentral",
    "#portraitsmag",
    "#worldofportraits",
    "#folkportrait",
    "#globe_people",
    "#portraits_perfection",
    "#portrait_shooterz",
    "#portrait_shooters",
    "#portrait_pros",
    "#portrait_styles",
    "#thelightsofbeauty",
    "#doports",
    "#portraisedition",
    "#yourvisiongallery",
    "#theportraitculture",
    "#portraitgames",
    "#gramkilla",
    "#igportrait",
    "#portrait_shot",
    "#creativeportraits",
    "#portraitfestival",
    "#portraits_today",
    "#endlessfaces",
    "#ig_muse",
    "#artofportrait",
    "#portrait_legit",
    "#portraitinspiration"
    "#discoverunder1k",
    "#discoverunder20k",
    "#discoverunder10k",
    "#portraitlove",
    "#instagood",
    "#theworldofportraits",
    "#portraitscam",
    "#portraitplay",
    "#creatives_lounge",
    "#quietthechaos",
    "#ftwotw",
    "#ftmedd",
    "#l0tsabraids",
    "#hinfluencercollective",
    "#postmypicssticks",
    "#cheadsmagazine",
    "#myphotoshop",
    "#of2humans",
    "#earthportraits",
    "#darkmornings",
    "#featurepalette",
    "#featuremeseas",
    "#freepeople",
    "#hotisthenewblack",
    "#createcommune",
    "#portraitsfromtheworld",
    "#kdpeoplegallery",
    "#peoplephotatoes",
    "#ourmoodydays",
    "#lastdaze",
    "#thoughtcatalog",
    "#featurecreature",
    "#ftwwne",
    "#postthepeople",
    "#featuremepf",
    "#makeportraits",
    "#cooloceann",
    "#2instagoodportraitlove",
    "#seekingthestars",
    "#pr0ject_soul",
    "#rainbowfeatures",
    "#vscoportrait",
    "#vogove",
    "#theswaggingchicken",
    "#portraitperfection",
    "#hvmansouls",
    "#lensofourlives",
    "#skilled_portraits",
    "#iiwiimang",
    "#envisiontones",
    "#oursecrethidden",
    "#modernmoons",
    "#chasingessence",
    "#featureworlds",
    "#featuremeflake",
    "#featuremeof",
    "#ambiantfeature",
    "#artistfound",
    "#exploremore",
    "#majesticcasual",
    "#24hrchruch",
    "#thecreatorclass",
]
LIST_MAP[POPULAR_PORTRAIT] = popular_portrait

FINE_ART = 'fine_art'
fine_art = [
    "#fineart",
    "#hurtlamb",
    "#ifyouleave",
    "#subjectivelyobjective",
    "#indies_minimal",
    "#staybasicly",
]
LIST_MAP[FINE_ART] = fine_art

STREET = 'street'
street = [
    "#streetphotography",
    "#lensonstreets",
    "#thesmartview",
    "#ig_streetphotography",
    "#spicollective",
    "#streetsunseen",
    "#thedecisivemoment",
    "#thecommoneye",
    "#allcitiesarebeautiful",

]
LIST_MAP[STREET] = street

MINIMALISM = 'minimalism'
minimalism = [
    "#gominimalmag",
    "#lucecurated",
]
LIST_MAP[MINIMALISM] = minimalism

BNW = 'bnw'
bnw = [
    "#lightandshadow",
    "#bnw_drama",
    "#friendsinbnw",
]
LIST_MAP[BNW] = bnw

FILM = 'film'
film = [
    "#filmphotographers",
    "#filmphotographyday",
    "#filmphotoshare",
    "#filmphotografic",
    "#filmphotographyisnotdead",
    "#filmphotographybaguio",
    "#filmphotorussia",
    "#filmphotographyisgrowing",
    "#filmphotographyindia",
    "#filmphotogram",
    "#filmphoto",
    "#filmphotographic",
    "#filmphotographer",
    "#filmphotograph",
    "#filmphotos",
    "#filmphotooftheday",
    "#filmphotographyproject",
    "#analog",
    "#analogue",
    "#analogfilm",
    "#analogfilmlab",
    "#analogphotography",
    "#analogphotographer",
    "#analoguevibes",
    "#analogmood",
    "#analogblog",
    "#analogpeople",
    "#analogshooters",
    "#analogfever",
    "#analogfromtheworld",
    "#analogarithmic",
    "#analoguelove",
    "#mm",
    "#film",
    "#filmisnotdead",
    "#ishootfilm",
    "#infilmwetrust",
    "#mmfilm",
    "#kodak",
    "#filmcommunity",
    "#filmcamera",
    "#shootfilm",
    "#filmfeed",
    "#believeinfilm",
    "#staybrokeshootfilm",
    "#filmisalive",
    "#grainisgood",
    "#buyfilmnotmegapixels",
    "#keepfilmalive",
    "#mmphotography",
    "#vintage",
    "#lomography",
    "#fujifilm",
    "#filmwave",
    "#istillshootfilm",
    "#theanalogclub",
    "#canon",
    "#kodakfilm",
    "#minolta",
    "#onfilm",
    "#shotonfilm",
    "#filmphotographic",
    "#nikon",
    "#portra",
    "#filmwave",
    "#baeareafilm",
    "#theanalogclub",
    "#believeinfilm",
    "#everybodyfilm",
    "#filmfeed",
    "#filmphotographic",
    "#pulsefilm",
    "#nowherediary",
    "#fujifilm",
    "#filmshooters",
    "#believeinfilm",
    "#onfilm",
    "#filmshooterscollective",
    "#filmcommunity",
    "#bestfilmphoto",
    "#shootitwithfilm",
    "#shootonfilm",
    "#filmshooterscollective",
    "#madewithkodak",
    "#heyfsc",
    "#back2thebase",
    "#kodaklosers",
    "#drivebyfilm",
    "#restorefrombackup",
    "#blurbsonfilm",
    "#deathb4digital",
    "#thefilmpublic",
    "#rolledgoldfilm",
    "#thefilmrenaissance",
    "#photozine",
    "#analogue_people",
    "#shootaesthetics",
    "#filmisgood",
    "#kodakprofessional"
    "#ilford",
    "#ilfordfilm"
    "#longlivefilm",
    "#filmforever",
    "#indiefilmlab",
    "#selfdevelopedfilm",
    "#givemefilm",
    "#sharefilm",
    "#filmisbetter",
    "#filmneverdies",
    "#filmcolor",
    "#filmonly",
    "#makefilmgreatagain",
    "#negativefb",
    "#taintedfilm",
    "#photofilmy",
    "#thefilmgang",
    "#theanalogueproject",
    "#filmday",
    "#camerafilm",
    "#cinefilm",
    "#kodizes",
    "#oftheafternoon",
    "#135film",
    "#thefilmcollectives",
    "#thefilmcollective",
    "#leicalosers",
    "#burbsonfilm",
    "#shootfilmunder1000",
    "#filmdiscovered",
    "#moderndayanalogue",
    "#minoltagang",
    "#shootfilmnotbullets",
    "#nograinnoglory",
    "#shootmorefilm",
    "#beforepixel",
    "#c41",
    "#wearefilmfolks",
    "#negativelabpro",
    "#holygrainfilmcollective",
    "#thefilmshot",
    "#filmcameraclub",
    "#bleachmyfilm",
    "#filmcamerainternational",
    "#filmcommunityph",
    "#retroikafilme",
    "#film365life",
    "#lovefilmclub",
    "#filmgrain",
    "#ibelieveinfilm",
    "#loveoldlensclub",
    "#girlsonfilm",
]
LIST_MAP[FILM] = film

FILM_FEATURES = 'film_features'
film_features = [
    "#shootfilmmag",
    "#filmphotomag",
    "#photocinematica",
    "#somewheremagazine",
    "#dreamermagazine",
    "#thinkverylittle",
    "#pellicolamag",
    "#classicmagazine",
    "#goldmoony",
    "#analogfeatures",
    "#boxspeedfeature",
    "#makemeseemag",
    "#nowherediary",
    "#senekamagazine",
    "#rentalmag",
    "#espritmag",
    "#indiependentmag",
    "#etczine",
    "#missnothingmag",
    "#realismag",
    "#taintedmag",
    "#framepressmag",
    "#theoctobermagazine",
    "#gominimalmag",
    "#tintomag",
    "#verybusymag",
    "#collecmag",
    "#noicemag",
    "#phroommagazine",
    "#paperjournalmag",
    "#aintbadmagazine",
    "#foammagazine",
    "#phroom",
    "#yetmagazine",
    "#lucecurated",
    "#lightzine",
    "#justifiedmagazine",
    "#dietcolazine",
    "#afilmcosmos",
]
LIST_MAP[FILM_FEATURES] = film_features

FILM_35MM = 'film_35mm'
film_35mm = [
    "#35mm",
    "#35mmphotography",
    "#35mmfilmphotography",
    "#35mmstreetphotography",
    "#35mmfilmphoto",
    "#35mmcamera",
    "#35mmphoto",
    "#35mmfilm",
    "#thedaily35mm",
    "#35mmbook",
    "#35mmwaste",
    "#trip35",
    "#35mm_look",
    "#35mmmagazine",
    "#myfilm35mm",
    "#35fuckingmillimeter"
    "#thirtyfivefuckingmillimeter",
]
LIST_MAP[FILM_35MM] = film_35mm

FILM_MEDIUM_FORMAT = 'film_medium_format'
film_medium_format = [
    "#120film",
    "#120",
    "#120mm",
    "#mediumformatfilm",
    "#mediumformat",
    "#hexanon",
    "#bronicatribe",
    "#中判カメラ",
    "#中画幅",
]
LIST_MAP[FILM_MEDIUM_FORMAT] = 'film_medium_format'

KR_FILM = 'kr_film'
kr_film = [
    "#필름",
    "#필카",
    "#필름사진",
    "#필름감성"
    "#필름스냅"
    "#필름카메라",
    "#코닥필름",
    "#사진취미",
    "#현상소",
    "#필름느낌",
]
LIST_MAP[KR_FILM] = kr_film

KR_GENERAL = 'kr_general'
kr_general = [
    "#개인화보",
    "#스냅사진",
    "#스냅촬영",
    "#스냅",
    "#포트레이트",
    "#홈스냅",
    "#유료촬영",
    "#일상스냅",
    "#감성",
    "#풍경",
    "#카페스냅",
    "#카페스타그램",
    "#사진소통",
    "#무보정",
    "#일반인모델",
    "#일반인촬영"
    "#촬영",
    "#프로필촬영",
    "#프로필"
    "#촬영문의",
    "#인물사진",
    "#인물촬영"
    "#감성사진",
    "#우정스냅",
    "#개인스냅",
    "#상호무페이",
    "#배우프로필사진",
]
LIST_MAP[KR_GENERAL] = kr_general

JP_FILM = 'jp_film'
jp_film = [
    "#フィルムカメラ",
    "#フィルム",
    "#フィルム写真",
    "#フィルム写真部",
    "#フィルム写真普及委員会"
    "#フィルムと生活",
    "#フィルムに恋してる",
    "#フィルム好きな人と繋がりたい",
    "#フィルムに魅せられて",
    "#フィルムカメラ好きな人と繋がりたい",
    "#フィルムカメラ普及委員会",
    "#フィルムカメラ初心者",
    "#フィルムカメラに恋してる",
    "#フィルム普及委員会",
    "#フィルムで残す日常",
    "#フィルム寫眞",
    "#日々フィルム",
    "日常に魔法をかけて",
    "#ふぃるむ寫眞",
    "#オートボーイ",
    "#写ルンですのある生活",
    "#その瞬間に物語を",
    "#胶片",
    "#銀塩",
    "生活とフィルム",
    "#恋するオールドレンズ部",
    "#hibiプリ",
    "#kodakで写す冬",
    "#film_com",
    "#film_japan",
    "#film365life",
    "#autoboy",
    "#sunday_film_"
    "#reco_ig",
    "#loveoldlensclub",
    "#vague_memories",
    "#into_the_screen",
    "#hueart_life",
]
LIST_MAP[JP_FILM] = jp_film

JP_GENERAL = 'jp_general'
jp_general = [
    "#人物写真",
]
LIST_MAP[JP_GENERAL] = jp_general


TW_FILM = 'tw_film'

tw_film = [
    "#銀塩",
    "#銀鹽写真",
    "#老靈魂",
    "#底片魂",
    "#银盐"
    "#胶片",
    "#膠片",
    "#胶片摄影",
    "#胶片写真",
    "#胶片的味道",
    "#胶片约拍"
    "#底片",
    "#底片日常",
    "#底片攝影",
    "#底片相機",
    "#菲林相機",
    "#菲林",
    "#膠卷",
    "#showa_photo",
    "#foto_tw",
    "#filmintaiwan",
]
LIST_MAP[TW_FILM] = tw_film

CN_GENERAL = 'cn_general'
cn_general = [

]
LIST_MAP[CN_GENERAL] = cn_general

RU_FILM = 'ru_film'
ru_film = [
    "#пленка35мм",
    "#пленочнаяфотография",
    "#35mmrussia",
    "#плёнка",
    "#пленочка",
    "#пленкафото",
    "#пленка"
    "#фотонапленку",
    "#фотоназенит"
    "#аналоговаяфотография",
    "#зенитет",
    "#напленку",
    "#зенит12сд",
    "#зенитттл",
    "#зенитфото"
    "#plenkafriends",
    "#35ммплівка",
    "#plenka",
    "#zenitet",
    "#zenit11",
    "#zenet12xp",
    "#zenitphoto",
    "#кодак",
    "#praktica",

]
LIST_MAP[RU_FILM] = ru_film

SPANISH_FILM = 'spanish_film'
spanish_film = [
    "#disparafilm"
    "#argentinaanalogica"
    "#disparaencarrete",
]
LIST_MAP[SPANISH_FILM] = spanish_film

INDO_FILM = 'indo_film'
indo_film = [
    "#indo35mm",
    "#hipercatlab",
    "#jellyplayground",
    "#retroikafilme",
]
LIST_MAP[INDO_FILM] = indo_film

# tags with 10k-100k submissions
AESTHETIC_S = 'aesthetic_s'
aesthetic_s = [
    '#nothinglessmag',
    '#auressa',
    '#fadedaesthetics',
    '#saturdaysmag',
    '#fujifilmxe3',
    '#etczine_trip',
    '#thezonezine',
    '#myfujifilmlegacy',
    '#fujinon35mmf14',
    '#vintagefeed',
    '#nowheremagazine',
    '#aestheticvibe',
    '#aestheticsoft',
    '#fujixpro3',
    '#tnscollective',
    '#cinesomnia',
    '#protectyourhighlights',
    '#creatorcommune',
    '#mytinyatlashello',
    '#thislifemagazine',
    '#voyagecollective',
    '#dreamagazine',
    '#concretewaveco',
    '#nextjauntmag',
    '#satellitetales',
    '#fujixpassion',
    '#fujixphotographer',
    '#fujifilmxe1',
    '#sweetnesday',
]
LIST_MAP[AESTHETIC_S] = aesthetic_s

# tags with 100k-300k submissions
AESTHETIC_M = 'aesthetic_m'
aesthetic_m = [
    '#focalzine',
    '#classicchrome',
    '#Onearthmagazine',
    '#documentingspace',
    '#dazedandexposed',
    '#24hrchurch',
    '#theoctobermagazine',
    '#xphotographer',
    '#minimablu',
    '#fujifilmx',
    '#retrovibes',
    '#fujixlovers',
    '#kodizes',
    '#observationmag',
    '#anotherplacemagazine',
    '#futurebalance',
    '#somewheremag',
    '#ifyouleavestagram',
    '#pixsoulmag',
    '#floatmagazine',
    '#shootaesthetics',
    '#insomniamag',
    '#fujixshooters',
    '#fujiphotography',
    '#lightaesthetic',
    '#fujixfam',
    '#fujifilmxt30',
    '#fujifilmxh1',
    '#fujilovers',
    '#aestheticvibes',
    '#aestheticinspiration',
    '#takemagazine',
    '#staycinematic',
    '#nuagesmagazine',
    '#la_minimal',
    '#anotherescape',
    '#stademagazine',
    '#oksfieldmag',
    '#palepalmcollection',
    '#thinkveryfilm',
    '#tinypeopleinbigplaces',
    '#rundownmagazine',
    '#freshairclub',
    '#repostmyfuji',
    '#curiouscameraclub',
    '#fivesixmag',
    '#aintbad',
    '#opendoorsgallery',
    '#theheavycollective',
    '#nightwalkermagazine',
]
LIST_MAP[AESTHETIC_M] = aesthetic_m

AESTHETIC_L = 'aesthetic_l'
aesthetic_l = [
    '#makemeseemag',
    '#reframedmag',
    '#worldviewmag',
    '#hippomag',
    '#thisveryinstant',
    '#weltraumzine',
    '#odtakeovers',
    '#aestheticphotos',
    '#fujixclub',
    '#fuji_xseries',
    '#espritmag',
    '#aesthetictheme',
    '#n8zine',
    '#exploreobserveshare',
    '#magazine35mm',
    '#cerealmag',
    '#oldtonecollective',
    '#imaginarymagnitude',
    '#ozshotmag',
    '#ignantpicoftheday',
    '#solarcollective',
    '#wherewillwegonext',
    '#fujiframez',
    '#phornography',
    '#thisaintartschool',
    '#burnmagazine',
    '#apricotmagazine',
    '#yetmagazine',
    '#indiependentmag',
    '#collecmag',
    '#onbooooooom',
]
LIST_MAP[AESTHETIC_L] = aesthetic_l

SF = 'sf'
sf = [
    '#sfgate',
    '#sfpulse',
    '#sf_creatives',
    '#bay_shooters',
    '#sf_insta',
    '#wildbayarea',
    '#ilovesf',
    '#ig_california',
    '#sf_insta',
    '#sfbayarea',
    '#igerssf',
]
LIST_MAP[SF] = sf

GGB = 'ggb'
ggb = [
    '#ggb',
    '#sanfranciscocity',
    '#sflife',
    '#sanfranciscobay',
    '#goldengatebridge',
    '#goldengate',
    '#sanfran',
    '#sfgate',
    '#sfpulse',
    '#sf_creatives',
    '#bay_shooters',
    '#sf_insta',
    '#wildbayarea',
    '#ilovesf',
    '#sf_insta',
    '#sfbayarea',
    '#igerssf',
]
LIST_MAP[GGB] = ggb
