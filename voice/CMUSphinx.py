#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

#Directory for downloaded models
MODELDIR = "/usr/share/pocketsphinx/model"
#Data dir for the .wav files to decode
DATADIR = "/home/lalotone/Descargas"

# Decoder with the model, in this case english from US(default)
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

# Decode stream data, increased from 1024 to 2048
decoder = Decoder(config)
decoder.start_utt()
#Sample file for making some proofs
stream = open(path.join(DATADIR, 'hello.wav'), 'rb')
while True:
  buf = stream.read(2048)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Words decoded: ', [seg.word for seg in decoder.seg()])
