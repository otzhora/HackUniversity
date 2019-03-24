# About DJS

## Requirements @ HackUniversity
This application was done under HackUniversity campaing (3/22/2019 - 3/24/2019).
The case to solve: Audio & Open (Linux) Software.
It was required to develop an application from scratch, that would allow to do mastering & mixing operations for the DJs.

## Features
Mastering & mixing - is a time-intesive routine. One could spent 10s of hours to produce a nice looking mix. For sure, noone can substitue the DJ, but we could try to make tjeir life a bit easier.

DJS app tends to do basic operations & simplify mixed records creation. In addition the resulting tracks could be played separately by the audience, e.g. when the DJ wants to share his progress to the user to make judjments, likes and so one. 

The overall workflow:
![DJ workflow](/wiki/Workflow.png)



There are 2 main apps:
 - DJ MIxer
 - MasterTrack Player


### DJ Mixer

#### Main DJ window

![Main DJ window](/wiki/dj_screen.png)

#### DJ plays tracks

![Main DJ - playing & info ](/wiki/dj_screen_info.png)

#### Track player control

![Main DJ - track](/wiki/dj_screen_track.png)

#### Mixer control

![Main DJ - track](/wiki/dj_mixer_controls.png)


### Master Track Player
![Main player - track](/wiki/main_screen.png)

#### Master Track

![Master Track](/wiki/main_screen_playing.png)

#### Mixing tracks
![Master Track](/wiki/main_screen_info.png)

# Tech Details

## Implementation Details

Being a very technically oriented task, some steps of the audio processing could be simplified. E.g. bits comparison, playback, tone tuning, instruments segmentation and so on. Another important part is applying different kinds of effects and filters.

It was required to support VTS filters. Unfortunatelly we were not able to find any base oriented products that support VTS filters. It is supposed to be a pure C++ libraries, that could be hosted in the desktop environments by (mostly) paid software.

There are some analogues of the VST for Web - WAM - ![Web Audio Modules](https://www.webaudiomodules.org/), that possibly could be integrated in the web apps. As alternative, there would be required a separate VST server that would host the C++ plugins and produce the audio results. 

We think this is a far more complex and does not fit in the Hackathons format. Thus we developed applications (as required), implemented 2 js filters, similar to VST & were concentrated on the mastering & mixing features.

Technical architecture:
![Technical architecture](/wiki/Tech-Architecture.png)

## How to run

//TBD

## Components & Tools used

https://wavesurfer-js.org

Server side:
 - python
 - Flask
 - Node.js (as a development environment)
 - librosa

Front: 
 - Vue.js
 - Icons8
 - Tone.js
 - Bulma.css
 
Hosting:
 - REG.RU

# Thanks

- To Organizers!
- To Experts
- To people, who are involved into OpenSource comminuty and drive it
- To A-Team =)