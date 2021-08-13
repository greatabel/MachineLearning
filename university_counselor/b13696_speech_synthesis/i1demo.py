import sox
# create combiner
cbn = sox.Combiner()
# pitch shift combined audio up 3 semitones
#cbn.pitch(3.0)
# convert output to 8000 Hz stereo
#cbn.convert(samplerate=8000, n_channels=2)
# create the output file

mylist  = []
for i in range(0, 8+1):
    #name = 'demo_output_0' + str(i) +'.wav'
    name =  "output_folder/demo_output_%02d.wav" % i
    print('name=',name)
    mylist.append(name)
print(mylist)
cbn.build(
    mylist, 'output_folder/output3.wav', 'concatenate'
)
# the combiner does not currently support array input/output