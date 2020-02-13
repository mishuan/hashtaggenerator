#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import argparse 
import random

### execute with in cmd prompt
### python c:\Users\Sydney\Desktop\hashtags.py -t portraits
### python c:\Users\Sydney\Desktop\hashtags.py -t portraits -n 30


generic = [
    "#broadmag",
    "#exploreobserveshare",
    "#magazine35mm",
    "#fujifilm_global",
    "#lookslikefilm",
    "#cerealmag",
    "#weltraumzine",
    "#oldtonecollective",
    "#exploreobserveshare",
    "#weltraumzine",
    "#fujifeed",
    "#imaginarymagnitude",
    "#somewheremagazine",
    "#ignant",
    "#fujilove",
    "#stademagazine",
    "#satellitetales",
]

# 100k+ followers
p_big = [
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

# 50k-100k followers
p_mid = [
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

# 20k-50k followers
p_small = [
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

# less than 20k followers
p_xsmall = [
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
    "#westcoastusa"
       
]

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
  "#24hrchruch"
  "#thecreatorclass"
  ]

fineart = [
    "#fineart",
    "#hurtlamb",
    "#ifyouleave",
    "subjectivelyobjective",
    "indies_minimal",
    "#staybasicly",
]
street = [
    "#streetphotography",
    "#lensonstreets",
    "#thesmartview",

]

minimalism = [
    "#gominimalmag",
    "#lucecurated",
]

bnw = [
    "#lightandshadow",
]

film =[
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
    "#analogphotography",
    "#analoguevibes",
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
    "kodakprofessional"
    "ilford",
    "ilfordfilm"
    "longlivefilm",
    "filmforever",
    "indiefilmlab",
    "selfdevelopedfilm",
    "#givemefilm",
    "#sharefilm",
    "filmisbetter",
    "#filmneverdies",
    "#filmcolor",
    "#filmonly",
    "#makefilmgreatagain",
    "#negativefb",
    "taintedfilm",
    "#photofilmy",
    "#thefilmgang",
    "#theanalogueproject",
    "#filmday",
    "#camerafilm",
    "#cinefilm",
    "#kodizes",
    "#oftheafternoon",
    "#135film"
    
    
]

filmfeatures = [
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
    "espritmag",
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
    "phroom",
    "#yetmagazine",
    "#lucecurated",
    "#lightzine",
    "#justifiedmagazine",
    
    
]

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
    "35mmbook",
    "35mmwaste",
    "#trip35",
    "#35mm_look",
    "#35mmmagazine",
    "#myfilm35mm",
]

film_medium_format = [
    "120film",
    "mediumformatfilm",
    "mediumformat",
    "#120"
    "#hexanon"
    "#bronicatribe"
    
    
]

kr_film = [
    "#감성사잔",
    "#필름",
    "#프로필자진",
]

jp_film = [
    "#フィルムカメラ",
    "#フィルム",
    "#フィルムに恋してる",
    "#胶片",
    "#film_com",
    "#film_japan",
    
]

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
    "#praktica"

]

spanish_film =[
    "#disparafilm"
    "#argentinaanalogica"
    "#disparaencarrete"
]


### List of lists for mapping

GEN_PORTS = [popular_portrait]
YAYAREA_PORTS = [popular_portrait, popular_portrait, popular_portrait, yayarea]
GEN = [generic]
GEN_FILM = [film,film,filmfeatures]


H_MAP = {
    'portraits': GEN_PORTS,
    'general': GEN,
    'bayareaportraits': YAYAREA_PORTS,
    'general_film': GEN_FILM
}


def add_to_hashtags(h_list, hashtags, size):
    c = 0
    tries = 0
    while c < size and tries < 10:
        rc = random.choice(h_list)
        if rc in hashtags:
            tries += 1
            continue
        else:
            hashtags.add(rc)
            c += 1


def gen_hashtags(photo_type, n=25):
    if n > 30:
        return "Maximum number of hastag is 30."

    if photo_type not in H_MAP:
      return f"'{photo_type}' is not a supported category."

    type_list = H_MAP[photo_type]
    type_list_len = len(type_list)
    chunk = n / type_list_len
    leftovers = 25 - chunk * type_list_len
    hashtags = set()

    # randomly sample from every hashtag list.
    for l in type_list:
        add_to_hashtags(l, hashtags, chunk)

    # randomly sample for the leftovers from one random hashtag list
    l = random.choice(type_list)
    add_to_hashtags(l, hashtags, leftovers)

    return "\n".join(hashtags)


def main(): 
    parser = argparse.ArgumentParser(description = "A #hashtag generator") 
    parser.add_argument("-t", "--type", type=str, required=True, help="Type of post (ie, portrait, landscape).") 
    parser.add_argument("-n", "--number", type=int, default=25, help="Number of hashtags.") 
    args = parser.parse_args() 
      
    print(gen_hashtags(args.type, args.number))


if __name__ == "__main__": 
    main()
