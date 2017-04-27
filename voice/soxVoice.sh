#For using it
# echo "SomethingToSay" | ./soxVoice

espeak --stdout -v male2 -s 120 | play -t wav - \
overdrive 10 \
echo 0.7 0.8 7 0.7 \
echo 0.7 0.8 7 0.7 \
echo 0.7 0.8 15 0.7 \
echo 0.7 0.8 15 0.7 \
echo 0.7 0.88 15 0.7 \
echo 0.7 0.88 15 0.7 \
echo 0.6 0.6 15 0.7 \
gain 4
