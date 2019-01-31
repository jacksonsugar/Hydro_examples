#! /bin/bash

nc -l 2222 | mplayer -fps 200 -demuxer h264es -
