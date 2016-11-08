Title:  TUT Acoustic scenes 2016, Evaluation dataset

TUT Acoustic scenes 2016, Evaluation dataset
=============================================
[Audio Research Group / Tampere University of Technology](http://arg.cs.tut.fi/)

Authors
- Toni Heittola (<toni.heittola@tut.fi>, <http://www.cs.tut.fi/~heittolt/>)
- Annamaria Mesaros (<annamaria.mesaros@tut.fi>, <http://www.cs.tut.fi/~mesaros/>)
- Tuomas Virtanen (<tuomas.virtanen@tut.fi>, <http://www.cs.tut.fi/~tuomasv/>)

Recording and annotation
- Eemi Fagerlund
- Aku Hiltunen

# Table of Contents
1. [Dataset](#1-dataset)
2. [Usage](#2-usage)
3. [Changelog](#3-changelog)
4. [License](#4-license)

1. Dataset
=================================

TUT Acoustic Scenes evaluation dataset consists of 30-seconds audio segments from 15 acoustic scenes: 

- Bus - traveling by bus in the city (vehicle)
- Cafe / Restaurant - small cafe/restaurant (indoor)
- Car - driving or traveling as a passenger, in the city (vehicle)
- City center (outdoor)
- Forest path (outdoor)
- Grocery store - medium size grocery store (indoor)
- Home (indoor)
- Lakeside beach (outdoor)
- Library (indoor)
- Metro station (indoor)
- Office  - multiple persons, typical work day (indoor)
- Residential area (outdoor)
- Train (traveling, vehicle)
- Tram (traveling, vehicle)
- Urban park (outdoor)

Each acoustic scene has 26 segments totaling 13 minutes of audio.

The dataset was collected in Finland by Tampere University of Technology between 06/2015 - 01/2016. The data collection has received funding from the European Research Council under the ERC Grant Agreement 637422 EVERYSOUND.

[![ERC](https://erc.europa.eu/sites/default/files/content/erc_banner-horizontal.jpg "ERC")](https://erc.europa.eu/)

### Preparation of the dataset

For all acoustic scenes, the recordings were captured each in a different location: different streets, different parks, different homes. The equipment used for recording consists of a binaural [Soundman OKM II Klassik/studio A3](http://www.soundman.de/en/products/) electret in-ear microphone and a [Roland Edirol R-09](http://www.rolandus.com/products/r-09/) wave recorder using 44.1 kHz sampling rate and 24 bit resolution. 

Postprocessing of the recorded data involves aspects related to privacy of recorded individuals, and possible errors in the recording process. For audio material recorded in private places, written consent was obtained from all people involved. Material recorded in public places does not require such consent, but was screened for content, and privacy infringing segments were eliminated. Temporary microphone failure and radio signal interferences from mobile phones were annotated and these annotations are provided. 

Audio material was cut into segments of 30 seconds length. 


### File structure

```
dataset root
│   README.md				this file, markdown-format
│   README.html				this file, html-format
│   EULA.pdf				End user license agreement
│
└───audio					1170 audio segments, 24-bit 44.1kHz
│   │   1.wav		name format [original_recording_identifier]_[start sec (int)]_[end sec (int)].wav
│   │   2.wav
│   │   ...
│
└───evaluation_setup		cross-validation setup, 4 folds
    │   test.txt 			testing file list, csv-format, [audio file (string)]

```

2. Usage
=================================

The partitioning of the data was done based on the location of the original recordings. All segments obtained from the same original recording were included into a single subset - either **development dataset** or **evaluation dataset**. For each acoustic scene, 78 segments were included in the development dataset and 26 segments were kept for evaluation. Development dataset is provided separately.

### Evaluation setup

#### Testing

`evaluation setup\test.txt`
: testing file list (in csv-format)

Format:
    
    [audio file (string)]

3. Changelog
=================================
#### 1.0 / 2016-05-31
* Initial commit for DCASE2016 challenge

4. License
=================================

See file [EULA.pdf](EULA.pdf)