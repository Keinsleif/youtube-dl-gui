# -*- coding: UTF-8 -*-

import gettext

from .utils import TwoWayOrderedDict as tdict


OUTPUT_FORMATS = tdict([
    (0, _("ID")),
    (1, _("Title")),
    (2, _("Title + ID")),
    (4, _("Title + Quality")),
    (5, _("Title + ID + Quality")),
    (3, _("Custom"))
])


DEFAULT_FORMATS = tdict([
    ("0", _("default"))
])


VIDEO_FORMATS = tdict([
    ("3gp", "3gp"),
    ("3gp[height=144]", "3gp [144p]"),
    ("3gp[height=240]", "3gp [240p]"),
    ("flv", "flv"),
    ("flv[height=240]", "flv [240p]"),
    ("flv[height=360]", "flv [360p]"),
    ("flv[height=480]", "flv [480p]"),
    ("webm", "webm"),
    ("webm[height=240]+bestaudio", "webm [240p]"),
    ("webm[height=360]+bestaudio", "webm [360p]"),
    ("webm[height=480]+bestaudio", "webm [480p]"),
    ("webm[height=720]+bestaudio", "webm [720p]"),
    ("webm[height=1080]+bestaudio", "webm [1080p]"),
    ("webm[height=1440]+bestaudio", "webm [1440p]"),
    ("webm[height=2160]+bestaudio", "webm [2160p]"),
    ("mp4", "mp4"),
    ("mp4[height=144]+bestaudio[ext=m4a]", "mp4 [144p]"),
    ("mp4[height=240]+bestaudio[ext=m4a]", "mp4 [240p]"),
    ("mp4[height=360]+bestaudio[ext=m4a]", "mp4 [360p]"),
    ("mp4[height=480]+bestaudio[ext=m4a]", "mp4 [480p]"),
    ("mp4[height=720]+bestaudio[ext=m4a]", "mp4 [720p]"),
    ("mp4[height=1080]+bestaudio[ext=m4a]", "mp4 [1080p]"),
    ("mp4[height=1440]+bestaudio[ext=m4a]", "mp4 [1440p]"),
    ("mp4[height=2160]+bestaudio[ext=m4a]", "mp4 [2160p]"),
    ("139", "m4a 48k (DASH Audio)"),
    ("140", "m4a 128k (DASH Audio)"),
    ("141", "m4a 256k (DASH Audio)"),
    ("171", "webm 48k (DASH Audio)"),
    ("172", "webm 256k (DASH Audio)")
])


AUDIO_FORMATS = tdict([
    ("mp3", "mp3"),
    ("wav", "wav"),
    ("aac", "aac"),
    ("m4a", "m4a"),
    ("vorbis", "vorbis"),
    ("opus", "opus"),
    ("flac", "flac")
])


FORMATS = DEFAULT_FORMATS.copy()
FORMATS.update(VIDEO_FORMATS)
FORMATS.update(AUDIO_FORMATS)


def reload_strings():
    # IF YOU DONT WANT YOUR EYES TO BLEED STOP HERE
    # YOU HAVE BEEN WARNED
    # DO NOT LOOK THE CODE BELOW
    #
    #
    #
    #
    #
    #
    #
    #
    #NOTE Remove
    # Code is so messed up that i need to reload strings else
    # the translations wont work on the about gettext tags
    global OUTPUT_FORMATS
    global DEFAULT_FORMATS
    global VIDEO_FORMATS
    global AUDIO_FORMATS
    global FORMATS

    OUTPUT_FORMATS = tdict([
        (0, _("ID")),
        (1, _("Title")),
        (2, _("Title + ID")),
        (4, _("Title + Quality")),
        (5, _("Title + ID + Quality")),
        (3, _("Custom"))
    ])


    DEFAULT_FORMATS = tdict([
        ("0", _("default"))
    ])


    VIDEO_FORMATS = tdict([
        ("3gp", "3gp"),
        ("3gp[height=144]", "3gp [144p]"),
        ("3gp[height=240]", "3gp [240p]"),
        ("flv", "flv"),
        ("flv[height=240]", "flv [240p]"),
        ("flv[height=360]", "flv [360p]"),
        ("flv[height=480]", "flv [480p]"),
        ("webm", "webm"),
        ("webm[height=240]+bestaudio", "webm [240p]"),
        ("webm[height=360]+bestaudio", "webm [360p]"),
        ("webm[height=480]+bestaudio", "webm [480p]"),
        ("webm[height=720]+bestaudio", "webm [720p]"),
        ("webm[height=1080]+bestaudio", "webm [1080p]"),
        ("webm[height=1440]+bestaudio", "webm [1440p]"),
        ("webm[height=2160]+bestaudio", "webm [2160p]"),
        ("mp4", "mp4"),
        ("mp4[height=144]+bestaudio[ext=m4a]", "mp4 [144p]"),
        ("mp4[height=240]+bestaudio[ext=m4a]", "mp4 [240p]"),
        ("mp4[height=360]+bestaudio[ext=m4a]", "mp4 [360p]"),
        ("mp4[height=480]+bestaudio[ext=m4a]", "mp4 [480p]"),
        ("mp4[height=720]+bestaudio[ext=m4a]", "mp4 [720p]"),
        ("mp4[height=1080]+bestaudio[ext=m4a]", "mp4 [1080p]"),
        ("mp4[height=1440]+bestaudio[ext=m4a]", "mp4 [1440p]"),
        ("mp4[height=2160]+bestaudio[ext=m4a]", "mp4 [2160p]"),
        ("139", "m4a 48k (DASH Audio)"),
        ("140", "m4a 128k (DASH Audio)"),
        ("141", "m4a 256k (DASH Audio)"),
        ("171", "webm 48k (DASH Audio)"),
        ("172", "webm 256k (DASH Audio)")
    ])


    AUDIO_FORMATS = tdict([
        ("mp3", "mp3"),
        ("wav", "wav"),
        ("aac", "aac"),
        ("m4a", "m4a"),
        ("vorbis", "vorbis"),
        ("opus", "opus"),
        ("flac", "flac")
    ])


    FORMATS = DEFAULT_FORMATS.copy()
    FORMATS.update(VIDEO_FORMATS)
    FORMATS.update(AUDIO_FORMATS)
